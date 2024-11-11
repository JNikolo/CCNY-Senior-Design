from flask import Flask, request, jsonify

from services.summarizer import TextSummarizer

app = Flask(__name__)

model = TextSummarizer()


@app.route('/status')
def status():
    if model.model is None:
        return jsonify({'status': 'error', 'message': 'Model not loaded'})
    else:
        return jsonify({'status': 'ok'})
    
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data['text']
    summary = model.summarize(text)
    return jsonify({'summary': summary})

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    reference_summary = data['reference_summary']
    text = data['text']
    metrics = data.get('metrics', ['rouge1', 'rougeL'])
    summary = model.summarize(text)
    scores = model.evaluate(reference_summary, summary, metrics)

    result = {
        'reference_summary': reference_summary,
        'summary': summary,
        'scores': scores
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
