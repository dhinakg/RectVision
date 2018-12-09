import cv2
import numpy as np

img = "test.png"
squareList = []

image = cv2.imread(img, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
im2, contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    epsilon = 0.1*cv2.arcLength(contours[i], True)
    shape = cv2.approxPolyDP(contours[i], epsilon, True)

    if len(shape == 4):
        squareList.append(contours[i])

x, y, w, h = cv2.boundingRect(squareList[1])
length = w
width = h

cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
print("The length is " + str(length))
print("The width is " + str(width))

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()
