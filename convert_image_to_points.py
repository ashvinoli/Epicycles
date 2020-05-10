import numpy as np
import cv2

def get_points(image_name):
    im = cv2.imread(image_name)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    contours, hierarcy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    mega_amps = []
    for i in range(1,len(contours)):
        all_points= [complex(item[0][0],item[0][1]) for item in contours[i]]
        mega_amps.append(all_points)
    return mega_amps
    




