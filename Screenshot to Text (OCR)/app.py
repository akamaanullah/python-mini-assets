import pytesseract
from PIL import Image

# Tesseract ka exact path manually set karo
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def image_to_text(image_file):
    text = pytesseract.image_to_string(Image.open(image_file))
    with open("image_text.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(text)
    
    print("Extracted text saved to image_text.txt")

image_to_text("screenshot.png")
