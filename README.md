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
An intelligent chatbot using DialoGPT medium model from Hugging Face Transformers. It can have contextual conversations with users and maintains conversation history for better responses.

**Features:**
- Pre-trained conversational AI model (DialoGPT-medium)
- Context-aware responses based on conversation history
- Interactive command-line interface
- Multi-turn conversation support
- Natural language understanding

**How it works:**
- Uses transformer-based language model trained on conversational data
- Encodes user input and generates contextual responses
- Supports continuous conversation flow with exit command

**Dependencies:** `transformers`, `torch`

**Installation:**
```bash
pip install transformers torch
```

**Usage:**
```bash
cd "AI Chatbot with Pre-trained Model"
python app.py
```
Type "exit" to end the conversation.

---

### 2. AI-Based Sentiment Analyzer
Analyzes the sentiment of text (positive, negative, neutral) using DistilBERT model fine-tuned on sentiment analysis tasks. Perfect for social media monitoring, review analysis, and customer feedback processing.

**Features:**
- Fast sentiment classification using DistilBERT
- Supports positive, negative, and neutral sentiment detection
- Easy-to-use API
- Can analyze single texts or batch processing

**How it works:**
- Uses pre-trained DistilBERT model fine-tuned on SST-2 dataset
- Provides sentiment label and confidence score
- Processes text in real-time

**Dependencies:** `transformers`, `torch`

**Installation:**
```bash
pip install transformers torch
```

**Usage:**
```bash
cd "AI-Based Sentiment Analyzer"
python app.py
```

---

### 3. Handwritten Text Recognition
Recognizes handwritten text from images using OCR (Optical Character Recognition) technology powered by Tesseract. Ideal for digitizing handwritten documents, notes, and forms.

**Features:**
- OCR-based handwritten text extraction
- Support for multiple image formats (PNG, JPG, JPEG)
- Text extraction from scanned documents
- Language support configuration

**How it works:**
- Processes images using image preprocessing
- Applies OCR using Tesseract engine
- Returns extracted text in readable format

**Dependencies:** `pytesseract`, `Pillow`

**Installation:**
```bash
pip install pytesseract Pillow
# Also install Tesseract OCR: https://github.com/tesseract-ocr/tesseract
```

**Usage:**
```bash
cd "Handwritten Text Recognition"
python app.py
```

---

### 4. Real-time Face Recognition
Detects and recognizes faces in real-time using webcam or images. Built with face_recognition library and OpenCV for video processing. Perfect for security systems, attendance tracking, and access control.

**Features:**
- Real-time face detection and recognition
- Webcam integration for live video processing
- Face matching and identification
- Support for multiple faces in a single frame
- Image-based face recognition

**How it works:**
- Uses dlib's face recognition model
- Extracts facial features (128-dimensional face encodings)
- Compares faces with known face database
- Detects faces in real-time video stream

**Dependencies:** `opencv-python`, `face-recognition`, `numpy`, `cmake`, `dlib`

**Installation:**
```bash
pip install opencv-python face-recognition numpy cmake dlib
```

**Usage:**
```bash
cd "Real-time Face Recognition"
python app.py
```

---

### 5. Image Caption Generator
Generates descriptive captions for images using deep learning models like BLIP or GPT-based vision-language models. Automatically describes what's happening in an image.

**Features:**
- Automatic image description generation
- Natural language captions
- Support for various image types
- Context-aware descriptions

**How it works:**
- Uses vision-language models (e.g., BLIP, CLIP)
- Processes images through vision encoder
- Generates captions using language decoder
- Returns human-readable image descriptions

**Dependencies:** `transformers`, `Pillow`, `torch`

**Installation:**
```bash
pip install transformers Pillow torch
```

**Usage:**
```bash
cd "Image Caption Generator"
python app.py
```

---

### 6. Text-to-Image Generator
Converts text descriptions into images using AI image generation models like Stable Diffusion. Create images from natural language descriptions.

**Features:**
- Text-to-image generation using AI models
- High-quality image generation
- Customizable image parameters
- Support for various artistic styles

**How it works:**
- Uses diffusion models (e.g., Stable Diffusion)
- Encodes text prompts into latent space
- Generates images through iterative denoising process
- Returns high-resolution generated images

**Dependencies:** `diffusers`, `transformers`, `torch`, `accelerate`

**Installation:**
```bash
pip install diffusers transformers torch accelerate
```

**Usage:**
```bash
cd "Text-to-Image Generator"
python app.py
```

## 🌐 Web Scraping & APIs

### 7. News Scrape
Scrapes news articles from BBC News website and extracts headlines and relevant information. Useful for news aggregation, content monitoring, and data collection.

**Features:**
- Web scraping from BBC News website
- Headline extraction
- Beautiful Soup for HTML parsing
- Automatic content extraction

**How it works:**
- Makes HTTP request to news website
- Parses HTML content using BeautifulSoup
- Extracts headlines from HTML elements
- Displays top 5 news headlines

**Dependencies:** `beautifulsoup4`, `requests`

**Installation:**
```bash
pip install beautifulsoup4 requests
```

**Usage:**
```bash
cd "News Scrape"
python app.py
```

---

### 8. Weather Forecast App
Fetches and displays weather forecasts using OpenWeatherMap API. Get real-time weather data for any city worldwide including temperature, humidity, wind speed, and weather conditions.

**Features:**
- Real-time weather data from OpenWeatherMap API
- Temperature display in Celsius
- Weather conditions and descriptions
- City-based weather lookup
- Error handling for invalid cities

**How it works:**
- Uses OpenWeatherMap API for weather data
- Takes city name as input
- Fetches current weather conditions
- Displays formatted weather information

**Note:** Requires OpenWeatherMap API key (free tier available)

**Dependencies:** `requests`

**Installation:**
```bash
pip install requests
```

**Usage:**
```bash
cd "Weather Forecast App"
# Update API key in app.py before running
python app.py
```

---

### 9. Currency Converter
Converts currencies using real-time exchange rates from ExchangeRate-API. Supports all major currencies with up-to-date conversion rates.

**Features:**
- Real-time exchange rates
- Support for all major currencies (USD, EUR, GBP, INR, etc.)
- Accurate currency conversion
- Free API with no authentication required
- Error handling for invalid currencies

**How it works:**
- Fetches latest exchange rates from ExchangeRate-API
- Takes amount, source currency, and target currency
- Calculates converted amount using current exchange rate
- Returns converted value

**Dependencies:** `requests`

**Installation:**
```bash
pip install requests
```

**Usage:**
```bash
cd "Currency Converter"
python app.py
```
Enter amount and currency codes (e.g., USD, EUR, GBP)

## 🖥️ GUI Applications

### 10. Simple Calculator
A basic calculator application with GUI using Tkinter supporting addition, subtraction, multiplication, and division operations. Perfect for learning GUI development with Python.

**Features:**
- User-friendly graphical interface
- Four basic operations: add, subtract, multiply, divide
- Error handling for division by zero
- Real-time result display
- Simple and intuitive design

**How it works:**
- Uses Tkinter for GUI creation
- Takes two input numbers
- Performs selected operation on button click
- Displays result in label widget

**Dependencies:** `tkinter` (included with Python)

**Installation:**
```bash
# tkinter is included with Python on most systems
# If not available, install: sudo apt-get install python3-tk (Linux)
```

**Usage:**
```bash
cd "Simple Calculator"
python app.py
```

---

### 11. To-Do List Application
A simple task management application with add and delete functionality. Keep track of your daily tasks and manage your productivity.

**Features:**
- Add new tasks to list
- Delete selected tasks
- Visual list display
- Simple and clean interface
- Task management made easy

**How it works:**
- Uses Tkinter for GUI
- Stores tasks in Listbox widget
- Add button inserts new task
- Delete button removes selected task

**Dependencies:** `tkinter` (included with Python)

**Installation:**
```bash
# tkinter is included with Python on most systems
```

**Usage:**
```bash
cd "To-Do List Application"
python app.py
```

## 📝 Text Processing

### 12. Language Translator
Translates text between multiple languages using Google Translate API. Supports 100+ languages for seamless translation.

**Features:**
- Multi-language translation support
- Uses Google Translate API
- Fast and accurate translations
- Simple API for integration
- Support for 100+ languages

**How it works:**
- Uses googletrans library for translation
- Detects source language automatically
- Translates text to target language
- Returns translated text

**Dependencies:** `googletrans==4.0.0rc1`

**Installation:**
```bash
pip install googletrans==4.0.0rc1
```

**Usage:**
```bash
cd "Language Translator"
python app.py
```
Example: Translate English to Spanish (code: 'es')

---

### 13. Text Summarizer
Summarizes long text documents into shorter versions while preserving key information using Natural Language Processing. Uses NLTK for stopword removal and text processing.

**Features:**
- Text summarization using NLP
- Stopword removal for better results
- Tokenization and text processing
- Preserves key information
- Useful for document analysis

**How it works:**
- Uses NLTK for text processing
- Removes stopwords (common words like 'the', 'is', etc.)
- Processes text tokens
- Returns summarized text

**Dependencies:** `nltk`

**Installation:**
```bash
pip install nltk
# Run once to download resources: nltk.download('punkt') and nltk.download('stopwords')
```

**Usage:**
```bash
cd "Text Summarizer"
python app.py
```

---

### 14. Text-Based Adventure Game
An interactive text-based adventure game with multiple story paths and decision points. Navigate through the story by making choices.

**Features:**
- Interactive story gameplay
- Multiple story paths and endings
- Decision-based progression
- Engaging narrative experience
- No dependencies required

**How it works:**
- Uses conditional statements for story branches
- Takes user input for decisions
- Progresses story based on choices
- Different endings based on decisions

**Dependencies:** None (Pure Python)

**Installation:**
```bash
# No installation required - pure Python
```

**Usage:**
```bash
cd "Text-Based Adventure Game"
python app.py
```

## 🖼️ Image Processing

### 15. Image to ASCII Art Converter
Converts images into ASCII art characters. Transforms any image into artistic text-based representation using character density mapping.

**Features:**
- Converts images to ASCII art
- Supports multiple image formats
- Customizable character set
- Adjustable resolution/quality
- Artistic text representation

**How it works:**
- Processes image pixel by pixel
- Maps pixel brightness to ASCII characters
- Creates text-based image representation
- Supports grayscale conversion

**Dependencies:** `Pillow`

**Installation:**
```bash
pip install Pillow
```

**Usage:**
```bash
cd "Image to ASCII Art Converter"
python app.py
```

---

### 16. Screenshot to Text (OCR)
Takes screenshots and extracts text from them using OCR (Optical Character Recognition) technology. Perfect for extracting text from images, screenshots, or scanned documents.

**Features:**
- Screenshot capture functionality
- OCR-based text extraction
- Image preprocessing for better accuracy
- Saves extracted text to file
- Support for multiple image formats

**How it works:**
- Captures screenshot using pyautogui
- Processes image for OCR
- Extracts text using Tesseract OCR
- Saves extracted text to file

**Dependencies:** `pytesseract`, `Pillow`, `pyautogui`

**Installation:**
```bash
pip install pytesseract Pillow pyautogui
# Also install Tesseract OCR: https://github.com/tesseract-ocr/tesseract
```

**Usage:**
```bash
cd "Screenshot to Text (OCR)"
python app.py
```

---

### 17. Screenshot Capture Utility
A utility to capture screenshots with customizable options. Take full-screen or region-specific screenshots with ease.

**Features:**
- Full-screen screenshot capture
- Region-specific screenshot support
- Customizable capture area
- Save screenshots in various formats
- Easy-to-use interface

**How it works:**
- Uses pyautogui for screenshot capture
- Supports full screen or region selection
- Saves images using Pillow
- Supports multiple image formats

**Dependencies:** `Pillow`, `pyautogui`

**Installation:**
```bash
pip install Pillow pyautogui
```

**Usage:**
```bash
cd "Screenshot Capture Utility"
python app.py
```

---

### 18. QR Code Creator
Generates QR codes for text, URLs, or other data. Create scannable QR codes for websites, contact information, or any text content.

**Features:**
- QR code generation for text/URLs
- Customizable QR code size
- Error correction support
- Saves QR codes as images
- Simple API for integration

**How it works:**
- Takes input text or URL
- Generates QR code using qrcode library
- Creates image representation
- Saves as PNG image file

**Dependencies:** `qrcode`, `Pillow`

**Installation:**
```bash
pip install qrcode Pillow
```

**Usage:**
```bash
cd "qr code creator"
python app.py
```

## 🎵 Media & Audio

### 19. Text-to-Speech
Converts text to speech and saves as audio file (MP3 format). Uses pyttsx3 library for offline text-to-speech conversion. Perfect for creating audio books, voiceovers, or accessibility features.

**Features:**
- Text to speech conversion
- Saves audio as MP3 file
- Offline operation (no internet required)
- Support for multiple voices
- Customizable speech rate and volume

**How it works:**
- Uses pyttsx3 engine for TTS
- Converts text input to speech
- Saves audio output to file
- Supports different voice options

**Dependencies:** `pyttsx3`

**Installation:**
```bash
pip install pyttsx3
```

**Usage:**
```bash
cd "Text-to-Speech"
python app.py
```

---

### 20. Voice-to-Text Converter
Converts speech/audio to text using speech recognition. Uses Google Speech Recognition API for accurate transcription. Perfect for dictation, voice commands, or audio transcription.

**Features:**
- Speech to text conversion
- Real-time audio input processing
- Multiple recognition engines support
- Microphone input handling
- High accuracy transcription

**How it works:**
- Captures audio from microphone
- Processes audio using SpeechRecognition
- Uses Google Speech API for transcription
- Returns transcribed text

**Dependencies:** `SpeechRecognition`, `pyaudio`

**Installation:**
```bash
pip install SpeechRecognition pyaudio
```

**Usage:**
```bash
cd "Voice-to-Text Converter"
python app.py
```
Speak into microphone when prompted.

---

### 21. Voice Assistant
A voice-activated assistant that responds to voice commands. Combines speech recognition and text-to-speech for interactive voice-based interaction.

**Features:**
- Voice command recognition
- Voice response output
- Interactive conversation
- Multiple command support
- Hands-free operation

**How it works:**
- Listens for voice commands using speech recognition
- Processes commands and generates responses
- Speaks responses using text-to-speech
- Continuous interaction loop

**Dependencies:** `SpeechRecognition`, `pyttsx3`, `pyaudio`

**Installation:**
```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

**Usage:**
```bash
cd "Voice Assistant"
python app.py
```

---

### 22. YouTube Video Downloader
Downloads videos from YouTube in various formats and quality options. Supports MP4, MP3 formats with customizable quality settings. Perfect for offline viewing or audio extraction.

**Features:**
- YouTube video downloading
- Multiple format support (MP4, MP3)
- Quality selection options
- Playlist download support
- Progress tracking

**How it works:**
- Takes YouTube URL as input
- Downloads video using yt-dlp or pytube
- Supports different quality/format options
- Saves video to local directory

**Dependencies:** `yt-dlp` or `pytube`

**Installation:**
```bash
pip install yt-dlp
# OR
pip install pytube
```

**Usage:**
```bash
cd "youtubde-video-downloader"
python app.py
```
Enter YouTube video URL when prompted.

---

### 23. PDF to Text Converter
Extracts text content from PDF files. Supports text-based PDFs and extracts readable content for further processing.

**Features:**
- PDF text extraction
- Support for text-based PDFs
- Batch processing capability
- Preserves text formatting
- Simple API for integration

**How it works:**
- Reads PDF file using PyPDF2 or pdfplumber
- Extracts text from each page
- Combines extracted text
- Returns or saves text content

**Dependencies:** `PyPDF2` or `pdfplumber`

**Installation:**
```bash
pip install PyPDF2
# OR (better for complex PDFs)
pip install pdfplumber
```

**Usage:**
```bash
cd "PDF to Text Converter"
python app.py
```

---

### 24. PDF ko Speech me Convert Karne Ki Script
Converts PDF text to speech in Hindi/Urdu. Extracts text from PDF files and converts it to audio using text-to-speech technology with Hindi/Urdu language support.

**Features:**
- PDF text extraction
- Text-to-speech conversion
- Hindi/Urdu language support
- Saves audio output
- Useful for accessibility

**How it works:**
- Extracts text from PDF using PyPDF2
- Converts text to speech using pyttsx3
- Supports Hindi/Urdu voices
- Saves audio output

**Dependencies:** `PyPDF2`, `pyttsx3`

**Installation:**
```bash
pip install PyPDF2 pyttsx3
```

**Usage:**
```bash
cd "PDF ko Speech me Convert Karne Ki Script"
python app.py
```

---

### 25. PDF ko Speech me Convert Karne Ki Script- UI ke sath
PDF to Speech converter with GUI interface. User-friendly graphical interface for converting PDF text to speech in Hindi/Urdu.

**Features:**
- GUI-based interface
- PDF file selection
- Text-to-speech conversion
- Hindi/Urdu language support
- Easy-to-use design

**How it works:**
- Provides GUI using Tkinter
- Allows PDF file selection
- Extracts text and converts to speech
- Plays or saves audio output

**Dependencies:** `PyPDF2`, `pyttsx3`, `tkinter`

**Installation:**
```bash
pip install PyPDF2 pyttsx3
# tkinter is included with Python
```

**Usage:**
```bash
cd "PDF ko Speech me Convert Karne Ki Script- UI ke sath"
python app.py
```

---

### 26. Text-to-Image
Another text-to-image generation tool using AI models. Creates images from text descriptions with various customization options.

**Features:**
- AI-powered image generation
- Text prompt input
- Customizable image parameters
- High-quality output
- Support for various styles

**How it works:**
- Uses diffusion models (e.g., Stable Diffusion)
- Processes text prompts
- Generates images through AI model
- Returns generated images

**Dependencies:** `diffusers`, `transformers`, `torch`, `accelerate`

**Installation:**
```bash
pip install diffusers transformers torch accelerate
```

**Usage:**
```bash
cd "text-to-image"
python app.py
```

## 🛠️ Utilities

### 27. Email Sender
Sends emails programmatically using SMTP. Send emails from your Python script with custom subject, body, and recipient. Supports Gmail and other SMTP servers.

**Features:**
- Programmatic email sending
- Custom email content (subject, body)
- Multiple recipient support
- HTML email support
- SMTP authentication

**How it works:**
- Uses SMTP protocol for email sending
- Authenticates with email server
- Creates email message with content
- Sends email to specified recipient

**Note:** Update email credentials and SMTP settings in the script before use.

**Dependencies:** `smtplib` (included with Python)

**Installation:**
```bash
# smtplib is included with Python
# Update email credentials in app.py
```

**Usage:**
```bash
cd "email-sender"
# Update email credentials in app.py
python app.py
```

**Security Note:** Use app passwords or OAuth for Gmail instead of regular passwords.

---

### 28. Password Generator
Generates strong random passwords with customizable length and character sets. Creates secure passwords using Python's random module with letters, digits, and special characters.

**Features:**
- Random password generation
- Customizable password length
- Multiple character sets (letters, digits, symbols)
- Strong security features
- Easy integration

**How it works:**
- Generates random characters from character set
- Combines letters (uppercase/lowercase), digits, and punctuation
- Creates password of specified length
- Returns secure random password

**Dependencies:** None (Pure Python - uses built-in `random` and `string` modules)

**Installation:**
```bash
# No installation required - pure Python
```

**Usage:**
```bash
cd "password-genrator"
python app.py
```
Modify `length` parameter in code to customize password length.

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

**Amaanullah**
- GitHub: [@akamaanullah](https://github.com/akamaanullah)
- Website: [amaanullah.com](https://amaanullah.com)
- Email: [info@amaanullah.com](mailto:info@amaanullah.com)

## 📞 Contact

For questions, suggestions, or collaborations, feel free to reach out:

- **Website:** [amaanullah.com](https://amaanullah.com)
- **Email:** [info@amaanullah.com](mailto:info@amaanullah.com)
- **GitHub:** [@akamaanullah](https://github.com/akamaanullah)

## 🙏 Acknowledgments

- Thanks to all the open-source libraries and frameworks used in these projects
- Special thanks to Hugging Face, Google, and other service providers for their APIs and models
- Appreciation to the Python community for excellent documentation and support
- Thanks to all contributors and users of these projects

## 📝 Additional Notes

- **Educational Purpose:** These projects are designed for learning and educational purposes
- **Contributions Welcome:** Feel free to contribute improvements, bug fixes, or new features
- **Issues:** If you encounter any issues or have suggestions, please open an issue on GitHub
- **License:** This project is open source and available for educational use
- **Model Downloads:** First-time use of AI models may require downloading large files (ensure stable internet connection)
- **API Keys:** Some projects require API keys (weather, email services) - configure them before use

---

⭐ If you found this collection helpful, please consider giving it a star!

📧 **Contact us at:** [info@amaanullah.com](mailto:info@amaanullah.com) | 🌐 **Visit:** [amaanullah.com](https://amaanullah.com)
