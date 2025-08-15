import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import time
CLICK_THRESHOLD = 40
DOUBLE_CLICK_INTERVAL = 0.3
SCROLL_THRESHOLD = 40
SCROLL_SPEED = 2
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
screen_width, screen_height = pyautogui.size()
def get_gesture(hand_landmarks, handedness):
    """
    Detects the basic hand gestures based on pre-defined rules.
    """
    gestures = {
        "click": False,
        "scroll": None,
        "pointer": None
    }
    landmarks = hand_landmarks.landmark
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    gestures["pointer"] = (index_finger_tip.x, index_finger_tip.y)
    if abs(index_finger_tip.x - middle_finger_tip.x) < 0.02 and abs(index_finger_tip.y - middle_finger_tip.y) < 0.02:
        gestures["click"] = True
    if middle_finger_tip.y < index_finger_tip.y - 0.05:
        gestures["scroll"] = "up"
    elif middle_finger_tip.y > index_finger_tip.y + 0.05:
        gestures["scroll"] = "down"
    return gestures
cap = cv2.VideoCapture(0)
cap.set(3, CAMERA_WIDTH)
cap.set(4, CAMERA_HEIGHT)
last_click_time = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    if result.multi_hand_landmarks:
        for hand_landmarks, hand_handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gestures = get_gesture(hand_landmarks, hand_handedness)
            if gestures["pointer"]:
                pointer_x = gestures["pointer"][0] * screen_width
                pointer_y = gestures["pointer"][1] * screen_height
                pyautogui.moveTo(pointer_x, pointer_y)
            if gestures["click"]:
                current_time = time.time()
                if current_time - last_click_time < DOUBLE_CLICK_INTERVAL:
                    pyautogui.doubleClick()
                else:
                    pyautogui.click()
                last_click_time = current_time
            if gestures["scroll"] == "up":
                pyautogui.scroll(SCROLL_SPEED)
            elif gestures["scroll"] == "down":
                pyautogui.scroll(-SCROLL_SPEED)

    cv2.imshow("Hand Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()