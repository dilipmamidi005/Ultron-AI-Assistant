import os

os.environ["PATH"] += os.pathsep + r"C:\Ultron Ai assistent\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"
import whisper
import speech_recognition as sr

model = whisper.load_model("base")

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        audio = recognizer.listen(source)

    with open("command.wav", "wb") as f:
        f.write(audio.get_wav_data())

    result = model.transcribe("command.wav")

    text = result["text"].lower()

    return text