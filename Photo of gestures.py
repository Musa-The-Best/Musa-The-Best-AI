import cv2
import numpy as np
import mediapipe as mp
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Define finger indices
thumb_tip = 4
index_tip = 8
middle_tip = 12
ring_tip = 16
pinky_tip = 20

# Start webcam
cap = cv2.VideoCapture(0)

# Variables for FPS calculation
pTime = 0
cTime = 0

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Flip image for natural interaction
    image = cv2.flip(image, 1)

    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and find hands
    results = hands.process(image_rgb)

    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get fingertip positions
            h, w, c = image.shape
            landmarks = []
            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append((cx, cy))

            if len(landmarks) > 20:
                # Example gesture recognition: Distance between thumb and index finger
                x1, y1 = landmarks[thumb_tip]
                x2, y2 = landmarks[index_tip]
                distance = np.hypot(x2 - x1, y2 - y1)

                cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.circle(image, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
                cv2.circle(image, (x2, y2), 5, (0, 0, 255), cv2.FILLED)

                # Gesture: Pinch
                if distance < 40:
                    cv2.putText(image, "Pinch Detected", (50, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # FPS calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(image, f'FPS: {int(fps)}', (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display the image
    cv2.imshow('Hand Gesture Recognition', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
