from transformers import pipeline
from PIL import Image

# Initialize the text-to-image generation pipeline
generator = pipeline("image-generation", model="CompVis/stable-diffusion-v1-4-original")

def generate_image_from_text(text):
    # Generate image from text
    generated_images = generator(text)
    image = Image.open(generated_images[0]['image'])
    return image

# Example usage: generate an image based on a text prompt
image = generate_image_from_text("A painting of a cat playing piano")
image.show()
