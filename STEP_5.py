import cv2 as cv
import time
import numpy as py
import pygame

def rotate(Frame):     # 2nd method to rotate Frame by only (90,270,180) angle both clock & anti_clock wise , advantage no edge croped
    rotate_img = cv.rotate(Frame,cv.ROTATE_90_COUNTERCLOCKWISE)
    return rotate_img

def rotate1(Frame,centre,angle):   # 1st method to rotate any angle , disadvantage is edge will be croped
    m = cv.getRotationMatrix2D(centre,angle,1.0)
    r_img = cv.warpAffine(Frame,m,(Frame.shape[1],Frame.shape[1]))
    return r_img

def resize(Frame,scale):
    width = int(Frame.shape[1]*scale)
    height = int(Frame.shape[0]*scale)
    dimension = (width,height)
    return cv.resize(Frame,dimension,interpolation=cv.INTER_AREA)

def recolor(Frame):
    Frame[:] += 70
    return Frame

pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\Admin\OneDrive\Pictures\audio1.mp3")
pygame.mixer.music.play()

capture = cv.VideoCapture(r"C:\Users\Admin\OneDrive\Pictures\garp.mp4")

while(capture.isOpened()):
    time.sleep(0)
    isTrue,Frame = capture.read()
    r_Frame = resize(Frame,0.5)
   # r_Frame = rotate1(r_Frame,(r_Frame.shape[1]//2,r_Frame.shape[0]//2),90)
    r_Frame = rotate(r_Frame)
   # r_Frame = cv.cvtColor(r_Frame,cv.COLOR_BGR2HLS)
    r_Frame = recolor(r_Frame)
    cv.imshow("live",r_Frame)

    if(cv.waitKey(20) & 0xFF == ord("d")):
        break
capture.release()
cv.destroyAllWindows()  
