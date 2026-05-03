from gtts import gTTS

with open("script.txt", "r") as f:
    text = f.read()

tts = gTTS(text=text, lang='en', slow=True)
tts.save("audio/voice.mp3")
