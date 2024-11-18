import re
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from sklearn.model_selection import train_test_split

class TextPreprocessor:
    """Handles all text preprocessing tasks"""
    
    def __init__(self):
        self.contraction_mapping = {
            "ain't": "is not", "aren't": "are not", "can't": "cannot", 
            "'cause": "because", "could've": "could have", "couldn't": "could not",
            "didn't": "did not", "doesn't": "does not", "don't": "do not",
            "hadn't": "had not", "hasn't": "has not", "haven't": "have not",
            "he'd": "he would", "he'll": "he will", "he's": "he is",
            "how'd": "how did", "how'll": "how will", "how's": "how is",
            "i'd": "i would", "i'll": "i will", "i'm": "i am", "i've": "i have",
            "isn't": "is not", "it'd": "it would", "it'll": "it will",
            "it's": "it is", "let's": "let us", "ma'am": "madam",
            "might've": "might have", "mightn't": "might not",
            "must've": "must have", "mustn't": "must not",
            "needn't": "need not", "she'd": "she would",
            "she'll": "she will", "she's": "she is",
            "should've": "should have", "shouldn't": "should not",
            "that's": "that is", "there'd": "there would",
            "there's": "there is", "they'd": "they would",
            "they'll": "they will", "they're": "they are",
            "they've": "they have", "wasn't": "was not",
            "we'd": "we would", "we'll": "we will", "we're": "we are",
            "weren't": "were not", "what'll": "what will",
            "what're": "what are", "what's": "what is",
            "what've": "what have", "where'd": "where did",
            "where's": "where is", "who'll": "who will",
            "who's": "who is", "won't": "will not",
            "wouldn't": "would not", "you'd": "you would",
            "you'll": "you will", "you're": "you are"
        }
        
        # Download required NLTK data
        nltk.download('stopwords')
        
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        """Clean and preprocess review text"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove HTML tags
        text = BeautifulSoup(text, "lxml").text
        
        # Remove parentheses and their contents
        text = re.sub(r'\([^)]*\)', '', text)
        
        # Remove quotes
        text = re.sub('"', '', text)
        
        # Handle contractions
        text = ' '.join([self.contraction_mapping.get(t, t) for t in text.split()])
        
        # Remove possessive 's
        text = re.sub(r"'s\b", "", text)
        
        # Remove non-alphabetic characters
        text = re.sub("[^a-zA-Z]", " ", text)
        
        # Remove stopwords and short words
        tokens = [w for w in text.split() if w not in self.stop_words]
        tokens = [w for w in tokens if len(w) >= 3]
        
        return " ".join(tokens).strip()

    def clean_summary(self, text):
        """Clean and preprocess summary text"""
        # Remove quotes
        text = re.sub('"', '', text)
        
        # Handle contractions
        text = ' '.join([self.contraction_mapping.get(t, t) for t in text.split()])
        
        # Remove possessive 's
        text = re.sub(r"'s\b", "", text)
        
        # Remove non-alphabetic characters
        text = re.sub("[^a-zA-Z]", " ", text)
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove short words
        tokens = [t for t in text.split() if len(t) > 1]
        
        return " ".join(tokens).strip()

    def prepare_data(self, data_path, fields, test_size, random_state, shuffle):
        """Prepare data for training"""
        # Read data
        data = pd.read_csv(data_path)

        # Select required fields
        data = data[fields]

        textField = fields[0]
        summaryField = fields[1]
    
        # Clean data
        data.drop_duplicates(subset=[textField], inplace=True)
        data.dropna(axis=0, inplace=True)
        
        # Clean text and summaries
        data['cleaned_text'] = data[textField].apply(self.clean_text)
        data['cleaned_summary'] = data[summaryField].apply(self.clean_summary)
        
        # Add start and end tokens to summaries
        data['cleaned_summary'] = data['cleaned_summary'].apply(lambda x: '_START_ ' + x + ' _END_')
        
        # Split data
        x_tr, x_val, y_tr, y_val = train_test_split(
            data['cleaned_text'], 
            data['cleaned_summary'],
            test_size=test_size,
            random_state=random_state,
            shuffle=shuffle
        )
        
        return x_tr, x_val, y_tr, y_val
