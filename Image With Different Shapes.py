# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:23:31 2023

@author: ATHUL AKSHAY
"""

import cv2
img=cv2.imread(r"C:\Users\ATHUL AKSHAY\Downloads\Car.jpg")
img

img=cv2.resize(img,(500,600))
img.shape
color=(135,206,235)
color2=(255,87,51)
cv2.rectangle(img,(300,300),(500,500),color,2)
cv2.circle(img,(250,250),50,color,10)
cv2.line(img,(150,250),(350,200),color2,4)
font=cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img, 'CarNew', (100,100), font,3,color,10)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()