import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import pyttsx3
import json
import datetime
model = Model =("model")
recognizer = KaldiRecognizer(model, 16000)
audio_queue.Queue()
tts_engine = pyttsx3.init()
def callback(indata, frmes, time, status):
    if status:
        print(status)
    audio_queue.put(bytes(indata))
def process_query(query):
    query = query.lower()
    if "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        response = f"The current time is {now}."
    elif "date" in query:
        today = datetime.datetime.now().stftime("%B%d, %Y")
        response = f"Today's date is {today}."
    else:
        response = "!'m sorry, I didn't unsertand that."
    return response
with sd.RawlputStream(s)