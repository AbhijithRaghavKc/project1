from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)

def translate_text(text, destination_language='es'):
    translator = Translator()
    translated_text = translator.translate(text, dest=destination_language)
    return translated_text.text

@app.route("/translate")
def translate():
    text = request.args.get('text', 'Hello')  # Get 'text' parameter from query string
    destination_language = request.args.get('destination_language', 'es')  # Get 'destination_language' parameter from query string
    translated = translate_text(text, destination_language)
    return render_template('translate.html', translated=translated)

if __name__ == '__main__':
    app.run(debug=True)
