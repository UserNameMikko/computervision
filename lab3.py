import cv2
import imutils
import os

file_name = os.path.join(os.path.dirname(__file__), 'lab3_image.png')
assert os.path.exists(file_name)
image = cv2.imread(file_name)
cv2.imshow("Image", image)
cv2.rectangle(image, (525, 200), (625, 300), (0, 0, 0), thickness=cv2.FILLED)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()
for c in cnts:
    cv2.drawContours(output, [c], -1, (144, 144, 144), 3)
    text = "{} figures".format(len(cnts))
cv2.circle(output, (25, 625), 5, (0, 0, 0), -1)
cv2.putText(output, "1042 Vasily Andreevich Levashov", (10, 25), cv2.FONT_ITALIC, 0.7, (0, 0, 255), 2)
cv2.putText(output, text, (10, 50), cv2.FONT_ITALIC, 0.7, (255, 0, 0), 2)
cv2.imshow("Contours", output)
print("1042 Vasily Andreevich Levashov")
print(text)
cv2.waitKey(0)
