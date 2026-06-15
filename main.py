from voice import speak
from listen import listen
from commands import execute
from brain import ask_ai
from memory import remember, recall

speak("Hello Dilip. I am Ultron.")

while True:

    command = listen()

    print("You said:", command)

    if not command:
        continue

    if "exit" in command or "stop" in command or "goodbye" in command:

        speak("Goodbye Dilip")
        break

    if "remember my name is" in command:

        name = command.replace("remember my name is", "").strip()

        remember("name", name)

        speak(f"I will remember your name is {name}")

        continue

    if "what is my name" in command:

        name = recall("name")

        if name:
            speak(f"Your name is {name}")
        else:
            speak("I don't know your name yet")

        continue

    if (
        "youtube" in command
        or "chatgpt" in command
        or "github" in command
        or "instagram" in command
        or "calculator" in command
        or "vs code" in command
        or "file explorer" in command
    ):

        speak("Executing command")
        execute(command)

    else:

        answer = ask_ai(command)

        print(answer)

        speak(answer[:300])