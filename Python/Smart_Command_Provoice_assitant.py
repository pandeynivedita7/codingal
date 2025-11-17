import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"✅ You said: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        print("❌ Could not understand. Please repeat.")
        return ""
    except sr.RequestError as e:
        print(f"⚠️ API Error: {e}")
        return ""

def greet_user():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Smart Command Pro. How can I assist you?")

def respond_to_command(command):
    if "hello" in command:
        speak("Hi there! How can I help you today?")
    elif "your name" in command:
        speak("I am Smart Command Pro, your upgraded voice assistant.")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "date" in command:
        today = datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {today}")
    elif "search" in command:
        speak("What should I search for?")
        query = get_audio()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the results for {query}")
    elif "wikipedia" in command:
        speak("What do you want to know from Wikipedia?")
        topic = get_audio()
        if topic:
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(f"According to Wikipedia, {summary}")
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find that page.")
    elif "exit" in command or "stop" in command or "goodbye" in command:
        speak("Goodbye! Have a great day.")
        return False
    else:
        speak("I'm not sure how to help with that.")
    return True

def main():
    speak("Activating Smart Command Pro...")
    greet_user()
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break

if __name__ == "__main__":
    main()