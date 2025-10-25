# Step 1: Install required libraries
!pip install -q SpeechRecognition pydub# google API transcribe pydub

# Step 2: Import modules
import numpy as np
import matplotlib.pyplot as plt
import wave
import speech_recognition as sr
from speech_recognition import AudioData
from pydub import AudioSegment
from pydub.utils import make_chunks
from io import BytesIO
from google.colab import files

# Step 3: Upload an audio file
print("Please upload a WAV file (mono, 16-bit PCM, 16000Hz preferred)...")
uploaded = files.upload()

# Get uploaded filename
filename = list(uploaded.keys())[0]

# Step 4: Display waveform
def show_waveform(file_path):# function waveform
    with wave.open(file_path, 'rb') as wf:
        rate = wf.getframerate()
        frames = wf.readframes(wf.getnframes())
        samples = np.frombuffer(frames, dtype=np.int16)# buffer temp storage
        time_axis = np.linspace(0, len(samples) / rate, num=len(samples))

    plt.figure(figsize=(12, 4))
    plt.plot(time_axis, samples)
    plt.title("Audio Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

show_waveform(filename)

# Step 5: Transcribe using Google Speech Recognition API
def transcribe_audio(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        text = "Could not understand the audio."
    except sr.RequestError as e:
        text = f"API Error: {e}"
    
    print("Transcription:\n", text)
    with open("transcription.txt", "w") as f:
        f.write(text)
    files.download("transcription.txt")

transcribe_audio(filename)
