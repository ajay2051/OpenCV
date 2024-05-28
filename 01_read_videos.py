import cv2 as cv

from rescale import rescale_frame


# cv.VideoCapture(0)  # captures first webcam

def rescale_video_frame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture("Videos/rabbit.mp4")
while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_video_frame(frame, 0.5)
    # cv.imshow("Video Resized", frame_resized)
    cv.imshow('Video', frame)  # displays individual frame
    if cv.waitKey(20) & 0xFF == ord('q'):  # break out from infinite loop
        break
capture.release()
cv.destroyAllWindows()
