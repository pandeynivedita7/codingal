import sounddevice as sd
from vosk import Model, KaldiRecognizer
import pyttsx3
import json
import datetime
import webbrowser
import queue
import sys
#1. Go to: https://alphacephei.com/vosk/models
#2. Download a model (recommended: **vosk-model-small-en-us-0.15** for English - ~40MB)
#Extract the downloaded folder
#4. Rename it to **"model"**
#5. Place it in the same directory as your Python script
class VoiceAssistant:
    def __init__(self, model_path="model"):
        # Initialize Vosk model and recognizer
        try:
            self.model = Model(model_path)
            self.recognizer = KaldiRecognizer(self.model, 16000)
        except:
            print("ERROR: Please download Vosk model first!")
            print("Download from: https://alphacephei.com/vosk/models")
            print("Extract to a folder named 'model' in the same directory")
            sys.exit(1)
        
        # Initialize audio queue
        self.audio_queue = queue.Queue()
        
        # Initialize TTS engine
        self.tts_engine = pyttsx3.init()
        self.setup_voice()
        
        self.is_listening = True
    
    def setup_voice(self):
        """Configure voice properties"""
        voices = self.tts_engine.getProperty('voices')
        self.tts_engine.setProperty('voice', voices[0].id)
        self.tts_engine.setProperty('rate', 180)
        self.tts_engine.setProperty('volume', 0.9)
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"Assistant: {text}")
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
    
    def callback(self, indata, frames, time, status):
        """Callback function to capture audio data"""
        if status:
            print(status)
        self.audio_queue.put(bytes(indata))
    
    def listen(self):
        """Listen and recognize speech using Vosk"""
        print("Listening... (Speak now)")
        
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                               channels=1, callback=self.callback):
            while self.is_listening:
                data = self.audio_queue.get()
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    text = result.get('text', '')
                    if text:
                        print(f"You said: {text}")
                        return text
        return ""
    
    def process_query(self, query):
        """Function to process user input and respond"""
        query = query.lower()
        
        # Exit commands
        if any(word in query for word in ['exit', 'quit', 'bye', 'goodbye']):
            self.speak("Goodbye! Have a great day!")
            return False
        
        # Time
        if "time" in query:
            now = datetime.datetime.now().strftime("%I:%M %p")
            response = f"The current time is {now}"
            self.speak(response)
        
        # Date
        elif "date" in query or "today" in query:
            now = datetime.datetime.now().strftime("%B %d, %Y")
            response = f"Today's date is {now}"
            self.speak(response)
        
        # Day
        elif "day" in query:
            now = datetime.datetime.now().strftime("%A")
            response = f"Today is {now}"
            self.speak(response)
        
        # Search
        elif "search" in query or "google" in query:
            search_term = query.replace("search", "").replace("google", "").strip()
            if search_term:
                url = f"https://www.google.com/search?q={search_term}"
                webbrowser.open(url)
                self.speak(f"Searching for {search_term}")
            else:
                self.speak("What do you want me to search for?")
        
        # Open website
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            self.speak("Opening YouTube")
        
        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            self.speak("Opening Google")
        
        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com")
            self.speak("Opening Gmail")
        
        # Greetings
        elif any(word in query for word in ['hello', 'hi', 'hey']):
            self.speak("Hello! How can I help you today?")
        
        # How are you
        elif "how are you" in query:
            self.speak("I'm doing great! Thank you for asking. How can I assist you?")
        
        # Name
        elif "your name" in query or "who are you" in query:
            self.speak("I am your voice assistant powered by Vosk and pyttsx3!")
        
        # Help
        elif "help" in query:
            self.speak("I can tell you the time, date, search the web, open websites like YouTube and Google, and answer basic questions. Just ask me!")
        
        # Unknown command
        else:
            if query.strip():  # Only respond if there was actual input
                self.speak("I'm not sure how to help with that. Try saying 'help' to see what I can do.")
        
        return True
    
    def run(self):
        """Main function to run the assistant"""
        self.speak("Hello! I am your voice assistant. How can I help you?")
        print("\n" + "="*50)
        print("Voice Assistant is running...")
        print("="*50)
        print("\nCommands you can try:")
        print("- 'What time is it?'")
        print("- 'What's the date?'")
        print("- 'Search Python tutorials'")
        print("- 'Open YouTube'")
        print("- 'Help'")
        print("- 'Exit' or 'Bye'")
        print("="*50 + "\n")
        
        try:
            while True:
                query = self.listen()
                if query:
                    if not self.process_query(query):
                        break
        except KeyboardInterrupt:
            print("\n\nStopping assistant...")
            self.speak("Goodbye!")
        except Exception as e:
            print(f"Error: {e}")
            self.speak("Sorry, I encountered an error.")

# Run the assistant
if __name__ == "__main__":
    print("\n" + "="*50)
    print("VOICE ASSISTANT with VOSK")
    print("="*50)
    print("\nBefore running, make sure you have:")
    print("1. Downloaded a Vosk model from https://alphacephei.com/vosk/models")
    print("2. Extracted it to a folder named 'model' in this directory")
    print("3. Installed required packages:")
    print("   pip install vosk sounddevice pyttsx3")
    print("="*50 + "\n")
    
    input("Press Enter to start the assistant...")
    
    assistant = VoiceAssistant()
    assistant.run()