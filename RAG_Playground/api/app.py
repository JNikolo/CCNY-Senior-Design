from flask import Flask, request, jsonify
from functools import wraps
from datetime import datetime, timezone
import jwt
import re
from typing import Tuple, Dict, Any, List, Optional

from services.summarizer import TextSummarizer
from services.geminiSummarizer import GeminiSummarizer

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '/api/v1'
app.config['API_KEYS'] = {'valid-api-key'}    # In production, use secure storage
app.config['JSON_SORT_KEYS'] = False

model = TextSummarizer()
geminiModel = GeminiSummarizer()

# Custom Exceptions
class APIError(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

# Error Handler
@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify({'error': error.message})
    response.status_code = error.status_code
    return response

@app.errorhandler(Exception)
def handle_generic_error(error):
    response = jsonify({'error': 'An unexpected error occurred'})
    response.status_code = 500
    return response

# Authentication Decorators
def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if not api_key or api_key not in app.config['API_KEYS']:
            raise APIError('Invalid or missing API key', 401)
        return f(*args, **kwargs)
    return decorated


# Input Validation Functions
def validate_text(data: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """Validate text input for summarization."""
    if not data or not isinstance(data, dict):
        return False, "Invalid request format"
    
    if 'text' not in data:
        return False, "Missing 'text' field"
        
    if not isinstance(data['text'], str):
        return False, "'text' field must be a string"
        
    if not data['text'].strip():
        return False, "'text' field cannot be empty"
        
    if len(data['text']) > 10000:  # Example limit
        return False, "Text exceeds maximum length of 10000 characters"
    
    if 'reference_summary' in data and not isinstance(data['reference_summary'], str):
        return False, "'reference_summary' must be a string"
    
    if 'metrics' in data and not isinstance(data['metrics'], list):
        return False, "'metrics' must be a list"
    
    if data.get('metrics') and not all(isinstance(m, str) for m in data['metrics']):
        return False, "All metrics must be strings"
    
    for key in data:
        if key not in ['text', 'reference_summary', 'metrics']:
            return False, f"Invalid field: {key}"
        
    return True, None

def validate_evaluation_input(data: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """Validate evaluation input data."""
    if not data or not isinstance(data, dict):
        return False, "Invalid request format"
        
    required_fields = ['reference_summary', 'text']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
        
    if not all(isinstance(data[field], str) for field in required_fields):
        return False, "All text fields must be strings"
        
    if 'metrics' in data:
        if not isinstance(data['metrics'], list):
            return False, "'metrics' must be a list"
        valid_metrics = {'rouge1', 'rougeL'}
        invalid_metrics = [m for m in data['metrics'] if m not in valid_metrics]
        if invalid_metrics:
            return False, f"Invalid metrics: {', '.join(invalid_metrics)}"
            
    return True, None

# Enhanced API Routes
@app.route('/status')
@require_api_key
def status():
    """Check model status with enhanced error handling."""
    try:
        if model.model is None:
            raise APIError('Model not loaded', 503)
            
        return jsonify({
            'status': 'ok',
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'model_info': {
                'name': model.__class__.__name__,
                'is_ready': model.model is not None
            },
            'last_train_time': model.LAST_TRAINED_DATE,
            'accuracy': model.ACCURACY,
            'loss': model.LOSS
        })
    except Exception as e:
        app.logger.error(f"Status check failed: {str(e)}")
        raise APIError('Error checking model status', 500)

@app.route('/summarize', methods=['POST'])
@require_api_key
def summarize():
    """Generate summary with enhanced validation and error handling."""
    try:
        data = request.get_json()
        is_valid, error = validate_text(data)
        if not is_valid:
            raise APIError(error, 400)
            
        summary = model.summarize(data['text'])
        
        return jsonify({
            'summary': summary,
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'char_count': len(summary)
        })
    except APIError:
        raise
    except Exception as e:
        app.logger.error(f"Summarization failed: {str(e)}")
        raise APIError('Error generating summary', 500)

@app.route('/evaluate', methods=['POST'])
@require_api_key
def evaluate():
    """Evaluate summaries with enhanced validation and error handling."""
    try:
        data = request.get_json()
        is_valid, error = validate_evaluation_input(data)
        if not is_valid:
            raise APIError(error, 400)
            
        reference_summary = data['reference_summary']
        text = data['text']
        metrics = data.get('metrics', ['rouge1', 'rougeL'])
        
        summary = model.summarize(text)
        scores = model.evaluate(reference_summary, summary, metrics)
        
        result = {
            'reference_summary': reference_summary,
            'summary': summary,
            'scores': scores,
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
        return jsonify(result)
    except APIError:
        raise
    except Exception as e:
        app.logger.error(f"Evaluation failed: {str(e)}")
        raise APIError('Error evaluating summary', 500)

@app.route('/llm_summarize', methods=['POST'])
@require_api_key
def generate_summary():
    """Generate LLM summary with enhanced validation and error handling."""
    try:
        data = request.get_json()
        is_valid, error = validate_text(data)
        if not is_valid:
            raise APIError(error, 400)
            
        summary = geminiModel.generate_summary(data['text'])
        
        return jsonify({
            'summary': summary,
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'char_count': len(summary)
        })
    except APIError:
        raise
    except Exception as e:
        app.logger.error(f"LLM summarization failed: {str(e)}")
        raise APIError('Error generating LLM summary', 500)

@app.route('/dual_summarize', methods=['POST'])
@require_api_key
def dual_summarize():
    """Generate dual summaries with enhanced validation and error handling."""
    try:
        data = request.get_json()
        is_valid, error = validate_text(data)
        if not is_valid:
            raise APIError(error, 400)
            
        text = data['text']
        text_summary = model.summarize(text)
        gemini_summary = geminiModel.generate_summary(text)
        
        return jsonify({
            'text_summary': text_summary,
            'gemini_summary': gemini_summary,
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'char_counts': {
            'text_summary': len(text_summary),
            'gemini_summary': len(gemini_summary)
            }
        })
    except APIError:
        raise
    except Exception as e:
        app.logger.error(f"Dual summarization failed: {str(e)}")
        raise APIError('Error generating dual summaries', 500)

@app.route('/dual_evaluate', methods=['POST'])
@require_api_key
def dual_evaluate():
    """Evaluate dual summaries with enhanced validation and error handling."""
    try:
        data = request.get_json()
        is_valid, error = validate_evaluation_input(data)
        if not is_valid:
            raise APIError(error, 400)
            
        reference_summary = data['reference_summary']
        text = data['text']
        metrics = data.get('metrics', ['rouge1', 'rougeL'])
        
        text_summary = model.summarize(text)
        gemini_summary = geminiModel.generate_summary(text)
        
        text_scores = model.evaluate(reference_summary, text_summary, metrics)
        gemini_scores = geminiModel.evaluate(reference_summary, gemini_summary, metrics)
        
        result = {
            'reference_summary': reference_summary,
            'text_summary': text_summary,
            'gemini_summary': gemini_summary,
            'text_scores': text_scores,
            'gemini_scores': gemini_scores,
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
        return jsonify(result)
    except APIError:
        raise
    except Exception as e:
        app.logger.error(f"Dual evaluation failed: {str(e)}")
        raise APIError('Error evaluating dual summaries', 500)

if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)