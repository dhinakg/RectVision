import cv2
import numpy as np

img = "test.png"
squareList = []

image = cv2.imread(img, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
im2, contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

(screen_h, screen_w) = image.shape[:2] # Gets width and height of screen so that cv2 won't draw a rectangle around the image's frame

for i in range(len(contours)):
    epsilon = 0.1*cv2.arcLength(contours[i], True)
    shape = cv2.approxPolyDP(contours[i], epsilon, True)

    if len(shape == 4):
        x, y, w, h = cv2.boundingRect(contours[i]) # x is top left (x) coordinate, y is top left (y) coordinate, w is length, h is width
        if ((h != screen_h) or (w != screen_w)):
            squareList.append(contours[i])

x, y, w, h = cv2.boundingRect(squareList[0]) # x is top left (x) coordinate, y is top left (y) coordinate, w is length, h is width
length = w
width = h

cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
print("The length is " + str(length/96) + " inches") # windows has 96 dpi by default
print("The width is " + str(width/96) + " inches")

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()
