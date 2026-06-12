import speech_recognition as sr
import wave

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak for 5 seconds...")
    audio = r.listen(source)

with open("test.wav", "wb") as f:
    f.write(audio.get_wav_data())

print("Saved as test.wav")