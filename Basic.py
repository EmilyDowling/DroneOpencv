# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:37:10 2017

@author: Emily
"""
# Edited from the opencv tutorials
# Turn on camera and import numpy, opencv
import numpy as np
import cv2


cap = cv2.VideoCapture(0)

# Track a colour
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert each video frame from BGR to HSV colour
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define blue colour range (HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
     
    # Mask the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image ----- find out what bitwise is?
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    
# press 'esc' to close all
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# When everything done, close everything
# cap.release()
cv2.destroyAllWindows()