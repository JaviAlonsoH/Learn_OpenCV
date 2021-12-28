import cv2
import numpy as np

print("Program started")

# capturing image

img = cv2.imread("./res/ia.jpg")
print(img.shape)
kernel = np.ones((5, 5), np.uint8)

cv2.imshow("Output", img)

# BASIC FUNCTIONS #

# resize
imgResize = cv2.resize(img, (1000, 500))

# crop
imgCropped = img[0:200, 200:500]

# image to gray
imgToGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur effect
imgBlur = cv2.GaussianBlur(img, (7,7), 0)

# canny effect (edges)
imgCanny = cv2.Canny(img, 100, 100)

# dialation (increase edges)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

# erosion (edges)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Image Resized", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.imshow("Gray image", imgToGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialation image", imgDialation)
cv2.imshow("Erosion image", imgEroded)


cv2.waitKey(0)
