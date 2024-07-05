import cv2 as cv
import numpy as np

img = cv.imread('Photos/cute_krishna.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces = haar_cascade.detectMultiScale(gray, 1.3, 5)  # change min_neighbours value to find correct number of faces

print(f"Found {len(faces)} faces")

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv.imshow('Detected Face', img)

cv.waitKey(0)
