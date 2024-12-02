# Text Summarization API Documentation

## Overview

The Text Summarization API offers a powerful solution for training and deploying text summarization models. Built on a sequence-to-sequence architecture with attention mechanism, it excels at generating abstractive summaries from input texts.

### Key Features
- State-of-the-art abstractive text summarization
- Support for pre-trained models and custom training
- Efficient batch processing capabilities
- Built-in ROUGE score evaluation
- Advanced text preprocessing and tokenization
- Production-ready error handling

## Getting Started

### Prerequisites
The API requires Python 3.7 or higher and the following dependencies:

```bash
tensorflow >= 2.0.0
nltk >= 3.6.0
pandas >= 1.2.0
numpy >= 1.19.0
rouge-score >= 0.0.4
beautifulsoup4 >= 4.9.0
lxml >= 4.9.0
```

### Installation

Save the dependencies to `requirements.txt` and install:

```bash
pip install -r requirements.txt
```

### Quick Start Guide

Generate a summary using a pre-trained model:

```python
from text_summarizer import SummarizerPipeline

# Initialize and load pre-trained model
summarizer = SummarizerPipeline()
summarizer.load_model(
    model_path='model.keras',
    x_tokenizer_path='x_tokenizer.pickle',
    y_tokenizer_path='y_tokenizer.pickle'
)

# Generate summary
text = "Your text here..."
summary = summarizer.summarize(text)
print(summary)
```

## Core Components

### 1. SummarizerPipeline

The main interface that orchestrates all summarization operations.

#### Configuration Options

| Parameter       | Type | Default | Description                         |
|----------------|------|---------|-------------------------------------|
| max_text_len    | int  | 150     | Maximum input text length           |
| max_summary_len | int  | 10      | Maximum summary length              |
| latent_dim      | int  | 300     | LSTM hidden state dimension         |
| embedding_dim   | int  | 100     | Word embedding dimension            |

#### Key Methods

**prepare_data(data_path, test_size=0.2)**
```python
# Prepare dataset for training
x_tr, x_val, y_tr, y_val = summarizer.prepare_data(
    data_path="dataset.csv",
    test_size=0.2
)
```

**train(x_tr, y_tr, x_val, y_val, epochs=50, batch_size=512)**
```python
# Train the model
history = summarizer.train(
    x_tr, y_tr,
    x_val, y_val,
    epochs=50,
    batch_size=512
)
```

**summarize(text)**
```python
# Generate summary
summary = summarizer.summarize(text)
```

### 2. Data Specifications

#### Training Data Format
Required CSV structure:
```csv
Text,Summary
"Original text content...","Reference summary"
"Another text sample...","Another summary"
```

#### Model I/O
- Input: Raw text (automatically truncated to max_text_len)
- Output: Generated summary (constrained to max_summary_len)

## Advanced Usage

### Training Pipeline

```python
# Initialize with custom parameters
summarizer = SummarizerPipeline(
    max_text_len=150,
    max_summary_len=10,
    latent_dim=300,
    embedding_dim=100
)

# Prepare and train
x_tr, x_val, y_tr, y_val = summarizer.prepare_data("training_data.csv")
history = summarizer.train(x_tr, y_tr, x_val, y_val)

# Save trained model
summarizer.save_model(
    model_path='custom_model.keras',
    x_tokenizer_path='x_tokenizer.pickle',
    y_tokenizer_path='y_tokenizer.pickle'
)

# Evaluate performance
scores = summarizer.evaluate(x_val, y_val)
print(f"ROUGE-1: {scores['rouge1']:.4f}")
print(f"ROUGE-2: {scores['rouge2']:.4f}")
print(f"ROUGE-L: {scores['rougeL']:.4f}")
```

### Batch Processing

```python
texts = [
    "First document to summarize...",
    "Second document to summarize...",
    "Third document to summarize..."
]

# Process multiple texts efficiently
with summarizer.batch_mode():
    summaries = [summarizer.summarize(text) for text in texts]
```

## Best Practices

### Data Preparation
1. Clean and normalize text data
2. Remove duplicates and invalid entries
3. Ensure dataset balance and quality
4. Validate input/output length distributions

### Model Training
1. Start with default hyperparameters
2. Implement early stopping
3. Monitor validation metrics
4. Save checkpoints regularly
5. Use cross-validation for smaller datasets

### Production Deployment
1. Pre-load models at startup
2. Implement robust error handling
3. Use batch processing for multiple documents
4. Monitor system resources and performance
5. Implement proper logging and monitoring

## Error Handling

```python
try:
    summary = summarizer.summarize(text)
except ValueError as e:
    logger.error(f"Invalid input format: {e}")
except RuntimeError as e:
    logger.error(f"Model prediction failed: {e}")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
```

Common Error Types:
- `ValueError`: Invalid input format or length
- `RuntimeError`: Model prediction or loading issues
- `FileNotFoundError`: Missing model files
- `MemoryError`: Insufficient system resources

## Evaluation Metrics

The API provides comprehensive evaluation using ROUGE metrics:

```python
{
    'rouge1': 0.XXX,  # Precision, recall, F1 for unigrams
    'rouge2': 0.XXX,  # Precision, recall, F1 for bigrams
    'rougeL': 0.XXX   # Longest common subsequence based scoring
}
```

For questions or issues, please consult our documentation or open an issue in our repository.