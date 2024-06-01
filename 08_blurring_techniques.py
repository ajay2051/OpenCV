import cv2 as cv

img = cv.imread("Photos/cute_krishna.jpg")
cv.imshow("Cute Krishna", img)

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow("Average", average)

# Gaussian Blur
blur = cv.GaussianBlur(img, (3, 3), 0, 0)
cv.imshow("Blur", blur)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 9, 9, 9)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
