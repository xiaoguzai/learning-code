import cv2
from itertools import cycle
import random
import os

from cv2 import setWindowProperty
index = 0
img_list = []
file_dir = "D:\照片"
file_list = []
dir_list = os.listdir(file_dir)
for cur_file in dir_list:
    path = os.path.join(file_dir,cur_file)
    img_list.append(path)

index = 0
random.shuffle(img_list)

while 1:
    img = cv2.imread(img_list[index])
    img = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
    index = index+1
    cv2.namedWindow('myPicture',cv2.WINDOW_FULLSCREEN)
    cv2.moveWindow('myPicture',400,200)
    cv2.setWindowProperty('myPicture',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_AUTOSIZE)
    #cv2.resizeWindow('myPicture',1000,1000)
    cv2.imshow('myPicture',img)
    cv2.waitKey(120000)
cv2.destroyAllWindows()