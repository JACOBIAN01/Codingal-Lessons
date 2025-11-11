#############################################
# GESTURE-BASED SCROLL CONTROL - IMPLEMENTATION
#############################################

import cv2
import time
import pyautogui
import mediapipe as mp

# ---------------------------------------------------
# STEP 2: Initialize hand tracking model
# ---------------------------------------------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# ---------------------------------------------------
# STEP 3: Configuration Values
# ---------------------------------------------------
SCROLL_SPEED = 100        # Amount to scroll per gesture
SCROLL_DELAY = 1.0        # Seconds between scroll actions
CAM_WIDTH, CAM_HEIGHT = 640, 480

# ---------------------------------------------------
# STEP 4: Gesture Detection Function
# ---------------------------------------------------
def detect_gesture(landmarks, handedness):
    """
    Determines whether to scroll up or down based on finger extension.
    """
    if not landmarks:
        return "none"

    # Tips of fingers: [Thumb, Index, Middle, Ring, Pinky]
    finger_tips = [4, 8, 12, 16, 20]
    finger_states = []

    # For all fingers except thumb
    for tip in finger_tips[1:]:
        if landmarks[tip].y < landmarks[tip - 2].y:
            finger_states.append(1)  # finger open
        else:
            finger_states.append(0)  # finger closed

    # Handle thumb (different for left/right hand)
    if handedness == "Right":
        if landmarks[finger_tips[0]].x > landmarks[finger_tips[0] - 1].x:
            finger_states.insert(0, 1)
        else:
            finger_states.insert(0, 0)
    else:  # Left hand
        if landmarks[finger_tips[0]].x < landmarks[finger_tips[0] - 1].x:
            finger_states.insert(0, 1)
        else:
            finger_states.insert(0, 0)

    total_fingers = sum(finger_states)

    if total_fingers == 5:
        return "scroll_up"
    elif total_fingers == 0:
        return "scroll_down"
    else:
        return "none"

# ---------------------------------------------------
# STEP 5: Webcam Setup
# ---------------------------------------------------
cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)

prev_time = 0
last_scroll_time = 0

# ---------------------------------------------------
# STEP 6: Main Loop
# ---------------------------------------------------
while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    gesture = "none"
    handedness_label = ""

    if results.multi_hand_landmarks:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            handedness_label = hand_handedness.classification[0].label
            gesture = detect_gesture(hand_landmarks.landmark, handedness_label)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            current_time = time.time()
            if current_time - last_scroll_time > SCROLL_DELAY:
                if gesture == "scroll_up":
                    pyautogui.scroll(SCROLL_SPEED)
                    last_scroll_time = current_time
                elif gesture == "scroll_down":
                    pyautogui.scroll(-SCROLL_SPEED)
                    last_scroll_time = current_time

    # FPS Calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if curr_time != prev_time else 0
    prev_time = curr_time

    # Overlay info
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.putText(frame, f"Hand: {handedness_label}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
    cv2.putText(frame, f"Gesture: {gesture}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2)

    cv2.imshow("🖐️ Gesture Scroll Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ---------------------------------------------------
# STEP 7: Cleanup
# ---------------------------------------------------
cap.release()
cv2.destroyAllWindows()
