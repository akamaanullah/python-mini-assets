# Python Mini Projects Collection

A comprehensive collection of mini Python projects covering various domains including AI/ML, web scraping, GUI applications, utilities, and more. Each project is self-contained and demonstrates different Python concepts and libraries.

## 📋 Table of Contents

- [AI & Machine Learning](#ai--machine-learning)
- [Web Scraping & APIs](#web-scraping--apis)
- [GUI Applications](#gui-applications)
- [Text Processing](#text-processing)
- [Image Processing](#image-processing)
- [Media & Audio](#media--audio)
- [Utilities](#utilities)
- [Games](#games)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## 🤖 AI & Machine Learning

### 1. AI Chatbot with Pre-trained Model
An intelligent chatbot using DialoGPT medium model from Hugging Face Transformers. It can have contextual conversations with users.

**Features:**
- Pre-trained conversational AI model
- Context-aware responses
- Interactive command-line interface

**Dependencies:** `transformers`, `torch`

**Usage:**
```bash
cd "AI Chatbot with Pre-trained Model"
python app.py
```

### 2. AI-Based Sentiment Analyzer
Analyzes the sentiment of text (positive, negative, neutral) using AI models.

**Dependencies:** `transformers`, `torch`

**Usage:**
```bash
cd "AI-Based Sentiment Analyzer"
python app.py
```

### 3. Handwritten Text Recognition
Recognizes handwritten text from images using OCR technology.

**Dependencies:** `pytesseract`, `Pillow`

**Usage:**
```bash
cd "Handwritten Text Recognition"
python app.py
```

### 4. Real-time Face Recognition
Detects and recognizes faces in real-time using webcam or images.

**Dependencies:** `opencv-python`, `face-recognition`, `numpy`

**Usage:**
```bash
cd "Real-time Face Recognition"
python app.py
```

### 5. Image Caption Generator
Generates descriptive captions for images using deep learning models.

**Dependencies:** `transformers`, `Pillow`, `torch`

**Usage:**
```bash
cd "Image Caption Generator"
python app.py
```

### 6. Text-to-Image Generator
Converts text descriptions into images using AI image generation models.

**Dependencies:** `diffusers`, `transformers`, `torch`

**Usage:**
```bash
cd "Text-to-Image Generator"
python app.py
```

## 🌐 Web Scraping & APIs

### 7. News Scrape
Scrapes news articles from websites and extracts relevant information.

**Dependencies:** `beautifulsoup4`, `requests`

**Usage:**
```bash
cd "News Scrape"
python app.py
```

### 8. Weather Forecast App
Fetches and displays weather forecasts using weather API.

**Dependencies:** `requests`

**Usage:**
```bash
cd "Weather Forecast App"
python app.py
```

### 9. Currency Converter
Converts currencies using real-time exchange rates from API.

**Dependencies:** `requests`

**Usage:**
```bash
cd "Currency Converter"
python app.py
```

## 🖥️ GUI Applications

### 10. Simple Calculator
A basic calculator application with GUI using Tkinter supporting addition, subtraction, multiplication, and division.

**Dependencies:** `tkinter` (included with Python)

**Usage:**
```bash
cd "Simple Calculator"
python app.py
```

### 11. To-Do List Application
A simple task management application with add and delete functionality.

**Dependencies:** `tkinter` (included with Python)

**Usage:**
```bash
cd "To-Do List Application"
python app.py
```

## 📝 Text Processing

### 12. Language Translator
Translates text between multiple languages using Google Translate API.

**Dependencies:** `googletrans==4.0.0rc1`

**Usage:**
```bash
cd "Language Translator"
python app.py
```

### 13. Text Summarizer
Summarizes long text documents into shorter versions while preserving key information.

**Dependencies:** `sumy`, `nltk`

**Usage:**
```bash
cd "Text Summarizer"
python app.py
```

### 14. Text-Based Adventure Game
An interactive text-based adventure game with multiple story paths.

**Dependencies:** None (Pure Python)

**Usage:**
```bash
cd "Text-Based Adventure Game"
python app.py
```

## 🖼️ Image Processing

### 15. Image to ASCII Art Converter
Converts images into ASCII art characters.

**Dependencies:** `Pillow`

**Usage:**
```bash
cd "Image to ASCII Art Converter"
python app.py
```

### 16. Screenshot to Text (OCR)
Takes screenshots and extracts text from them using OCR technology.

**Dependencies:** `pytesseract`, `Pillow`, `pyautogui`

**Usage:**
```bash
cd "Screenshot to Text (OCR)"
python app.py
```

### 17. Screenshot Capture Utility
A utility to capture screenshots with customizable options.

**Dependencies:** `Pillow`, `pyautogui`

**Usage:**
```bash
cd "Screenshot Capture Utility"
python app.py
```

### 18. QR Code Creator
Generates QR codes for text, URLs, or other data.

**Dependencies:** `qrcode`, `Pillow`

**Usage:**
```bash
cd "qr code creator"
python app.py
```

## 🎵 Media & Audio

### 19. Text-to-Speech
Converts text to speech and saves as audio file.

**Dependencies:** `pyttsx3`

**Usage:**
```bash
cd "Text-to-Speech"
python app.py
```

### 20. Voice-to-Text Converter
Converts speech/audio to text using speech recognition.

**Dependencies:** `SpeechRecognition`, `pyaudio`

**Usage:**
```bash
cd "Voice-to-Text Converter"
python app.py
```

### 21. Voice Assistant
A voice-activated assistant that responds to voice commands.

**Dependencies:** `SpeechRecognition`, `pyttsx3`, `pyaudio`

**Usage:**
```bash
cd "Voice Assistant"
python app.py
```

### 22. YouTube Video Downloader
Downloads videos from YouTube in various formats and quality.

**Dependencies:** `yt-dlp` or `pytube`

**Usage:**
```bash
cd "youtubde-video-downloader"
python app.py
```

### 23. PDF to Text Converter
Extracts text content from PDF files.

**Dependencies:** `PyPDF2` or `pdfplumber`

**Usage:**
```bash
cd "PDF to Text Converter"
python app.py
```

### 24. PDF ko Speech me Convert Karne Ki Script
Converts PDF text to speech in Hindi/Urdu.

**Dependencies:** `PyPDF2`, `pyttsx3`

**Usage:**
```bash
cd "PDF ko Speech me Convert Karne Ki Script"
python app.py
```

### 25. PDF ko Speech me Convert Karne Ki Script- UI ke sath
PDF to Speech converter with GUI interface.

**Dependencies:** `PyPDF2`, `pyttsx3`, `tkinter`

**Usage:**
```bash
cd "PDF ko Speech me Convert Karne Ki Script- UI ke sath"
python app.py
```

### 26. Text-to-Image
Another text-to-image generation tool.

**Dependencies:** `diffusers`, `transformers`, `torch`

**Usage:**
```bash
cd "text-to-image"
python app.py
```

## 🛠️ Utilities

### 27. Email Sender
Sends emails programmatically using SMTP.

**Dependencies:** `smtplib` (included with Python)

**Usage:**
```bash
cd "email-sender"
python app.py
```

**Note:** Update email credentials in the script before use.

### 28. Password Generator
Generates strong random passwords with customizable length and character sets.

**Dependencies:** None (Pure Python)

**Usage:**
```bash
cd "password-genrator"
python app.py
```

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. Clone the repository:
```bash
git clone git@github.com:akamaanullah/python-mini-assets.git
cd python-mini-assets
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate
```

3. Install common dependencies:
```bash
pip install transformers torch pillow requests beautifulsoup4 pytesseract pyttsx3 SpeechRecognition qrcode opencv-python face-recognition
```

4. Install project-specific dependencies as needed for each project.

### Common Dependencies List
```bash
pip install transformers torch pillow requests beautifulsoup4 pytesseract pyttsx3 SpeechRecognition qrcode opencv-python face-recognition numpy googletrans==4.0.0rc1 sumy nltk PyPDF2 pdfplumber yt-dlp pyautogui pyaudio
```

## 🎯 Project Structure

```
python-mini-assets/
├── AI Chatbot with Pre-trained Model/
├── AI-Based Sentiment Analyzer/
├── Currency Converter/
├── email-sender/
├── Handwritten Text Recognition/
├── Image Caption Generator/
├── Image to ASCII Art Converter/
├── Language Translator/
├── News Scrape/
├── password-genrator/
├── PDF ko Speech me Convert Karne Ki Script/
├── PDF ko Speech me Convert Karne Ki Script- UI ke sath/
├── PDF to Text Converter/
├── qr code creator/
├── Real-time Face Recognition/
├── Screenshot Capture Utility/
├── Screenshot to Text (OCR)/
├── Simple Calculator/
├── Text Summarizer/
├── Text-Based Adventure Game/
├── text-to-image/
├── Text-to-Image Generator/
├── Text-to-Speech/
├── To-Do List Application/
├── Voice Assistant/
├── Voice-to-Text Converter/
├── Weather Forecast App/
├── youtubde-video-downloader/
└── README.md
```

## 📚 Features Overview

- **AI/ML Projects:** Chatbots, sentiment analysis, face recognition, image generation
- **Web Tools:** Web scraping, API integration, currency conversion
- **GUI Apps:** Calculator, to-do list with user-friendly interfaces
- **Text Processing:** Translation, summarization, text games
- **Image Tools:** ASCII art, OCR, QR codes, image captioning
- **Media Tools:** Text-to-speech, voice recognition, video download
- **Utilities:** Email sending, password generation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Notes

- Some projects require API keys (e.g., weather, email). Make sure to configure them before use.
- AI/ML projects may require significant computational resources and may take time to download models on first run.
- Some projects use external APIs that may have rate limits or require registration.

## 🔧 Troubleshooting

- **Import errors:** Make sure all required dependencies are installed
- **Model download issues:** Some AI models download on first run - ensure stable internet connection
- **API errors:** Check API keys and rate limits for services requiring authentication
- **Permission errors:** Some projects (like screenshot capture) may require appropriate permissions

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

**Amaan Ullah**
- GitHub: [@akamaanullah](https://github.com/akamaanullah)

## 🙏 Acknowledgments

- Thanks to all the open-source libraries and frameworks used in these projects
- Special thanks to Hugging Face, Google, and other service providers for their APIs and models

---

⭐ If you found this collection helpful, please consider giving it a star!

