import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the image
image = cv2.imread('example.jpg')

# Check if image loaded successfully
if image is None:
    print("Error: Could not load image")
    exit()

# Convert to RGB for displaying with matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Show the original image
plt.imshow(image_rgb)
plt.title("Original Image")
plt.show()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.show()

# Crop the image (assuming we want the region from 100:300, 200:400)
cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()

# Rotate the image by 45 degrees
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image (45 degrees)")
plt.show()

# Increase brightness by adding 50 to all pixel values
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image, brightness_matrix)
brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)  # Fixed typo in function name and color code
plt.imshow(brighter_rgb)
plt.title("Brighter Image")  # Fixed underscore to space
plt.show()

# Save the output images
cv2.imwrite('output_images/grayscale_image.jpg', gray_image)  # Fixed typo in function name
cv2.imwrite('output_images/cropped_image.jpg', cropped_image)
cv2.imwrite('output_images/rotated_image.jpg', rotated)
cv2.imwrite('output_images/brighter_image.jpg', brighter)

# Create output directory if it doesn't exist
import os
os.makedirs('output_images', exist_ok=True)