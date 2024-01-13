import cv2
import numpy as np
Face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture('http://192.168.137.111:4747/video')
cpt=0
while(True):
   ret,frame=cap.read()
   faces=Face_cascade.detectMultiScale(frame,1.2,4)
   for(x,y,w,h) in faces:
      crop=frame[y:y+h,x:x+w]
      cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
   cv2.imshow("frame",frame)
   cpt+=1
   k=cv2.waitKey(1)&0xFF
   if k==ord('q'):
            break


