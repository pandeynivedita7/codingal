# Import necessary libraries 
import speech_recognition as sr#For converting speech to text
import pyttsx3#For converting text to speech (offline TTS)
from googletrans import Translator	#For translating text via Google Translate
#pyaudio Required for microphone input
#Speech-to-Text (speech recognition)  Translation (Google Translate) Text-to-Speech (voice output)
# -----------------------------
# Text-to-Speech Function
def speak(text, language="en"):#define function(text,lang)
    engine = pyttsx3.init()# Initializes 
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    if language == "en":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

# -----------------------------
# Speech-to-Text Function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Please speak now in English...")
        audio = recognizer.listen(source)
    try:
        print("🔎 Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")
    return ""

# -----------------------------
# Translation Function
def translate_text(text, target_language="es"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"🌍 Translated text: {translation.text}")
    return translation.text

# -----------------------------
# Display Language Options
def display_language_options():
    print("🗣️ Available translation languages:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
    print("9.kannada (ka)")
    print("10. French (fr)")
    choice = input("Select language number (1-8): ")
    language_dict = {
        "1": "hi", "2": "ta", "3": "te", "4": "bn",
        "5": "mr", "6": "gu", "7": "ml", "8": "pa","9":"ka","10":"fr"
    }
    return language_dict.get(choice, "es")

# -----------------------------
# Main Function
def main():
    # Step 1: Show language options and get user's choice
    target_language = display_language_options()

    # Step 2: Convert speech to text
    original_text = speech_to_text()

    if original_text:
        # Step 3: Translate
        translated_text = translate_text(original_text, target_language=target_language)

        # Step 4: Speak translated text
        speak(translated_text, language="en")
        print("✅ Translation spoken out!")

# -----------------------------
# Start the program
if __name__ == "__main__":
    main()

