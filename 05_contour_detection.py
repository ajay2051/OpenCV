# Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity.
# The contours are a useful tool for shape analysis and object detection and recognition.

import cv2 as cv
import numpy as np

img = cv.imread("Photos/cute_krishna.jpg")
cv.imshow("Cute Krishna", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)

# Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Canny
# Detecting contour on canny reduces the length of contours by significant numbers
canny = cv.Canny(blur, 100, 200)
cv.imshow("Canny", canny)

# Threshold looks into an image and binarize that image
ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

# Contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# contours returns list
print(f"Number of contours: {len(contours)}")

# Draw contours on blank image
cv.drawContours(blank, contours, -1, (0, 255, 0), 3)  # -1 specifies all
cv.imshow("Contours Passed", blank)

cv.waitKey(0)
