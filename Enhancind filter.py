import numpy as np
import matplotlib.pyplot as plt
import cv2

def display_image(title, image):
    """Utility function to display an image."""
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def apply_edge_detection(image, method="sobel", ksize=3, threshold1=100, threshold2=200):
    """Applies the selected edge detection method."""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if method == "sobel":
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=ksize)
        return cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))

    elif method == "canny":
        return cv2.Canny(gray_image, threshold1, threshold2)

    elif method == "laplacian":
        return cv2.Laplacian(gray_image, cv2.CV_64F).astype(np.uint8)

def apply_filter(image, filter_type="gaussian", ksize=5):
    """Applies the selected filter to the image."""
    if filter_type == "gaussian":
        return cv2.GaussianBlur(image, (ksize, ksize), 0)
    elif filter_type == "median":
        return cv2.medianBlur(image, ksize)

def interactive_edge_detection(image_path):
    """Interactive activity for edge detection and filtering."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image")
        return
    
    while True:
        print("\nOptions:")
        print("1. Apply Filter")
        print("2. Detect Edges")
        print("3. Display Original")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            filter_type = input("Enter filter type (gaussian/median): ").lower()
            ksize = int(input("Enter kernel size (odd number): "))
            filtered = apply_filter(image, filter_type, ksize)
            display_image(f"{filter_type.capitalize()} Filter", filtered)
            
        elif choice == '2':
            method = input("Enter method (sobel/canny/laplacian): ").lower()
            if method == 'canny':
                t1 = int(input("Enter threshold 1: "))
                t2 = int(input("Enter threshold 2: "))
                edges = apply_edge_detection(image, method, threshold1=t1, threshold2=t2)
            else:
                edges = apply_edge_detection(image, method)
            display_image(f"{method.capitalize()} Edges", edges)
            
        elif choice == '3':
            display_image("Original Image", image)
            
        elif choice == '4':
            break
            
        else:
            print("Invalid choice. Please try again.")

# Example usage:
# interactive_edge_detection('your_image.jpg')