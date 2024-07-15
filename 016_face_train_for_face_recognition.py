import os
import cv2 as cv
import numpy as np

people = ['cena', "rock"]

# p = []
#
# for i in os.listdir("/home/ajay/Desktop/OpenCV/Photos"):
#     p.append(i)

features = []  # list of faces
labels = []  # list of labels of that faces

DIR = r"/home/ajay/Desktop/OpenCV/Photos/"

haar_cascade = cv.CascadeClassifier('haar_face.xml')


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces_rect:
                face = gray[y:y + h, x:x + w]
                features.append(face)
                labels.append(label)


create_train()

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer.create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)
face_recognizer.save('face_train.yml')  # To use this function in another file
np.save('features.npy', features)
np.save('labels.npy', labels)
