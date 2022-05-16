# Face-tracking Drone

## Overview
![drone-project-01](https://user-images.githubusercontent.com/55883282/168631360-93da1228-aef5-48d4-8404-b8f106daf534.png)
<br />
The Face-tracking and movement following program detects a human face, then follows it along making corresponding transitions and rotations. Manually making such movements can be challenging, because there are just to many buttons to manipulate! This program is designed specifically to take off, detect the closest human face to the camera, then follow it along without requiring any manual control. 

## Tools Utilized
The program is fully facilitated in Python, and has implemented the OpenCV library to accurately identify the face, then used a PID controller to ensure smooth movements. A DJI Tello Drone and its SDK files were used over its Wi-fi connection for the development, and was created and tested in a MacOS environment. 

## How does it operate?
The mechanism implemented here is intuitive - we treat the camera view as a cartesian grid. By dividing the width and height of this grid by 2, we will get a center point (width/2, height/2), i.e. (x, y). Then, we set this center point as the desired fixed position of the detected face. 
<br /><br />
For instance, if the face is a bit off to the left, then the drone will rotate left to align the center of the face to match the center of the grid. The program sends new transition commands to the position of the face changes, in other words, tracks the face.

## Overcoming obstacles
Realistically, if we were to test the program outdoors, then there are high chances that it can detect multiple faces within its grid. This can lead to fatal errors of the program, since we cannot ensure that we are following one face along, but rather making random transitions to follow random faces. So, to resolve this issue, I created two arrays: `myFaceListCenter` and `myFaceListArea`. 
<br /><br />
`myFaceListCenter` is an array that stores the center point of the detected faces.
> Eg. `myFaceListCenter = [[15, 200], [100, 150], [230, 100]]`

`myFaceListArea` is an array that stores the area of the individual detected faces. (ie. area of the red rectangle)
> Eg. `myFaceListArea = [300, 280, 100, 270, 335]`

The goal was to identify exactly -one- face from the camera view, so this lead to a conclusion that that closest face detect should be the one to be followed by the drone. The largest item from the `myFaceListArea` meant that the face with that area is the closest to the camera, hence is the one that will be tracked. Also, to avoid confusion, the red rectangle was only drawn on the closest face to the camera to clearly let the users recognize the face that will be followed by the drone. 
<br /><br />
The code snippet for this configuration is as follows (from `utils.py`):<br />
<img width="627" alt="Screen Shot 2022-05-16 at 12 06 22 PM" src="https://user-images.githubusercontent.com/55883282/168638639-4cbdb2e7-a5c6-430e-8c4c-95c6a032b9f3.png">







