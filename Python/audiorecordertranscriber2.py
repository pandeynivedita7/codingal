# speech to text audio file
#user friend recording start enter key it will stop
#sppining animation recording process
# saving transcrpit and visualization
import threading #multi task 
import sys# system i/p and o/p
import time # access time
import pyaudio# For accessing and recording audio from the microphone.
import numpy as np#For numerical operations, especially to convert audio bytes to a numerical array for waveform plotting.
import matplotlib.pyplot as plt#For plotting the audio waveform.
import wave#For saving the recorded audio into a WAV file format.
import speech_recognition as sr#For converting speech to text using Google Speech Recognition.

stop_event = threading.Event()

def wait_for_enter():
    input("\nPress Enter to stop recording...\n")
    stop_event.set()# object therad start or stop loop

def spinner():
    spinner_chars = '|/-\\'# feedback animation
    idx = 0
    while not stop_event.is_set():
        sys.stdout.write('\rRecording... ' + spinner_chars[idx % len(spinner_chars)])# new line
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write('\rRecording stopped.          \n')

def record_until_enter():
    FORMAT = pyaudio.paInt16#Specifies the audio format (16-bit integers).
    CHANNELS = 1#Sets the audio to mono.
    RATE = 16000#Sets the sampling rate to 16,000 samples per second. This is a common rate for speech.
    CHUNK = 1024#input

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    # Start input listener and spinner
    input_thread = threading.Thread(target=wait_for_enter)
    spinner_thread = threading.Thread(target=spinner)
    input_thread.start()
    spinner_thread.start()

    while not stop_event.is_set():
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    audio_data = b''.join(frames)
    sample_width = p.get_sample_size(FORMAT)
    return audio_data, RATE, sample_width

def save_audio(data, rate, width, filename="audio.wav"):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)
    print(f"Audio saved as '{filename}'")

def transcribe_audio(data, rate, width, filename="transcription.txt"):
    recognizer = sr.Recognizer()
    audio = sr.AudioData(data, rate, width)
    try:
        text = recognizer.recognize_google(audio)
        print("Transcription:\n", text)
        with open(filename, 'w') as f:
            f.write(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service:", e)

def show_waveform(data, rate):
    audio_np = np.frombuffer(data, dtype=np.int16)
    time_axis = np.linspace(0, len(audio_np) / rate, num=len(audio_np))
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, audio_np)
    plt.title("Audio Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    print("Start speaking... Press Enter to stop.")
    audio_data, rate, width = record_until_enter()
    save_audio(audio_data, rate, width)
    transcribe_audio(audio_data, rate, width)
    show_waveform(audio_data, rate)

if __name__ == "__main__":
    main()
