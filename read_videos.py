import cv2 as cv

# cv.VideoCapture(0)  # captures first webcam


capture = cv.VideoCapture("Videos/rabbit.mp4")
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)  # displays individual frame
    if cv.waitKey(20) & 0xFF == ord('q'):  # break out from infinite loop
        break
capture.release()
cv.destroyAllWindows()
