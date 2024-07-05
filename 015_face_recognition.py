import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['cena', "rock"]

# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.read('face_train.yml')

img = cv.imread('/home/ajay/Desktop/OpenCV/Photos/cena/download.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('cena', gray)

# Detect the face in image
faces = haar_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    faces = gray[y:y + h, x:x + w]
    label, confidence = face_recognizer.predict(faces)
    print(f'label: {people[label]}, confidence: {confidence}')
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.rectangle(img, (x, y), (x+y, w+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)
