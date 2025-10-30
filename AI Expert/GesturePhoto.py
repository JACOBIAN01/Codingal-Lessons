import cv2, mediapipe as mp, time

# 🖐️ Setup hand detection
hands = mp.solutions.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils

# 🎥 Open webcam
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Camera not found!")
    exit()

pinch_on = False

while True:
    ok, img = cam.read()
    if not ok: break
    img = cv2.flip(img, 1)
    h, w = img.shape[:2]

    result = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        draw.draw_landmarks(img, hand, mp.solutions.hands.HAND_CONNECTIONS)
        lm = hand.landmark

        # ✋ Get thumb and index tip positions
        tx, ty = int(lm[4].x * w), int(lm[4].y * h)
        ix, iy = int(lm[8].x * w), int(lm[8].y * h)

        # 📸 Check if thumb and index are close (pinch)
        if abs(tx - ix) < 30 and abs(ty - iy) < 30:
            if not pinch_on:
                pinch_on = True
                filename = f"photo_{int(time.time())}.jpg"
                cv2.imwrite(filename, img)
                cv2.putText(img, "📸 Photo Taken!", (40, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                print("Saved:", filename)
        else:
            pinch_on = False

        # 🟢 Draw finger tips
        cv2.circle(img, (tx, ty), 10, (0, 255, 0), -1)
        cv2.circle(img, (ix, iy), 10, (0, 255, 0), -1)

    cv2.imshow("Pinch to Take Photo", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
