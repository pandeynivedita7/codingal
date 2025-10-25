import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer # For offline speech recognition.
import pyttsx3 #Converts text to speech.
import json# To handle recognition results.
import datetime#To fetch the current time/date.

# -----------------------------
# Initialize Vosk model and TTS engine
# -----------------------------
model = Model("model")  # Folder must contain the Vosk model
recognizer = KaldiRecognizer(model, 16000)
audio_queue = queue.Queue()
tts_engine = pyttsx3.init() #Initializes the speech engine for speaking responses.

# -----------------------------
# Callback to collect microphone audio
# -----------------------------
def callback(indata, frames, time, status):
    if status:
        print(f"Audio status: {status}")
    audio_queue.put(bytes(indata))#Sends data to the recognizer.

# -----------------------------
# Function to process recognized text and respond
# -----------------------------
def process_query(query):
    query = query.lower()
    if "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        response = f"The current time is {now}."
    elif "date" in query:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        response = f"Today's date is {today}."
    else:
        response = "I'm sorry, I didn't understand that."
    return response

# -----------------------------
# Start audio stream and recognize input
# -----------------------------
def main():
    print("🎤 Listening... Speak 'time' or 'date'. Press Ctrl+C to stop.")

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):#Starts microphone stream.
        while True:
            data = audio_queue.get()#Retrieves audio data from the queue.
            if recognizer.AcceptWaveform(data):#Checks if a complete speech command was received.
                result = json.loads(recognizer.Result())# Gets the recognized text
                text = result.get("text", "")
                if text:
                    print(f"\n🗣️ You said: {text}")
                    response = process_query(text)
                    print(f"🤖 Assistant: {response}")
                    tts_engine.say(response)
                    tts_engine.runAndWait()

# -----------------------------
# Run main loop
# -----------------------------
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Program stopped by user.")
