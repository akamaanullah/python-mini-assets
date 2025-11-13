import speech_recognition as sr

recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
    
    print("You said: " + recognizer.recognize_google(audio))

except sr.UnknownValueError:
    print("Sorry, I did not understand that.")
except sr.RequestError:
    print("Couldn't get results, check your internet connection.")
except OSError:
    print("No microphone found. Please check your microphone connection and try again.")
