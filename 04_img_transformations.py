from email.mime import image

import cv2 as cv
import numpy as np

img = cv.imread("Photos/cute_krishna.jpg")
cv.imshow("Cute Krishna", img)


# Transformation
# Shifting images along X and Y axis
def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])  # img.shape[1] is width and img.shape[0] is height
    return cv.warpAffine(img, trans_mat, dimensions)


# -x ------> Left
# -y ------> Up
# x -------> Right
# y -------> Down


translated_img = translate(img, 100, 100)
cv.imshow("Translated Image", translated_img)


# Rotation
def rotate(img, angle, rotation_point=None):
    (height, width) = img.shape[:2]
    if rotation_point is None:
        rotation_point = (width // 2, height // 2)
    rot_mat = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rot_mat, dimensions)


rotated_img = rotate(img, 90)
cv.imshow("Rotated Image", rotated_img)
rotated_rotated = rotate(rotated_img, 45)
cv.imshow("Rotated Rotated Image", rotated_rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resized Image", resized)

# Flip
flip = cv.flip(img, 1)
cv.imshow("Flipped Image", flip)

# Crop
cropped = img[200:300, 300:400]
cv.imshow("Cropped Image", cropped)

cv.waitKey(0)
