from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from model.encoder import Encoder
from model.decoder import Decoder
from model.attentionLayer import ScaledDotProductAttention
from config.variables import X_TOKENIZER_PATH, Y_TOKENIZER_PATH, MODEL_PATH
import pickle
from rouge_score import rouge_scorer

class TextSummarizer:
    LATENT_DIM = 300
    EMBEDDING_DIM = 100
    MAX_LEN_TEXT = 150
    MAX_LEN_SUMMARY = 10
    X_TOKENIZER_PATH = X_TOKENIZER_PATH
    Y_TOKENIZER_PATH = Y_TOKENIZER_PATH

    def __init__(self):
        self.model = load_model(MODEL_PATH, custom_objects={'ScaledDotProductAttention': ScaledDotProductAttention})
        self.encoder_model = Encoder(self.model)
        self.decoder_model = Decoder(self.model, self.LATENT_DIM, self.MAX_LEN_TEXT)
        
        with open(self.X_TOKENIZER_PATH, 'rb') as handle:
            self.x_tokenizer = pickle.load(handle)
        
        with open(self.Y_TOKENIZER_PATH, 'rb') as handle:
            self.y_tokenizer = pickle.load(handle)

        self.reverse_target_word_index=self.y_tokenizer.index_word
        self.reverse_source_word_index=self.x_tokenizer.index_word
        self.target_word_index=self.y_tokenizer.word_index

    def summarize(self, text):
        # Preprocess the text as required by your model
        preprocessed_text = self.preprocess(text)
        
        # Predict summary and convert it back to text
        summary = self.predict(preprocessed_text)
        
        return summary

    def preprocess(self, text):
        
        # Tokenize the input text
        x_seq = self.x_tokenizer.texts_to_sequences([text])

        # Pad the input sequences
        x_seq = pad_sequences(x_seq, maxlen=self.MAX_LEN_TEXT, padding='post')

        return x_seq


    def evaluate(self, reference_summary, summary, metrics=['rouge1', 'rougeL']):
        
        # Calculate ROUGE scores
        scorer = rouge_scorer.RougeScorer(metrics, use_stemmer=True)
        scores = scorer.score(summary, reference_summary)
        
        return scores

    def predict(self, input_seq):
        # Encode the input as state vectors.
        e_out, e_h, e_c = self.encoder_model.predict(input_seq)

        # Generate empty target sequence of length 1.
        target_seq = np.zeros((1, 1))

        # Choose the 'start' word as the first word of the target sequence
        target_seq[0, 0] = self.target_word_index['start']

        stop_condition = False
        decoded_sentence = ''
        while not stop_condition:
            output_tokens, h, c = self.decoder_model.predict(target_seq, e_out, e_h, e_c)

            # Sample a token
            sampled_token_index = np.argmax(output_tokens[0, -1, :])
            # Handle unknown tokens
            sampled_token = self.reverse_target_word_index.get(sampled_token_index, '<UNK>')

            # Only add the token if it's not <UNK> and not 'end'
            if sampled_token != '<UNK>' and sampled_token != 'end':
                decoded_sentence += ' ' + sampled_token

            # Exit condition: either hit max length or find stop word.
            if sampled_token == 'end' or len(decoded_sentence.split()) >= (self.MAX_LEN_SUMMARY - 1):
                stop_condition = True

            # Update the target sequence (of length 1).
            target_seq = np.zeros((1, 1))
            target_seq[0, 0] = sampled_token_index

            # Update internal states
            e_h, e_c = h, c

        return decoded_sentence.strip()
