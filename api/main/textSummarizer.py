from ..preprocessor.TextPreprocessor import TextPreprocessor
from ..utils.tokenManager import TokenizerManager
from ..models.seq2seq import TextSummarizer
from ..utils.evaluator import ModelEvaluator

class SummarizerPipeline:
    """Main pipeline for text summarization"""
    
    def __init__(self, max_text_len=150, max_summary_len=10):
        """Initialize the pipeline"""
        self.max_text_len = max_text_len
        self.max_summary_len = max_summary_len
        self.preprocessor = TextPreprocessor()
        self.tokenizer_manager = TokenizerManager(max_text_len, max_summary_len)
        self.model = TextSummarizer(max_text_len, max_summary_len)
        self.evaluator = ModelEvaluator(self.tokenizer_manager)
        
    def prepare_data(self, data_path, fields=["Text", "Summary"], **kwargs):
        """Prepare data for training"""

        test_size = kwargs.get('test_size', 0.2)
        random_state = kwargs.get('random_state', 0)
        shuffle = kwargs.get('shuffle', True)

        # Preprocess data
        x_tr, x_val, y_tr, y_val = self.preprocessor.prepare_data(
            data_path,
            fields,
            test_size,
            random_state,
            shuffle
        )
        
        # Fit and prepare sequences
        self.tokenizer_manager.fit_tokenizers(x_tr, y_tr)
        return self.tokenizer_manager.prepare_sequences(x_tr, x_val, y_tr, y_val)
    
    def train(self, x_tr, y_tr, x_val, y_val, epochs=50, batch_size=64):
        """Train the model"""
        # Build and train model
        self.model.build_model()
        history = self.model.train(x_tr, y_tr, x_val, y_val, epochs, batch_size)
        
        # Plot training history
        self.evaluator.plot_training_history(history)
        return history 
    
    def evaluate(self, x_val, y_val, sample_size=5000):
        """Evaluate model performance"""
        return self.evaluator.evaluate_model(self.model, x_val, y_val, sample_size)
    
    def save_model(self, model_path, x_tokenizer_path, y_tokenizer_path):
        """Save model and tokenizers"""
        self.model.save_model(model_path)
        self.tokenizer_manager.save_tokenizers(x_tokenizer_path, y_tokenizer_path)
    
    def load_model(self, model_path, x_tokenizer_path, y_tokenizer_path):
        """Load model and tokenizers"""
        self.model.load_model(model_path)
        self.tokenizer_manager.load_tokenizers(x_tokenizer_path, y_tokenizer_path)
    
    def summarize(self, text):
        """Generate summary for input text"""
        # Preprocess text
        cleaned_text = self.preprocessor.clean_text(text)
        return self.model.summarize(cleaned_text)
    