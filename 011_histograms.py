# Histograms allows you to visualize the distribution of pixels intensity in an image.
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Read the image
img = cv.imread("Photos/cute_krishna.jpg")
cv.imshow("Cute Krishna", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

circle = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, (45, 456, 255), thickness=-1)
# cv.imshow("Circle", circle)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow("Mask", mask)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# Create the histogram plot
plt.figure()
plt.title("Gray Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])

# Save the plot as an image file instead of showing it
plt.savefig("gray_histogram1.png")
plt.close()

# Color Histogram
plt.title("Color Histogram")
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], (0, 256))
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.savefig("color_histogram.png")
plt.close()

cv.waitKey(0)
cv.destroyAllWindows()
