from flask import Flask, render_template, request
from gtts import gTTS
import os
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None
    if request.method == "POST":
        text = request.form["text"]
        if text.strip():
            tts = gTTS(text)
            filename = f"output_{int(time.time())}.mp3"
            filepath = os.path.join("static", filename)
            tts.save(filepath)
            audio_file = filename
    return render_template("index.html", audio_file=audio_file)

if __name__ == "__main__":
    app.run(debug=True)