import os
import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Initialize pyttsx3 for real-time TTS
engine = pyttsx3.init()

def select_pdf():
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if pdf_file:
        entry_pdf.delete(0, tk.END)
        entry_pdf.insert(0, pdf_file)
        text = get_pdf_text(pdf_file)
        if text:
            pdf_text.delete(1.0, tk.END)
            pdf_text.insert(tk.END, text)

def get_pdf_text(pdf_file):
    try:
        with open(pdf_file, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in range(len(reader.pages)):
                text += reader.pages[page].extract_text() + "\n"
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read PDF:\n{e}")
        return None

def play_pdf_audio():
    pdf_file = entry_pdf.get()
    if not pdf_file:
        messagebox.showerror("Error", "Please select a PDF file first!")
        return
    
    text = get_pdf_text(pdf_file)
    if not text:
        return
    
    # Get language and speed from the user
    lang = lang_var.get()
    speed = speed_var.get()
    
    if lang == "en":
        engine.setProperty('rate', speed)  # Adjust speed
        engine.setProperty('voice', "english")  # Select English voice
    else:
        engine.setProperty('rate', speed)
        engine.setProperty('voice', "spanish")  # Select Spanish voice, for example

    engine.say(text)
    engine.runAndWait()

# Create GUI
root = tk.Tk()
root.title("PDF to Speech Converter")
root.geometry("500x300")

# UI Elements
label = tk.Label(root, text="Select a PDF file:", font=("Arial", 12))
label.pack(pady=5)

entry_pdf = tk.Entry(root, width=50)
entry_pdf.pack(pady=5)

btn_browse = tk.Button(root, text="Browse", command=select_pdf)
btn_browse.pack(pady=5)

# PDF preview text box
label_preview = tk.Label(root, text="PDF Preview:", font=("Arial", 12))
label_preview.pack(pady=5)

pdf_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=8)
pdf_text.pack(pady=5)

# Language Selection
lang_var = tk.StringVar(value="en")
label_lang = tk.Label(root, text="Select Language:", font=("Arial", 10))
label_lang.pack(pady=2)
lang_menu = tk.OptionMenu(root, lang_var, "en", "es")
lang_menu.pack(pady=2)

# Speed Control
speed_var = tk.DoubleVar(value=150)  # Default speed 150 words per minute
label_speed = tk.Label(root, text="Select Speed:", font=("Arial", 10))
label_speed.pack(pady=2)
speed_scale = tk.Scale(root, from_=50, to_=300, orient="horizontal", variable=speed_var)
speed_scale.pack(pady=2)

# Button to play PDF as speech
btn_play = tk.Button(root, text="Play PDF as Speech", command=play_pdf_audio)
btn_play.pack(pady=10)

# Run the GUI
root.mainloop()
