import pyttsx3
import PyPDF2

def pdf_to_speech(pdf_file, output_audio="output.mp3"):
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text() + "\n"
    
    if text:
        engine = pyttsx3.init()
        engine.save_to_file(text, output_audio)
        engine.runAndWait()
        print(f"Speech saved as {output_audio}")
    else:
        print("Error: PDF se text extract nahi ho raha!")

pdf_to_speech("response.pdf")
