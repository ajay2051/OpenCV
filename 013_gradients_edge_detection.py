import cv2 as cv
import numpy as np

img = cv.imread("Photos/cute_krishna.jpg")
cv.imshow("Cute Krishna", img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Sobel
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=3)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=3)
combine_sobel = cv.bitwise_or(sobel_x, sobel_y)


cv.imshow("Sobel X", sobel_x)
cv.imshow("Sobel Y", sobel_y)

cv.imshow("Combined Sobel", combine_sobel)

canny = cv.Canny(gray, 100, 200)
cv.imshow("Canny", canny)

cv.waitKey(0)
