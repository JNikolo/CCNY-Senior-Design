from rouge_score import rouge_scorer
import numpy as np
import matplotlib.pyplot as plt

class ModelEvaluator:
    """Handles model evaluation and performance metrics"""
    
    def __init__(self, tokenizer_manager):
        self.tokenizer_manager = tokenizer_manager
        self.scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    
    def calculate_rouge(self, references, hypotheses):
        """Calculate ROUGE scores"""
        scores = {
            'rouge1': [], 
            'rouge2': [], 
            'rougeL': []
        }
        
        for ref, hyp in zip(references, hypotheses):
            score = self.scorer.score(ref, hyp)
            scores['rouge1'].append(score['rouge1'].fmeasure)
            scores['rouge2'].append(score['rouge2'].fmeasure)
            scores['rougeL'].append(score['rougeL'].fmeasure)
        
        return {
            'rouge1': np.mean(scores['rouge1']),
            'rouge2': np.mean(scores['rouge2']),
            'rougeL': np.mean(scores['rougeL'])
        }
    
    def evaluate_model(self, model, x_val, y_val, sample_size=5000):
        """Evaluate model performance"""
        # Take a sample for evaluation
        x_val_sample = x_val[:sample_size]
        y_val_sample = y_val[:sample_size]
        
        # Generate predictions
        predictions = []
        for i in range(sample_size):
            pred = model.summarize(x_val_sample[i])
            predictions.append(pred)
        
        # Calculate ROUGE scores
        original_summaries = [self.seq2summary(summary) for summary in y_val_sample]
        rouge_scores = self.calculate_rouge(original_summaries, predictions)
        
        return rouge_scores
    
    def plot_training_history(self, history):
        """Plot training history"""
        # Plot loss
        plt.figure(figsize=(12, 4))
        
        plt.subplot(1, 2, 1)
        plt.plot(history.history['loss'], label='Train Loss')
        plt.plot(history.history['val_loss'], label='Validation Loss')
        plt.legend()
        plt.title('Model Loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        
        plt.subplot(1, 2, 2)
        plt.plot(history.history['accuracy'], label='Train Accuracy')
        plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
        plt.legend()
        plt.title('Model Accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        
        plt.tight_layout()
        plt.show()
    
    def seq2summary(self, input_seq):
        """Convert sequence to summary"""
        word_idx = self.tokenizer_manager.y_tokenizer.word_index
        idx_word = {v: k for k, v in word_idx.items()}
        
        return ' '.join([idx_word.get(i, '') for i in input_seq 
                        if i != 0 and i != word_idx.get('start') 
                        and i != word_idx.get('end')]).strip()
    
    def seq2text(self, input_seq):
        """Convert sequence to text"""
        word_idx = self.tokenizer_manager.x_tokenizer.word_index
        idx_word = {v: k for k, v in word_idx.items()}
        
        return ' '.join([idx_word.get(i, '') for i in input_seq if i != 0]).strip()