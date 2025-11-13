from PIL import Image

# Function to convert image to ASCII art
def image_to_ascii(image_path):
    img = Image.open(image_path)
    img = img.convert('L')  # Convert to grayscale
    pixels = list(img.getdata())
    chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    ascii_str = ''.join([chars[pixel // 25] for pixel in pixels])
    ascii_str_len = len(ascii_str)
    ascii_str = [ascii_str[index: index + img.width] for index in range(0, ascii_str_len, img.width)]
    return "\n".join(ascii_str)

# Provide image path
print(image_to_ascii("qrcode.png"))
