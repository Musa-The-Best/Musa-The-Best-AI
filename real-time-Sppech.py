import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Initialize text-to-speech engine
def speak(text, language='en'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Select voice based on language (if supported by pyttsx3)
    if language == 'en':
        engine.setProperty('voice', voices[0].id)  # Default English voice
    else:
        engine.setProperty('voice', voices[1].id)  # Fallback voice if available

    engine.say(text)
    engine.runAndWait()

# Speech-to-text: recognize spoken language
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Please speak...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🔎 Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"📝 You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio")
    except sr.RequestError as e:
        print(f"⚠ API Error: {e}")
    return ""

# Translate text into target language
def translate_text(text, target_language='es'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"🌍 Translated text: {translation.text}")
    return translation.text

# Display language options to user
def display_language_options():
    print("\n🌐 Available Translation Languages:")
    print("1. Spanish (es)")
    print("2. Urdu (ur)")
    print("3. Hindi (hi)")
    print("4. French (fr)")
    print("5. German (de)")

    choice = input("Please select the target language number (1-5): ")

    language_dict = {
        '1': 'es',
        '2': 'ur',
        '3': 'hi',
        '4': 'fr',
        '5': 'de'
    }

    return language_dict.get(choice, 'es')  # Default to Spanish if invalid input

# Main function to combine all steps
def main():
    print("🎙 Real-time Speech Translation App")

    # Step 1: Display language options and get user's choice
    target_language = display_language_options()

    # Step 2: Convert speech to text (speech in any language)
    original_text = speech_to_text()

    if original_text:
        # Step 3: Translate text into selected target language
        translated_text = translate_text(original_text, target_language)

        # Step 4: Text-to-speech (translate output and speak it)
        print("🔊 Speaking the translated text...")
        speak(translated_text, target_language)

if __name__ == "__main__":
    main()
