from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

class TokenizerManager:
    """Handles tokenization of text and summaries"""
    
    def __init__(self, max_text_len, max_summary_len):
        self.max_text_len = max_text_len
        self.max_summary_len = max_summary_len
        self.x_tokenizer = Tokenizer()
        self.y_tokenizer = Tokenizer()
        
    def fit_tokenizers(self, x_tr, y_tr):
        """Fit tokenizers on training data"""
        self.x_tokenizer.fit_on_texts(list(x_tr))
        self.y_tokenizer.fit_on_texts(list(y_tr))
        
    def prepare_sequences(self, x_tr, x_val, y_tr, y_val):
        """Convert text to sequences and pad them"""
        # Convert texts to sequences
        x_tr_seq = self.x_tokenizer.texts_to_sequences(x_tr)
        x_val_seq = self.x_tokenizer.texts_to_sequences(x_val)
        y_tr_seq = self.y_tokenizer.texts_to_sequences(y_tr)
        y_val_seq = self.y_tokenizer.texts_to_sequences(y_val)
        
        # Pad sequences
        x_tr_pad = pad_sequences(x_tr_seq, maxlen=self.max_text_len, padding='post')
        x_val_pad = pad_sequences(x_val_seq, maxlen=self.max_text_len, padding='post')
        y_tr_pad = pad_sequences(y_tr_seq, maxlen=self.max_summary_len, padding='post')
        y_val_pad = pad_sequences(y_val_seq, maxlen=self.max_summary_len, padding='post')
        
        return x_tr_pad, x_val_pad, y_tr_pad, y_val_pad
    
    def save_tokenizers(self, x_tokenizer_path, y_tokenizer_path):
        """Save tokenizers to files"""
        with open(x_tokenizer_path, 'wb') as handle:
            pickle.dump(self.x_tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open(y_tokenizer_path, 'wb') as handle:
            pickle.dump(self.y_tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    def load_tokenizers(self, x_tokenizer_path, y_tokenizer_path):
        """Load tokenizers from files"""
        with open(x_tokenizer_path, 'rb') as handle:
            self.x_tokenizer = pickle.load(handle)
        with open(y_tokenizer_path, 'rb') as handle:
            self.y_tokenizer = pickle.load(handle)
