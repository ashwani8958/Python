#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:14:22 2020

@author: ashwani
"""

# https://realpython.com/face-recognition-with-python/

import cv2

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

def detect(gray, frame):
    
    # detect face
    faces = face_cascade.detectMultiScale(gray, 1.2, 20)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # In face detect eye
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 7)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        
        # In face detect smile
        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        for (sx,sy,sw,sh) in smile:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
            
    return frame


image = cv2.imread('../images/threeperson.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canvas = detect(gray, image)
cv2.imshow("FACE FOUND", canvas)

cv2.waitKey(0)