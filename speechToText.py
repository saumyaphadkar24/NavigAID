import speech_recognition as sr

def speech_to_text_from_mic():
    # Initialize the recognizer
    print("Starting speech recognition")
    recognizer = sr.Recognizer()

    try:
        # Use the microphone as source for input
        print("Attempting to access the microphone...")
        with sr.Microphone() as source:
            print("Microphone accessed successfully!")
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for speech...")
            audio = recognizer.listen(source)
    except Exception as e:
        print(f"Error accessing the microphone: {e}")
        return

    try:
        # Recognize speech using Google Web Speech API (default)
        print("Converting speech to text...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    speech_to_text_from_mic()
