import pyttsx3

def text_to_speech(text, filename="mahad-1.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"Speech saved as {filename}")

text_to_speech("Hello Mustafa! How are you? how's your first day in RTG.")
