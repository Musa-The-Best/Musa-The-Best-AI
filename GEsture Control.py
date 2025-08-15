import cv2
import numpy as np
import time
import os
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: The camera is not opened")
    exit()
filters = ["normal", "grayscale", "sepia", "negative", "blur"]
current_filter = "normal"
if not os.path.exists("captured_images"):
    os.makedirs("captured_images")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image")
        break
    frame = cv2.flip(frame, 1)
    filtered_frame = frame.copy()
    if current_filter == "grayscale":
        filtered_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        filtered_frame = cv2.cvtColor(filtered_frame, cv2.COLOR_GRAY2BGR)
    elif current_filter == "sepia":
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        filtered_frame = cv2.transform(frame, kernel)
        filtered_frame = np.clip(filtered_frame, 0, 255).astype(np.uint8)
    elif current_filter == "negative":
        filtered_frame = cv2.bitwise_not(frame)
    elif current_filter == "blur":
        filtered_frame = cv2.GaussianBlur(frame, (15, 15), 0)
    cv2.putText(filtered_frame, f"filter: {current_filter}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Filtered Frame", filtered_frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('1'):
        current_filter = "normal"
    elif key == ord('g'):
        current_filter = "grayscale"
    elif key == ord('s'):
        current_filter = "sepia"
    elif key == ord('n'):
        current_filter = "negative"
    elif key == ord('b'):
        current_filter = "blur"
    elif key == ord("c"):
        timestamp = time.strftime("%y%m%d-%H%M%S")
        filename = f"captured_images/capture_{timestamp}_{current_filter}.jpg"
        cv2.imwrite(filename, filtered_frame)
cap.release()
cv2.destroyAllWindows()
