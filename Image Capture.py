import cv2
import os

folder=r'C:\Users\ATHUL AKSHAY\Desktop\Machine Learning Projects\SQL\Hands\Righthand\c'
if not os.path.exists(folder):
    os.makedirs(folder)

vid=cv2.VideoCapture(0)
vid.set(3,500)
vid.set(4,300)

num_of_images=100
for i in range(num_of_images):
    ret,frame=vid.read()
    cv2.imshow('Captured image',frame)
    outpath=os.path.join(folder, f'image{i+1}.jpg')
    cv2.imwrite(outpath,frame)
    cv2.waitKey(500)

vid.release()
cv2.destroyAllWindows()
print(f"{num_of_images} images captured and saved to {folder}")