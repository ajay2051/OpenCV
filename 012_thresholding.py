# Thresholding is binarization of image
import cv2 as cv

img = cv.imread("Photos/cute_krishna.jpg")
cv.imshow("Cute Krishna", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholding", thresh)

threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Inverse Thresholding", thresh_inverse)

# Adaptive Threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow("Adaptive Thresholding", adaptive_thresh)


cv.waitKey(0)
