import pyttsx3

def speak(text):
    engine = pyttsx3.init()

    print("ULTRON:", text)

    engine.say(text)

    engine.runAndWait()

    engine.stop()