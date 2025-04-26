from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()
        text = data.get('text')
        source_lang = data.get('source', 'auto')
        target_lang = data.get('target', 'ru')

        if not text:
            return jsonify({'error': 'Text is required'}), 400

        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return jsonify({'translated_text': translated}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)