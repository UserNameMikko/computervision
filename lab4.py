import detect_module_lab4
import imutils
import cv2
from array import *


def figType(figures, arrays):
    if figures == "triangle":
        arrays[0] += 1
    elif figures == "rectangle":
        arrays[1] += 1
    elif figures == "circle":
        arrays[2] += 1
    elif figures == "pentagon":
        arrays[3] += 1
    elif figures == "hexagon":
        arrays[4] += 1
    elif figures == "square":
        arrays[5] += 1

image = cv2.imread('lab4_image.png')
cv2.imshow('FirstImage', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 225, 255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow('image1', thresh)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
d = detect_module_lab4.Detector()
arr = array('i', [0, 0, 0, 0 ,0, 0])
for c in cnts:
     M = cv2.moments(c)
     cX = int((M["m10"] / M["m00"]))
     cY = int((M["m01"] / M["m00"]))
     shape = d.detect(c)
     figType(shape, arr)
     cv2.drawContours(image, [c], -1, (0, 0, 0), 2)
     cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
     cv2.putText(image, shape, (cX, cY),cv2.FONT_HERSHEY_SIMPLEX,0.5, (168, 60,
    50), 2)
# show the output image
cv2.imshow("Image", image)
print("Figures found:")
print("Triangle:" + str(arr[0]))
print("Rectangle:" + str(arr[1]))
print("Circle:" + str(arr[2]))
print("Pentagon:" + str(arr[3]))
print("Hexagon:" + str(arr[4]))
print("Square:" + str(arr[5]))
cv2.waitKey(0)