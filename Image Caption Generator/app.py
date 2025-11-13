# from transformers import BlipProcessor, BlipForConditionalGeneration
# from PIL import Image

# # Load pre-trained model and processor
# processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
# model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# def generate_caption(image_path):
#     raw_image = Image.open(image_path).convert("RGB")
#     inputs = processor(raw_image, return_tensors="pt")
#     out = model.generate(**inputs)
#     caption = processor.decode(out[0], skip_special_tokens=True)
#     return caption

# print(generate_caption("img.jpg"))

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Load pre-trained model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Function to generate detailed captions
def generate_detailed_caption(image_path):
    raw_image = Image.open(image_path).convert("RGB")
    inputs = processor(raw_image, return_tensors="pt")

    # Get a general caption
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    
    # You can add specific code here to break down the caption further or use object detection models
    # Example: Apply an object detection model here to detect specific features (eyes, hair, etc.)
    # Then, use this information to append or update the caption.

    return caption

# Example of using the function
print(generate_detailed_caption("img.jpg"))
