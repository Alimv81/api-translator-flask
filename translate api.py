from flask import Flask, jsonify, request, send_from_directory
from translate import Translator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    if 'text' not in data or 'dest_lang' not in data:
        return jsonify({"error": "Please provide 'text' and 'dest_lang' fields."}), 400
    
    text = data['text']
    dest_lang = data['dest_lang']
    
    translator = Translator(dest_lang)
    translation = translator.translate(text)

    response = {
        'original_text': text,
        'translated_text': translation,  
        'dest_lang': dest_lang
    }
    return jsonify(response)

@app.route('/translate', methods=['GET'])
def serve_main_html():
    return send_from_directory('.', 'main.html')

@app.route('/translate_version', methods=['GET'])
def get_version():
    version = Translator.__version__
    return jsonify({'version': version})

if __name__ == '__main__':
    app.run(debug=True)