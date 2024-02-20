from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import keras
import numpy as np
import os
import cvlib as cv
import cv2

model=load_model(r"C:\Users\ATHUL AKSHAY\Desktop\Machine Learning Projects\Hands Project\photo.h5")

vid=cv2.VideoCapture(0)
classes=['Akshay','Athul','Sreeshnu']
while(True):
    status,frame=vid.read()
    face,confidence=cv.detect_face(frame)
    for idx,f in enumerate(face):
        (startx,starty)=f[0],f[1]
        (endx,endy)=f[2],f[3]


        cv2.rectangle(frame,(startx,starty),(endx,endy),(255,0,0),2)
        face_crop=np.copy(frame[starty:endy,startx:endx])
        if (face_crop.shape[0])<10 or (face_crop.shape[1])<10:
            continue

        face_crop=cv2.resize(face_crop,(224,224))
        face_crop=face_crop/255
        face_crop=np.expand_dims(face_crop,axis=0)

        conf=model.predict(face_crop)[0]
        idx=np.argmax(conf)
        label=classes[idx]
        label='{}:{:.2f}%'.format(label,conf[idx]*100)
        y=starty-10 if starty-10>10 else starty+10


        cv2.putText(frame,label,(startx,y),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,0),2)


    cv2.imshow('Face Detection',frame)

    if cv2.waitKey(1)==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()