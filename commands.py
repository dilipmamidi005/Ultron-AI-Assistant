import webbrowser
import subprocess

def execute(command):

    if "youtube" in command:

        print("Opening YouTube...")
        webbrowser.open("https://youtube.com")

    elif "whatsapp" in command:

        print("Opening WhatsApp...")
        webbrowser.open("https://web.whatsapp.com")

    elif "github" in command:

        print("Opening GitHub...")
        webbrowser.open("https://github.com")

    elif "google" in command:

        print("Opening Google...")
        webbrowser.open("https://google.com")

    elif "instagram" in command:

        print("Opening Instagram...")
        webbrowser.open("https://instagram.com")

    elif "calculator" in command:
        print("Opening Calculator...")
        subprocess.Popen("calc.exe")

    elif "vs code" in command:
        print("Opening VS Code...")
        subprocess.Popen(r"C:\Users\Lenovo\AppData\Local\Programs\Microsoft VS Code\Code.exe")
        

    elif "file explorer" in command:
        print("Opening File Explorer...")
        subprocess.Popen("explorer")

    elif "ultron folder" in command:
        print("Opening Ultron Folder...")
        subprocess.Popen(r'explorer "C:\Ultron Ai assistent"')

    else:

        print("Command not recognized")