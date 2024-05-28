import cv2 as cv

img = cv.imread("Photos/cute_krishna.jpg")
cv.imshow("Cute Krishna", img)

# Converting image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur Image
blur = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=2)
cv.imshow("Dilated", dilated)

# Erode
erode = cv.erode(dilated, (3, 3), iterations=2)
cv.imshow("Eroded", erode)

# Resize image
resized = cv.resize(img, (800, 600), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

# Cropping
cropped = img[100:150, 100:150]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
