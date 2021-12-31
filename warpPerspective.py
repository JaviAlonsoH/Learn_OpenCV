import cv2
import numpy as np

img = cv2.imread("./res/cards.jpg")
width, height = 1024, 683
points = np.float32([[616, 247], [794, 457], [234, 423], [407, 666]])
points2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(points, points2)
imgOut = cv2.warpPerspective(img, matrix, (320, height))

cv2.imshow("Cards", img)
cv2.imshow("Out", imgOut)

cv2.waitKey(0)