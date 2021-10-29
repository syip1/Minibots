import cv2
import numpy as np
from time import sleep

cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows, cols, _ = frame.shape

centre = int(cols/2)
x_mid = centre # Avoids a crash if no object is detected

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Reset x_mid to centre of the screen if no object detected
    x_mid = centre

    #Red Colour
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        x_mid = int((2*x + w)/2)
        break

        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)

    cv2.line(frame, (x_mid, 0), (x_mid, 480), (0,255,0),2)

    cv2.imshow("Frame", frame)
    #cv2.imshow("mask", red_mask) #show what the computer sees

    key = cv2.waitKey(1)

    if key == 27:
        break

    #Output if the object is to the left or right of the centre
    if x_mid < centre:
        print("Go Left")
    elif x_mid > centre:
        print("Go Right")

    sleep(0.5)

cap.release()
cv2.destroyAllWindows()
