import speech_recognition as sr
import pyttsx3
import asyncio
from googletrans import Translator

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    voices = engine.getProperty("voices")
    if language == "en":
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id if len(voices) > 1 else voices[0].id)
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now in English:")
        audio = recognizer.listen(source)
    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"API Error: {e}")
    return ""

async def translate_text(text, target_language="ne"):
    translator = Translator()
    translation = await translator.translate(text, dest=target_language)
    print(f"Translated Text: {translation.text}")
    return translation.text

def display_language_options():
    print("Available languages: ")
    print("1. Nepali (ne)")
    print("2. English (en)")
    print("3. Spanish (es)")
    print("4. Hindi (hi)")
    print("5. Chinese (zh-CN)")
    choice = input("Please select the target language number (1-5): ")
    language_dict = {
        "1": "ne",
        "2": "en",
        "3": "es",
        "4": "hi",
        "5": "zh-CN"
    }
    return language_dict.get(choice, "ne")

async def main():
    target_language = display_language_options()
    original_text = speech_to_text()
    if original_text:
        translated_text = await translate_text(original_text, target_language=target_language)
        speak(translated_text, language="en")
        print("Translation spoken out")

if __name__ == "__main__":
    asyncio.run(main())