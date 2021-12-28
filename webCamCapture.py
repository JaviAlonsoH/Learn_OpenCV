import cv2

# capturing image

cap = cv2.VideoCapture(1)
# width
cap.set(3, 640)
# height
cap.set(4, 480)
# brightness
cap.set(10, 100)

while True:
    success, img = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

