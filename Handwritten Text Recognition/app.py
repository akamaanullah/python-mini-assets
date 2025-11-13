from PIL import Image
import easyocr
import cv2
import numpy as np

# Load image using OpenCV for preprocessing
img = cv2.imread('wa.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding for better contrast
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Save preprocessed image
cv2.imwrite('processed_image.jpg', thresh)

# Now, use easyocr on the processed image
reader = easyocr.Reader(['en'])
result = reader.readtext('processed_image.jpg')
print(result)
