import cv2 as cv
import time
import numpy as py
import pygame

# Translate Frame
def trans(Frame,x,y):
    m = py.float32([[1,0,x],[0,1,y]])
    c_img = cv.warpAffine(Frame,m,(Frame.shape[1],Frame.shape[0]))
    return c_img
# - x = left , +x = right 
# -y = down , +y = up

# resize Frame
def resize(Frame,scale):
    width = int(Frame.shape[1]*scale)
    height = int(Frame.shape[0]*scale)
    dimension = (width,height)
    return cv.resize(Frame,dimension,interpolation=cv.INTER_AREA)


# recolor Frame
def recolor(Frame):
    Frame[:] += 30
    return Frame

pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\Admin\OneDrive\Pictures\audio1.mp3")
pygame.mixer.music.play()

capture = cv.VideoCapture(r"C:\Users\Admin\OneDrive\Pictures\garp.mp4")

while(capture.isOpened()):
    time.sleep(0)
    isTrue,Frame = capture.read()
    r_Frame = resize(Frame,0.5)
    r_Frame = trans(r_Frame,-100,50)
    r_Frame = recolor(r_Frame)
    cv.imshow("live",r_Frame)

    if(cv.waitKey(20) & 0xFF == ord("d")):
        break
capture.release()
cv.destroyAllWindows()  
