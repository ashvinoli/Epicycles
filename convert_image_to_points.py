import numpy as np
import cv2

def get_points(image_name):
    im = cv2.imread(image_name)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    contours, hierarcy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    all_points= [complex(str(item[0][0])+"+"+str(item[0][1])+"j") for item in contours[1].tolist()]
    return all_points
    




