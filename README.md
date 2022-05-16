# Face-tracking Drone

## Overview
The Face-tracking and movement following program detects a human face, then follows it along making corresponding transitions and rotations. Manually making such movements can be challenging, because there are just to many buttons to manipulate! This program is designed specifically to take off, detect the closest human face to the camera, then follow it along without requiring any manual control. 

## Tools Utilized
The program is fully facilitated in Python, and has implemented the OpenCV library to accurately identify the face, then used a PID controller to ensure smooth movements. A DJI Tello Drone and its SDK files were used over its Wi-fi connection for the development, and was created and tested in a MacOS environment. 

## How does it operate?
The mechanism implemented here is intuitive - we treat the camera view as a cartesian grid. By dividing the width and height of this grid, we will get a center point (x, y). Then, we set this center point as the desired fixed position of the detected face. 
<br /><br />
For instance, if the face is a bit off to the left, then the drone will rotate left to align the center of the face to match the center of the grid. 


![drone-project-01](https://user-images.githubusercontent.com/55883282/168631360-93da1228-aef5-48d4-8404-b8f106daf534.png)

