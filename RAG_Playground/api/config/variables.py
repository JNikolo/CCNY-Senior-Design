import os
from dotenv import load_dotenv
load_dotenv()

MODEL_PATH = os.getenv('MODEL_PATH')
X_TOKENIZER_PATH = os.getenv('X_TOKENIZER_PATH')
Y_TOKENIZER_PATH = os.getenv('Y_TOKENIZER_PATH')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')