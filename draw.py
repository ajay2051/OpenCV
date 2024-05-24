import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

cv.imshow("Blank", blank)

# Point the image a certain color
# blank[:] = 0, 255, 0
blank[200:300, 300:400] = 0, 0, 255
cv.imshow("Blank", blank)

# Draw Rectangle
cv.rectangle(blank, (0, 0),  (250, 250), (0, 255, 0), thickness=2)
cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=2)
cv.imshow("Rectangle", blank)

# Draw Circle
cv.circle(blank, (0, 0), 40, (0, 0, 255), thickness=-1)
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 255, 0), thickness=2)
cv.imshow("Circle", blank)

# Draw line
cv.line(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=2)
cv.imshow("Line", blank)

# Write Text on Image
cv.putText(blank, "Hello", (255, 255), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow("Text", blank)

img = cv.imread('Photos/cute_krishna.jpg')
cv.imshow('Cute Krishna', img)

cv.waitKey(0)
