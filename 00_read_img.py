import cv2 as cv


def rescale_img_frame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Read Images
img = cv.imread('Photos/cute_krishna.jpg')
rescaled_img = rescale_img_frame(img, scale=0.5)
cv.imshow('Cute Krishna', img)
cv.imshow('Cute Krishna Rescaled', rescaled_img)
cv.waitKey(0)
