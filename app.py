"""
Faithful AI - Web Interface
Access Qwerty from any web browser
"""

from flask import Flask, render_template, request, jsonify
from faithful_ai import ai
import os
from pathlib import Path

# Get the absolute path to the app directory
basedir = Path(__file__).parent.absolute()

# Create Flask app with explicit template folder
app = Flask(
    __name__,
    template_folder=str(basedir / 'templates'),
    static_folder=str(basedir / 'static')
)

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
