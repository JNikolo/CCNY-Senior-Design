from main.textSummarizer import SummarizerPipeline

# 1. Initialize the Summarizer
summarizer = SummarizerPipeline(
    max_text_len=150,  # Maximum length of input text
    max_summary_len=10  # Maximum length of generated summary
    # You can also specify other parameters here
    # latent_dim, embedding_dim
)

# 2. Train a new model
# Prepare the data
x_tr, x_val, y_tr, y_val = summarizer.prepare_data(
                                                    "Reviews.csv", 
                                                    fields=["Text", "Summary"]
                                                    # You can also specify other parameters here
                                                    # test_size, random_state, shuffle using kwargs
                                                )

# Train the model
history = summarizer.train(
    x_tr=x_tr,
    y_tr=y_tr,
    x_val=x_val,
    y_val=y_val,
    epochs=5,
    batch_size=64
)

# Save the trained model
# This will save the model and tokenizers to files
# Model path should end with .keras and tokenizer paths should end with .pickle
summarizer.save_model(
    model_path='my_summarizer.keras',
    x_tokenizer_path='my_x_tokenizer.pickle',
    y_tokenizer_path='my_y_tokenizer.pickle'
)

# 3. Load a pre-trained model (if you want to use existing model instead of training)
summarizer.load_model(
    model_path='my_summarizer.keras',
    x_tokenizer_path='my_x_tokenizer.pickle',
    y_tokenizer_path='my_y_tokenizer.pickle'
)

# 4. Generate a summary for a single text
sample_text = """
This product is amazing! I bought it last month and have been using it daily. 
The quality is excellent and it's very durable. The customer service team was 
also very helpful when I had questions about some features. The battery life 
is incredible - lasts much longer than advertised. Would definitely recommend 
to anyone looking for a reliable product.
"""

summary = summarizer.summarize(sample_text)
print("Generated Summary:", summary)

# 5. Evaluate model performance
rouge_scores = summarizer.evaluate(x_val, y_val, sample_size=100)
print("\nROUGE Scores:")
print(f"ROUGE-1: {rouge_scores['rouge1']:.4f}")
print(f"ROUGE-2: {rouge_scores['rouge2']:.4f}")
print(f"ROUGE-L: {rouge_scores['rougeL']:.4f}")

# 6. Process multiple texts
texts = [
    "The movie was excellent. Great acting and beautiful cinematography. The plot kept me engaged throughout.",
    "The restaurant's service was terrible. Food was cold and took forever to arrive. Would not recommend.",
    "This book is a masterpiece. Beautifully written with complex characters. Couldn't put it down."
]

summaries = [summarizer.summarize(text) for text in texts]
for i, (text, summary) in enumerate(zip(texts, summaries), 1):
    print(f"\nText {i}:", text)
    print(f"Summary {i}:", summary)

# Alternative usage patterns:

# Quick load and use (when you just want to use a pre-trained model)
quick_summarizer = SummarizerPipeline()
quick_summarizer.load_model(
    model_path='my_summarizer.keras',
    x_tokenizer_path='my_x_tokenizer.pickle',
    y_tokenizer_path='my_y_tokenizer.pickle'
)
quick_summary = quick_summarizer.summarize("Your text here...")

# Custom training parameters
custom_summarizer = SummarizerPipeline(max_text_len=200, max_summary_len=15)
x_tr, x_val, y_tr, y_val = custom_summarizer.prepare_data("data.csv")
history = custom_summarizer.train(
    x_tr, y_tr, x_val, y_val,
    epochs=10,
    batch_size=256
)

# Evaluate existing model with new data
eval_summarizer = SummarizerPipeline()
eval_summarizer.load_model(
    model_path='my_summarizer.keras',
    x_tokenizer_path='my_x_tokenizer.pickle',
    y_tokenizer_path='my_y_tokenizer.pickle'
)
_, x_val, _, y_val = eval_summarizer.prepare_data("new_data.csv")
scores = eval_summarizer.evaluate(x_val, y_val, sample_size=500)