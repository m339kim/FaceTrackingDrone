from utilis import *
import cv2

myDrone = initTello()

# init variables
w, h = 360, 240
pid = [0.5, 0.5, 0]
pError = 0
startCounter = 0  # flight = 1, no flight = 0

while True:
    # Flight
    if startCounter == 0:
        myDrone.takeoff()
        startCounter = 1

    img = telloGetFrame(myDrone, w, h)
    img, info = findFace(img)
    pError = trackFace(myDrone, info, w, pid, pError)

    print(info[0][0]) # print center-x values
    cv2.imshow('Image', img)

    # Emergency stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
        break