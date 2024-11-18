import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, LSTM, Embedding, Dense, Concatenate, TimeDistributed, Bidirectional
from tensorflow.keras.optimizers import AdamW
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
import pickle
from .attention import ScaledDotProductAttention

class TextSummarizer:
    def __init__(self, max_text_len=150, max_summary_len=10, latent_dim=300, embedding_dim=100):
        self.max_text_len = max_text_len
        self.max_summary_len = max_summary_len
        self.latent_dim = latent_dim
        self.embedding_dim = embedding_dim
        self.x_tokenizer = None
        self.y_tokenizer = None
        self.model = None
        self.encoder_model = None
        self.decoder_model = None

    def load_tokenizers(self, x_tokenizer_path, y_tokenizer_path):
        """Load pre-trained tokenizers"""
        with open(x_tokenizer_path, 'rb') as handle:
            self.x_tokenizer = pickle.load(handle)
        with open(y_tokenizer_path, 'rb') as handle:
            self.y_tokenizer = pickle.load(handle)
        
        self.x_voc_size = len(self.x_tokenizer.word_index) + 1
        self.y_voc_size = len(self.y_tokenizer.word_index) + 1

    def build_model(self):
        """Build the model architecture"""
        # Encoder
        encoder_inputs = Input(shape=(self.max_text_len,))
        enc_emb = Embedding(self.x_voc_size, self.embedding_dim, trainable=True)(encoder_inputs)
        
        # Bidirectional LSTM layers
        encoder_lstm1 = Bidirectional(LSTM(self.latent_dim, return_sequences=True, return_state=True, 
                                         dropout=0.4, recurrent_dropout=0.4))
        encoder_output1, forward_h1, forward_c1, backward_h1, backward_c1 = encoder_lstm1(enc_emb)
        state_h1 = Concatenate()([forward_h1, backward_h1])
        state_c1 = Concatenate()([forward_c1, backward_c1])

        encoder_lstm2 = Bidirectional(LSTM(self.latent_dim, return_sequences=True, return_state=True, 
                                         dropout=0.4, recurrent_dropout=0.4))
        encoder_output2, forward_h2, forward_c2, backward_h2, backward_c2 = encoder_lstm2(encoder_output1)
        state_h2 = Concatenate()([forward_h2, backward_h2])
        state_c2 = Concatenate()([forward_c2, backward_c2])

        encoder_lstm3 = Bidirectional(LSTM(self.latent_dim, return_sequences=True, return_state=True, 
                                         dropout=0.4, recurrent_dropout=0.4))
        encoder_outputs, forward_h3, forward_c3, backward_h3, backward_c3 = encoder_lstm3(encoder_output2)
        state_h = Concatenate()([forward_h3, backward_h3])
        state_c = Concatenate()([forward_c3, backward_c3])

        # Decoder
        decoder_inputs = Input(shape=(None,))
        dec_emb_layer = Embedding(self.y_voc_size, self.embedding_dim, trainable=True)
        dec_emb = dec_emb_layer(decoder_inputs)

        decoder_lstm = LSTM(self.latent_dim * 2, return_sequences=True, return_state=True, 
                          dropout=0.4, recurrent_dropout=0.2)
        decoder_outputs, _, _ = decoder_lstm(dec_emb, initial_state=[state_h, state_c])

        # Attention
        attn_layer = ScaledDotProductAttention(name='attention_layer')
        attn_out, _ = attn_layer([encoder_outputs, decoder_outputs])
        decoder_concat_input = Concatenate(axis=-1, name='concat_layer')([decoder_outputs, attn_out])

        # Output
        decoder_dense = TimeDistributed(Dense(self.y_voc_size, activation='softmax'))
        decoder_outputs = decoder_dense(decoder_concat_input)

        self.model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
        self.model.compile(optimizer=AdamW(5e-4), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    def train(self, x_tr, y_tr, x_val, y_val, epochs=50, batch_size=512):
        """Train the model"""
        callbacks = [
            EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True, verbose=1),
            ReduceLROnPlateau(monitor='val_loss', factor=0.1, min_lr=1e-6, patience=2, verbose=1)
        ]

        history = self.model.fit(
            [x_tr, y_tr[:, :-1]], y_tr[:, 1:],
            epochs=epochs,
            callbacks=callbacks,
            batch_size=batch_size,
            validation_data=([x_val, y_val[:, :-1]], y_val[:, 1:])
        )
        return history
    
    def save_model(self, model_path):
        """Save the trained model"""
        self.model.save(model_path)

    def load_model(self, model_path):
        """Load a pre-trained model"""
        self.model = load_model(model_path, custom_objects={'ScaledDotProductAttention': ScaledDotProductAttention})
        self._build_inference_models()

    def _build_inference_models(self):
        """Build separate encoder and decoder models for inference"""
        # Encoder model
        encoder_inputs = self.model.input[0]
        encoder_bidirectional_layer = self.model.get_layer('bidirectional_2')
        encoder_outputs, forward_h3, forward_c3, backward_h3, backward_c3 = encoder_bidirectional_layer.output
        encoder_state_h = Concatenate()([forward_h3, backward_h3])
        encoder_state_c = Concatenate()([forward_c3, backward_c3])
        self.encoder_model = Model(inputs=encoder_inputs, 
                                 outputs=[encoder_outputs, encoder_state_h, encoder_state_c])

        # Decoder model
        decoder_inputs = Input(shape=(None,))
        decoder_state_input_h = Input(shape=(self.latent_dim * 2,))
        decoder_state_input_c = Input(shape=(self.latent_dim * 2,))
        encoder_output_input = Input(shape=(self.max_text_len, self.latent_dim * 2))

        dec_emb = self.model.get_layer("embedding_1")(decoder_inputs)
        decoder_lstm = self.model.get_layer("lstm_3")
        decoder_outputs, state_h, state_c = decoder_lstm(
            dec_emb, initial_state=[decoder_state_input_h, decoder_state_input_c]
        )

        attn_layer = self.model.get_layer('attention_layer')
        attn_out, _ = attn_layer([encoder_output_input, decoder_outputs])
        decoder_concat_input = Concatenate(axis=-1)([decoder_outputs, attn_out])
        decoder_dense = self.model.get_layer("time_distributed")
        decoder_outputs = decoder_dense(decoder_concat_input)

        self.decoder_model = Model(
            inputs=[decoder_inputs, encoder_output_input, decoder_state_input_h, decoder_state_input_c],
            outputs=[decoder_outputs, state_h, state_c]
        )

    def summarize(self, text):
        """Generate summary for input text"""
        # Preprocess input text
        sequences = self.x_tokenizer.texts_to_sequences([text])
        padded_sequences = pad_sequences(sequences, maxlen=self.max_text_len, padding='post')

        # Generate summary
        e_out, e_h, e_c = self.encoder_model.predict(padded_sequences, verbose=0)
        
        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = self.y_tokenizer.word_index['start']
        
        decoded_summary = []
        while True:
            output_tokens, h, c = self.decoder_model.predict(
                [target_seq] + [e_out, e_h, e_c], verbose=0
            )
            
            sampled_token_index = np.argmax(output_tokens[0, -1, :])
            sampled_token = self.y_tokenizer.index_word.get(sampled_token_index, '<UNK>')
            
            if sampled_token == 'end' or len(decoded_summary) >= self.max_summary_len - 1:
                break
                
            if sampled_token != '<UNK>':
                decoded_summary.append(sampled_token)
            
            target_seq = np.zeros((1, 1))
            target_seq[0, 0] = sampled_token_index
            e_h, e_c = h, c
            
        return ' '.join(decoded_summary)