import cv2 as cv

img = cv.imread("Photos/cute_krishna.jpg")
cv.imshow("Cute Krishna", img)


def rescale_frame(frame, scale):
    """
    Can be used in images, videos, live_videos
    :param frame:
    :param scale:
    :return:
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_resolution(width, height):
    """
    Only used for live videos
    :param width:
    :param height:
    :return:
    """
    capture = cv.VideoCapture("Videos/rabbit.mp4")
    capture.set(3, width)
    capture.set(4, height)


cv.waitKey(0)
