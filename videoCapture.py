import cv2

cap = cv2.VideoCapture("./res/video")

while True:
    success, img = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break