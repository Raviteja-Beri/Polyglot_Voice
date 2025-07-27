from flask import Flask, render_template, request, send_from_directory
import pandas as pd
from mtranslate import translate
from gtts import gTTS
import os

app = Flask(__name__)

# Load language data
df = pd.read_csv("language.csv").dropna()
lang_array = dict(zip(df['name'], df['iso']))
languages = list(lang_array.keys())

@app.route('/', methods=['GET', 'POST'])
def index():
    output_text = ""
    selected_lang = ""
    audio_generated = False

    if request.method == 'POST':
        input_text = request.form['input_text']
        selected_lang = request.form['language']

        try:
            lang_code = lang_array[selected_lang]
            output_text = translate(input_text, lang_code)

            # Generate audio file
            audio_path = os.path.join('static', 'audio', 'lang.mp3')
            tts = gTTS(text=output_text, lang=lang_code)
            tts.save(audio_path)
            audio_generated = True
        except Exception as e:
            output_text = f"Error: {e}"

    return render_template(
        'index.html',
        languages=languages,
        translated_text=output_text,
        selected_lang=selected_lang,
        audio_generated=audio_generated
    )

@app.route('/download')
def download_audio():
    return send_from_directory('static/audio', 'lang.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
