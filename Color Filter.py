import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def display_image(path):
    img = Image.open(path)
    img.show()

def apply_filter(image_path, filter_type, intensity=50):
    image = cv2.imread(image_path)

    # Convert image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if filter_type == "red_tint":
        filtered_image = image.copy()
        filtered_image[:, :, 0] = filtered_image[:, :, 0] * 0
        filtered_image[:, :, 1] = filtered_image[:, :, 1] * 0
        filtered_image[:, :, 2] = cv2.addWeighted(filtered_image[:, :, 2], 1, filtered_image[:, :, 2], 0, intensity)
    
    elif filter_type == "green_tint":
        filtered_image = image.copy()
        filtered_image[:, :, 0] = filtered_image[:, :, 0] * 0
        filtered_image[:, :, 2] = filtered_image[:, :, 2] * 0
        filtered_image[:, :, 1] = cv2.addWeighted(filtered_image[:, :, 1], 1, filtered_image[:, :, 1], 0, intensity)

    elif filter_type == "blue_tint":
        filtered_image = image.copy()
        filtered_image[:, :, 1] = filtered_image[:, :, 1] * 0
        filtered_image[:, :, 2] = filtered_image[:, :, 2] * 0
        filtered_image[:, :, 0] = cv2.addWeighted(filtered_image[:, :, 0], 1, filtered_image[:, :, 0], 0, intensity)

    elif filter_type == "grayscale":
        filtered_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    elif filter_type == "sepia":
        kernel = cv2.transform(image, 
            [[0.272, 0.534, 0.131],
             [0.349, 0.686, 0.168],
             [0.393, 0.769, 0.189]])
        filtered_image = cv2.convertScaleAbs(kernel)

    else:
        filtered_image = image

    return filtered_image

def save_image(image):
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
    )
    if save_path:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(save_path, image)
        print(f"Image saved to {save_path}")

def display_color_options():
    print("Choose a filter by typing one of the options below:")
    print("red_tint - Adds a red tint")
    print("green_tint - Adds a green tint")
    print("blue_tint - Adds a blue tint")
    print("grayscale - Converts to grayscale")
    print("sepia - Adds sepia tone")
    print("none - No filter")

# GUI to select file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

if not file_path:
    print("No file chosen. Please select a valid option.")
    exit()

display_image(file_path)
display_color_options()

filter_type = input("Enter filter type (as shown): ")
if filter_type in ["red_tint", "green_tint", "blue_tint"]:
    intensity = int(input("Enter intensity (0–100): "))
else:
    intensity = 50

filtered = apply_filter(file_path, filter_type, intensity=intensity)

# Display filtered image
cv2.imshow("Filtered Image", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Prompt to save image
save = input("Would you like to save the output? (yes/no): ")
if save.lower() == "yes":
    save_image(filtered)
