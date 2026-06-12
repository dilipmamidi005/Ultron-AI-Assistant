import webbrowser

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

    else:

        print("Command not recognized")