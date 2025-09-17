import cv2 as cv
import time
import pygame
import numpy as py
import matplotlib.pyplot as plt

# resize frame
def resize(Frame,scale):
    width = int(Frame.shape[1]*scale)
    height = int(Frame.shape[0]*scale)
    dimension = (width,height)

    return cv.resize(Frame,dimension,interpolation=cv.INTER_AREA)


# reading images
img = cv.imread(r'C:\Users\Admin\OneDrive\Pictures\spiderman.png')
r_img = resize(img,0.5)
cv.imshow('black_lake',r_img)

# blank image
blank = py.zeros((r_img.shape[0],r_img.shape[1],3),dtype='uint8')
cv.imshow("blank",blank)

# blur readed image
rb_img = cv.GaussianBlur(r_img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("blured_img",rb_img)

# canny edge detection
canny_img = cv.Canny(rb_img,125,175)
cv.imshow("Canny_img",canny_img)

# finding controus
contours, hirerarchy = cv.findContours(canny_img,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print("no of contours found : ",len(contours))

# drawing controus on blank image
draw_contrours = cv.drawContours(blank,contours,58,(160,45,255),1)
cv.imshow("drawn_contours",draw_contrours)

cv.waitKey(0)
cv.destroyAllWindows()