import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import time

engine = pyttsx3.init()

# Function to listen to voice commands
def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = recognizer.listen(source)
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I didn't understand that."
    except sr.RequestError:
        return "Error with the service."
    except OSError:
        return "No microphone found. Please check your microphone settings."

# Function to speak to the user
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except KeyboardInterrupt:
        print("Speech interrupted. Exiting...")
        return

while True:
    command = listen().lower()
    
    # Handling recognized voice commands
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "what time is it" in command:
        speak(f"The time is {datetime.datetime.now().strftime('%H:%M:%S')}")
    elif "exit" in command:
        speak("Goodbye")
        break
    else:
        # Speak if command is not recognized
        speak("Sorry, I didn't catch that. Can you please repeat?")
    
    time.sleep(1)  # Small delay to prevent program from running too quickly
