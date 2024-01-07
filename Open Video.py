# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:13:11 2023

@author: ATHUL AKSHAY
"""
import cv2
vid=cv2.VideoCapture(0)
while vid.isOpened():
    ret,frame=vid.read()
    
    cv2.imshow('video',frame)
    if cv2.waitKey(1)==ord('e'):
        break
    
