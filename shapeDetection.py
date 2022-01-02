import cv2
import numpy as np

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvaliable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvaliable:
        for x in range (0, rows):
            for y in range (0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, None)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0]))
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor()


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 400:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 1)
            per = cv2.arcLength(cnt, True)
            # print(per)
            approx = cv2.approxPolyDP(cnt, 0.05 * per, True)
            print(len(approx))
            objCorners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCorners == 3:
                ObjectType = "Tri"
            elif objCorners == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.5:
                    ObjectType = "Square"
                else:
                    ObjectType = "Rectangle"
            elif objCorners > 4:
                ObjectType =  "Circle"
            else:
                ObjectType = "None"



            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, ObjectType,
                        (x+(w//2) - 10, y+(h//2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 0), 1)




img = cv2.imread("./res/shapes2.jpg")
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

imgBlank = np.zeros_like(img)
cv2.imshow("Original", img)
cv2.imshow("Grey", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Blank", imgBlank)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Contours", imgContour)

cv2.waitKey(0)