import sys
import imutils
import numpy as np
import cv2


im = cv2.imread('lab5_test_image.png')
resized = imutils.resize(im, width=600)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
# Определение порога яркости для бинаризации изображения
# thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)
# Использование порога яркости для бинаризации изображения
ret, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST,
cv2.CHAIN_APPROX_SIMPLE)
font = cv2.FONT_ITALIC
text = "0:Star, 1:Heart, 2:Lightning, 3:Cloud, 4:Triangle, 5:Rhombus, 6: Pointer"
#cv2.imshow('image' , im)
samples = np.empty((0, 100))
responses = []
keys = [i for i in range(48, 58)]
for cnt in contours:
    if cv2.contourArea(cnt) > 30:
        [x, y, w, h] = cv2.boundingRect(cnt)
        if h > 28:
            cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 0, 255), 2)
            roi = thresh[y:y + h, x:x + w]
            print(roi)
            roismall = cv2.resize(roi, (10, 10))
            cv2.imshow('roi', roismall)
            cv2.putText(resized, text, (5, 25), font, 0.5, (255, 0, 0), 2)
            cv2.imshow('norm', resized)
            key = cv2.waitKey(0)
            if key == 27: # (escape to quit)
                sys.exit()
            elif key in keys:
                responses.append(int(chr(key)))
                sample = roismall.reshape((1, 100))
                samples = np.append(samples, sample, 0)
responses = np.array(responses, np.float32)
responses = responses.reshape((responses.size, 1))
np.savetxt('generalsamples.data', samples)
np.savetxt('generalresponses.data', responses)