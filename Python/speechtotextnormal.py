import sounddevice as sd
import speech_recognition as sr
import numpy as np

def get_audio():
    recognizer = sr.Recognizer()

    samplerate = 16000
    duration = 5  # seconds

    print("Listening...")

    # Record audio normally
    audio_data = sd.rec(int(samplerate * duration),
                        samplerate=samplerate,
                        channels=1,
                        dtype='int16')
    sd.wait()

    # Convert numpy → proper bytes
    audio_bytes = audio_data.tobytes()

    # Create proper AudioData object
    audio = sr.AudioData(audio_bytes, samplerate, sample_width=2)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand speech.")
    except sr.RequestError as e:
        print("API Error:", e)

    return ""

