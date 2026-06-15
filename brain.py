import google.generativeai as genai

API_KEY = "YOUR_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_ai(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"AI Error: {e}"