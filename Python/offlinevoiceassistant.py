import speech_recognition as sr#•	speech_recognition for speech-to-text (listening).
import pyttsx3#•	pyttsx3 for text-to-speech (speaking).
from datetime import datetime#•	datetime to respond with the current time.

# Function to make the assistant speak
def speak(text):
    engine = pyttsx3.init()# Initialize text-to-speech engine
    engine.setProperty('rate', 150)  # Set speech speed # Set speaking rate (words per minute)
    engine.say(text)# Add the text to speak
    engine.runAndWait()# Speak out loud

# Function to get audio input from the user and convert to text
def get_audio():
    r = sr.Recognizer()## Create Recognizer instance
    with sr.Microphone() as source:# Use microphone for input
        print("🎤 Speak now...")
        audio = r.listen(source)# Listen for input
        try:
            command = r.recognize_google(audio)# Convert speech to text using Google
            print(f"✅ You said: {command}")
            return command.lower()# Return in lowercase for easier matching
        except sr.UnknownValueError:
            print("❌ Could not understand.")
        except sr.RequestError as e:
            print(f"❌ API Error: {e}")
    return ""# Return empty string if there’s an error

# Function to respond based on voice commands
def respond_to_command(command):
    if "hello" in command:
        speak("Hi there! How can I help you today?")
    elif "your name" in command:
        speak("I am your Python voice assistant.")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")# Get current time
        speak(f"The time is {now}")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False# Stop the assistant
    else:
        speak("I'm not sure how to help with that.")
    return True# Continue running

# Main function to activate the assistant
def main():
    speak("Voice assistant activated. Say something!")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break# Exit if respond_to_command returns False

# Run the assistant
if __name__ == "__main__":
    main()
#•	“Hello” → 💬 “Hi there! How can I help you today?”
#	“What’s your name?” → 💬 “I am your Python voice assistant.”
#	“What time is it?” → 💬 “The time is 16:42”
#	“Exit” or “Stop” → 💬 “Goodbye!” (and the program ends)
