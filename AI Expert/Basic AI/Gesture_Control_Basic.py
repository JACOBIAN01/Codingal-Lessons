import cv2
import numpy as np

#Setup Webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera Issue")
    exit()

while True:

    ret,frame= cap.read()

    if not ret:
        print("Failed to Capture Image")
        break

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_skin_tone = np.array([0,20,70],dtype=np.uint8)
    upper_skin_tone = np.array([20,255,255],dtype=np.uint8)

    mask = cv2.inRange(hsv,lower_skin_tone, upper_skin_tone)
    result = cv2.bitwise_and(frame,frame,mask=mask)

    contours ,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if contours:

        max_contour = max(contours,key=cv2.contourArea)

        if(cv2.contourArea(max_contour)>500):
            x,y,w,h = cv2.boundingRect(max_contour)
            cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,0),2)


    cv2.imshow("Original Frame",frame)
    cv2.imshow("Result Frame",result)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





