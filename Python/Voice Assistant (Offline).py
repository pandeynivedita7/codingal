# realtime_vosk_tts.py
# Requirements:
#   pip install sounddevice vosk pyttsx3
# Download a Vosk model (e.g. small-en-us model) and extract it to a folder named "model"
# Run: python realtime_vosk_tts.py

import queue
import json
import datetime
import sys

import sounddevice as sd
from vosk import Model, KaldiRecognizer
import pyttsx3

SAMPLE_RATE = 16000          # must match the Vosk model/sample rate
CHANNELS = 1                 # mono audio
MODEL_PATH = "model"         # folder containing the Vosk model

# Initialize
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)
audio_queue = queue.Queue()  # stack FILO and queue FIFO
tts_engine = pyttsx3.init()

def callback(indata, frames, time, status):
    """
    sounddevice RawInputStream callback.
    indata is a bytes-like buffer (dtype='int16' when configured below).
    We push raw bytes to a queue for the main loop to process.
    """
    if status:
        # print device status warnings/errors
        print("Audio status:", status, file=sys.stderr)
    # Put raw bytes onto the queue
    audio_queue.put(bytes(indata))

def process_query(query: str) -> str:
    """
    Simple command/response processing. Add more rules as needed.
    """
    q = query.lower().strip()
    if not q:
        return "I didn't hear anything."
    if "time" in q:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {now}."
    if "date" in q:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {today}."
    if "hello" in q or "hi" in q:
        return "Hello. How can I help you?"
    if "stop" in q or "exit" in q or "quit" in q:
        return "exit"   # special token to stop the program
    # default fallback
    return "I'm sorry, I didn't understand that."

def speak(text: str):
    """Speak text with pyttsx3 (blocking until finished)."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def main():
    print("Starting. Press Ctrl+C to quit.")
    print("Make sure your microphone is set and model folder exists at:", MODEL_PATH)

    try:
        with sd.RawInputStream(samplerate=SAMPLE_RATE,
                               blocksize=8000,
                               dtype='int16',
                               channels=CHANNELS,
                               callback=callback):
            print("Listening...")
            while True:
                data = audio_queue.get()    # blocking until audio chunk available
                if recognizer.AcceptWaveform(data):
                    # final result available
                    result_json = recognizer.Result()
                    result = json.loads(result_json)
                    text = result.get("text", "")
                    if text:
                        print("You said:", text)
                        response = process_query(text)
                        if response == "exit":
                            print("Exit command received. Stopping.")
                            speak("Goodbye.")
                            break
                        print("Assistant:", response)
                        speak(response)
                else:
                    # partial result (optional)
                    partial_json = recognizer.PartialResult()
                    partial = json.loads(partial_json).get("partial", "")
                    if partial:
                        # show partial transcript inline (non-blocking)
                        print(f"\r(partial) {partial}", end="", flush=True)
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception as e:
        print("Error:", str(e))
    finally:
        # attempt to cleanly stop engine
        try:
            tts_engine.stop()
        except Exception:
            pass

if __name__ == "__main__":
    main()
