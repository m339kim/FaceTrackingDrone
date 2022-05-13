from djitellopy import Tello
import cv2
import numpy as np

def initTello():
    myDrone = Tello()
    myDrone.connect()
    # init translation values
    myDrone.for_back_velocity = 0
    myDrone.left_right_velocity = 0
    myDrone.up_down_velocity = 0
    myDrone.yaw_velocity = 0
    myDrone.speed = 0

    print(myDrone.get_battery())

    myDrone.streamoff()
    myDrone.streamon()

    return myDrone

def telloGetFrame(myDrone, w=360, h=240):
    # give the frame
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame, (w, h))
    return img

def findFace(img):
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert color image to mono
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 4)

    myFaceListCenter = []
    myFaceListArea = []

    # detect the closest face to the camera
    for (x, y, w, h) in faces:
        # 1. detect face
        # 2. find center x, center y, append to list of center x's and y's
        # 3. calculate area, append to list of area of faces
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cx = x + w//2
        cy = y + h//2
        myFaceListCenter.append([cx, cy])
        area = w * h
        myFaceListArea.append(area)

    # find index of largest area (ie. closest face to camera)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListCenter[i], myFaceListArea[i]]
                    # return largest face's center (x, y) coordinates, its area
    else:
        return img, [[0,0], 0]

def trackFace(myDrone, info, w, pid, pError):
    # pError = previous error

    # PID
    error = info[0][0] - w//2
    speed = pid[0] * error + pid[1] * (error-pError)
    speed = int(np.clip(speed, -100, 100)) # upper, lowerbound
    print(speed)

    if info[0][0] != 0:
        # then there is an actual coordinate of the face
        myDrone.yaw_velocity = speed
    else:
        # then set all the velocity to zero
        myDrone.for_back_velocity = 0
        myDrone.left_right_velocity = 0
        myDrone.up_down_velocity = 0
        myDrone.yaw_velocity = 0
        error = 0
    # send velocity values to myDrone
    if myDrone.send_rc_control:
        myDrone.send_rc_control(myDrone.left_right_velocity,
                                myDrone.for_back_velocity,
                                myDrone.up_down_velocity,
                                myDrone.yaw_velocity)
    return error
