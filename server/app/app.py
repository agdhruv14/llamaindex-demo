from flask import Flask, jsonify, request
from flask_cors import CORS
from llama import parse
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = 'uploaded_file.pdf'
    filepath = os.path.join('./files', filename)
    file.save(filepath)
    return jsonify({'message': 'file'})


@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json().get('question')
    return parse('./files/uploaded_file.pdf', data)

    

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)