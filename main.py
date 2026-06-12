from voice import speak
from listen import listen
from commands import execute

speak("Hello Dilip. I am Ultron.")

while True:

    command = listen()

    print("You said:", command)

    if "exit" in command:
        speak("Goodbye Dilip")
        break

    if command:
        speak("Executing command")
        execute(command)