# 🌐 Polyglot Voice

**Polyglot Voice** is a web-based multilingual translation tool built with Flask that allows users to:
- Translate text into 60+ languages
- Listen to the translated text via speech synthesis
- Download the translated speech as an MP3

This project leverages `mtranslate` for translation, `gTTS` for text-to-speech, and offers a smooth and responsive UI with Bootstrap 5.

---

## 🚀 Features

- 📝 Translate user-input text into any supported language
- 🌍 Language selection from a dynamic dropdown using a CSV list
- 🔊 Text-to-speech support in multiple languages
- 🎧 Audio playback in-browser
- ⬇️ Download option for MP3 of translated audio
- 💡 Clean and responsive frontend using Bootstrap

---


---

## 🛠️ Tech Stack

| Component         | Tech Used        |
|------------------|------------------|
| Backend          | Flask            |
| Translation API  | `mtranslate`     |
| Speech Synthesis | `gTTS`           |
| Frontend         | HTML5 + Bootstrap 5 |
| Audio Handling   | HTML `<audio>`   |
| Data Format      | CSV              |

---

## 📦 Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/polyglot-voice.git
cd polyglot-voice
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the Flask app
```
python app.py
```

---
## ThankYou
---
