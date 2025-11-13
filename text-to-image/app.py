from PIL import Image, ImageDraw, ImageFont

# Function to create an image with text
def create_image_with_text(text):
    img = Image.new('RGB', (500, 100), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((10, 25), text, font=font, fill=(0, 0, 0))
    img.save('text_image.png')
    img.show()

# Example usage
create_image_with_text("Hello, Muhammad Zain! How are you?")
