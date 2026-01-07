import threading
import sys
import time
import wave
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import speech_recognition as sr
from speech_recognition import AudioData

stop_event = threading.Event()


def wait_for_enter():
    input("Press Enter to stop recording...\n")
    stop_event.set()


def spinner():
    spinner_chars = "-\\|/"
    idx = 0
    while not stop_event.is_set():
        sys.stdout.write("\rRecording... " + spinner_chars[idx % len(spinner_chars)])
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write("\rRecording stopped.   \n")


def record_until_enter():
    p = pyaudio.PyAudio()

    format = pyaudio.paInt16
    channels = 1
    rate = 44100
    chunk = 1024
    frames = []

    stream = p.open(
        format=format,
        channels=channels,
        rate=rate,
        input=True,
        frames_per_buffer=chunk
    )

    threading.Thread(target=wait_for_enter).start()
    threading.Thread(target=spinner).start()

    while not stop_event.is_set():
        try:
            data = stream.read(chunk)
            frames.append(data)
        except Exception as e:
            print("Stream error:", e)
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    return b"".join(frames), rate, channels


def save_audio(data, rate, channels, filename="recorded_audio.wav"):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(data)

    print(f"Audio saved to {filename}")


def transcribe_audio(data, rate, filename="transcript.txt"):
    recognizer = sr.Recognizer()

    try:
        audio = AudioData(data, rate, 2)
        text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        text = "Could not understand the audio."
    except sr.RequestError as e:
        text = f"API error: {e}"

    print("Transcription:", text)

    with open(filename, "w") as f:
        f.write(text)

    print(f"Transcript saved to {filename}")


def show_waveform(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)
    time_axis = np.linspace(0, len(samples) / rate, num=len(samples))

    plt.plot(time_axis, samples)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title("Audio Waveform")
    plt.show()


def main():
    print("Speak into the mic. Press Enter to stop.")
    audio_data, rate, channels = record_until_enter()
    save_audio(audio_data, rate, channels)
    transcribe_audio(audio_data, rate)
    show_waveform(audio_data, rate)


if __name__ == "__main__":
    main()
