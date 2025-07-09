import cv2
import numpy as np
import matplotlib.pyplot as plt
def display_image(title, image):
    plt.figure(figsize=(8,8))
    if len(image.shape)==2:
        plt.imshow(image, cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()

def interactive_edge_detection(image_path):
    image=cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return
    
    grayimg=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    display_image("Original Grayscale Image", grayimg)

    print("Select an option: ")
    print("1.Edge Detection")
    print("2.Edge Detection")
    print("3.Edge Detection")

    print("4.Gaussian Smoothing")
    print("5.Median Filtering")
    print("6.exit")

    while True:
        choice=input("Enter your choice(1-6): ")

        if choice=="1":
            sobelx=cv2.Sobel(grayimg,cv2.CV_64F,1,0,ksize=3)
            sobely=cv2.Sobel(grayimg,cv2.CV_64F,0,1,ksize=3)
            combined_sobel=cv2.bitwise_or(sobelx.astype(np.uint8),sobely.astype(np.uint8))
            display_image("Sobel image",combined_sobel)

        elif choice =="2":
            print("Adjust thresholds for Canny(Default: 100 and 200)")
            lower_thresh=int(input("Enter lower threshold: "))
            upper_thresh=int(input("Enter upper threshold: "))
            edges=cv2.Canny(grayimg,lower_thresh,upper_thresh)
            display_image("Canny Edge Detecton",edges)

        elif choice=="3":
            laplacian=cv2.Laplacian(grayimg,cv2.CV_64F)
            display_image("Laplacian Edge Detection",np.abs(laplacian).astype(np.uint8))

        elif choice == "4":
            print("adjust kernel size for Gaussian Blur(Must be odd and default is 5)")
            kernal_size=int(input("Enter kernal size: "))
            blurred=cv2.GaussianBlur(image,(kernal_size,kernal_size),0)
            display_image("Gaussian Smoothed Image", blurred)
        
        elif choice == "5":
            print("adjust kernel size for Gaussian Blur(Must be odd and default is 5)")
            kernal_size=int(input("Enter kernal size: "))
            medianblurred=cv2.medianBlur(image,kernal_size)
            display_image("Median Filtered Image", medianblurred)
        elif choice=="6":
            print("Exiting...")
            break
        else:print("Invaid choice. Please select a number between 1 to 6")

interactive_edge_detection("example.jpg")