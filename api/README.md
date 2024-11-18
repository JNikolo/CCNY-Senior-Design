# Text Summarization API Documentation

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Core Components](#core-components)
- [Quick Start](#quick-start)
- [Detailed Usage Guide](#detailed-usage-guide)
- [API Reference](#api-reference)
- [Parameters Guide](#parameters-guide)
- [Data Format](#data-format)
- [Output Formats](#output-formats)
- [Error Handling](#error-handling)
- [Best Practices](#best-practices)
- [Examples](#examples)

## Overview

The Text Summarization API provides a comprehensive solution for training and using text summarization models. It uses a sequence-to-sequence architecture with attention mechanism to generate abstractive summaries from input texts.

### Key Features

- Abstractive text summarization
- Pre-trained model support
- Custom model training
- Batch processing capability
- ROUGE score evaluation
- Flexible text preprocessing
- Built-in tokenization management

## Installation

# Required Dependencies

- Python >= 3.7
- tensorflow >= 2.0.0
- nltk >= 3.6.0
- pandas >= 1.2.0
- numpy >= 1.19.0
- rouge-score >= 0.0.4
- beautifulsoup4 >= 4.9.0
- lxml >= 4.9.0

These can be installed all at once by saving them to a `requirements.txt` file and running:

```bash
pip install -r requirements.txt
```

## Core Components

The API consists of four main classes:

1. `SummarizerPipeline`: Main interface for the API
2. `TextPreprocessor`: Handles text cleaning and preprocessing
3. `TokenizerManager`: Manages text tokenization
4. `ModelEvaluator`: Handles model evaluation and metrics

## Quick Start

### Basic Usage

```python
from text_summarizer import SummarizerPipeline

# Initialize
summarizer = SummarizerPipeline()

# Load pre-trained model
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

### Training New Model

```python
# Initialize with custom parameters
summarizer = SummarizerPipeline(
    max_text_len=150,
    max_summary_len=10
)

# Prepare data and train
x_tr, x_val, y_tr, y_val = summarizer.prepare_data("data.csv")
history = summarizer.train(x_tr, y_tr, x_val, y_val)

# Save model
summarizer.save_model(
    model_path='my_model.keras',
    x_tokenizer_path='x_tok.pickle',
    y_tokenizer_path='y_tok.pickle'
)
```

## Detailed Usage Guide

### 1. SummarizerPipeline Class

The main interface for all summarization operations.

#### Initialization

```python
summarizer = SummarizerPipeline(
    max_text_len=150,        # Maximum length of input text
    max_summary_len=10,      # Maximum length of summary
    latent_dim=300,          # Size of LSTM hidden states
    embedding_dim=100        # Size of word embeddings
)
```

#### Core Methods

##### prepare_data()

Prepares dataset for training.

```python
x_tr, x_val, y_tr, y_val = summarizer.prepare_data(
    data_path="data.csv",    # Path to dataset
    test_size=0.2           # Validation split ratio
)
```

**Parameters:**

- `data_path` (str): Path to CSV file containing text data
- `test_size` (float): Proportion of data to use for validation (0.0 to 1.0)

**Returns:**

- Tuple of (x_train, x_val, y_train, y_val) arrays

##### train()

Trains the summarization model.

```python
history = summarizer.train(
    x_tr,                   # Training texts
    y_tr,                   # Training summaries
    x_val,                  # Validation texts
    y_val,                  # Validation summaries
    epochs=50,             # Number of training epochs
    batch_size=512         # Batch size
)
```

**Parameters:**

- `x_tr`, `y_tr`, `x_val`, `y_val`: Training and validation data
- `epochs` (int): Number of training epochs
- `batch_size` (int): Training batch size

**Returns:**

- Training history object containing loss and accuracy metrics

##### summarize()

Generates summary for input text.

```python
summary = summarizer.summarize(text)
```

**Parameters:**

- `text` (str): Input text to summarize

**Returns:**

- str: Generated summary

### 2. Data Format

#### Input Data Format

The training data CSV should contain at least two columns:

- 'Text': Original text
- 'Summary': Reference summary

Example:

```csv
Text,Summary
This is a long text...,This is the summary
Another long text...,Another summary
```

#### Model Input/Output Specifications

- Input text: String of any length (will be truncated to max_text_len)
- Output summary: String (limited to max_summary_len)

### 3. Parameters Guide

#### Model Parameters

| Parameter       | Type | Default | Description                         |
| --------------- | ---- | ------- | ----------------------------------- |
| max_text_len    | int  | 150     | Maximum length of input text        |
| max_summary_len | int  | 10      | Maximum length of generated summary |
| latent_dim      | int  | 300     | Dimension of LSTM hidden states     |
| embedding_dim   | int  | 100     | Dimension of word embeddings        |

#### Training Parameters

| Parameter  | Type  | Default | Description                 |
| ---------- | ----- | ------- | --------------------------- |
| epochs     | int   | 50      | Number of training epochs   |
| batch_size | int   | 64      | Training batch size         |
| test_size  | float | 0.2     | Validation data split ratio |

### 4. Output Formats

#### Summary Output

- Type: String
- Format: Clean text without special tokens
- Length: Limited by max_summary_len

#### Evaluation Metrics

```python
{
    'rouge1': float,  # ROUGE-1 F1 score
    'rouge2': float,  # ROUGE-2 F1 score
    'rougeL': float   # ROUGE-L F1 score
}
```

### 5. Error Handling

The API includes comprehensive error handling for common issues:

```python
try:
    summary = summarizer.summarize(text)
except ValueError as e:
    print(f"Invalid input: {e}")
except RuntimeError as e:
    print(f"Model error: {e}")
```

Common Errors:

- `ValueError`: Invalid input format or length
- `RuntimeError`: Model loading or prediction errors
- `FileNotFoundError`: Missing model or tokenizer files

### 6. Best Practices

1. Data Preparation

   - Clean and preprocess text data
   - Ensure balanced dataset
   - Remove duplicates and invalid entries

2. Model Training

   - Start with default parameters
   - Monitor validation loss
   - Use early stopping
   - Save best performing model

3. Production Use
   - Pre-load model
   - Batch process when possible
   - Implement proper error handling
   - Monitor performance metrics

### 7. Examples

#### Complete Training Pipeline

```python
# Initialize
summarizer = SummarizerPipeline(
    max_text_len=150,
    max_summary_len=10
)

# Prepare data
x_tr, x_val, y_tr, y_val = summarizer.prepare_data("data.csv")

# Train
history = summarizer.train(
    x_tr, y_tr, x_val, y_val,
    epochs=50,
    batch_size=512
)

# Save
summarizer.save_model(
    model_path='model.keras',
    x_tokenizer_path='x_tok.pickle',
    y_tokenizer_path='y_tok.pickle'
)

# Evaluate
scores = summarizer.evaluate(x_val, y_val)
print(f"ROUGE-1: {scores['rouge1']:.4f}")
```

#### Batch Processing

```python
texts = [
    "First text to summarize...",
    "Second text to summarize...",
    "Third text to summarize..."
]

summaries = [summarizer.summarize(text) for text in texts]
```
