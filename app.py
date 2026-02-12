"""
Faithful AI - Web Interface
Access Qwerty from any web browser
"""

from flask import Flask, render_template, request, jsonify
from faithful_ai import ai
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message', '')
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = ai.chat(message)
    return jsonify({'response': response})

@app.route('/identity')
def identity():
    return jsonify({'identity': ai.get_identity()})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'Faithful AI'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
