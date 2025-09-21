import cv2 as cv
import numpy as py
import random as rand
import time


def DirectionArrow(ct):
    x, y, w, h = cv.boundingRect(ct)
    cx, cy = x + w // 2, y + h // 2   # find center of bounding box of arrow

    # Find tip point by checking each point which is have long distance from center of box
    max_dist = 0
    tip = None
    for point in ct:
        px, py = point[0]
        dist = (px - cx) ** 2 + (py - cy) ** 2
        if dist > max_dist:
            max_dist = dist
            tip = (px, py)

    # Decide direction based on tip position from center
    if abs(tip[0] - cx) > abs(tip[1] - cy):
        if tip[0] < cx:            # detcect left or right by comparing x coordinate value of tip and center
            return "LEFT"
        else:
            return "RIGHT"
    else:
        if tip[1] < cy:            # detcect up or down by comparing y coordinate value of tip and center
            return "UP"
        else:
            return "DOWN"


    

# main program
capture = cv.VideoCapture(0)
while(capture.isOpened()):
    
    # Capture Live Frame
    isTrue,r_Frame = capture.read()
    dimension = (r_Frame.shape[1],r_Frame.shape[0])
    re_Frame = cv.resize(r_Frame,(int(r_Frame.shape[1]*0.6),int(r_Frame.shape[0]*0.6)),dimension)
    cv.rectangle(re_Frame,(100,350),(650,100),(0,255,0),thickness=1)
    Frame = re_Frame[100:350,100:650]

    # Convert Frame to Grayscale
    blank_img = py.zeros((Frame.shape[0], Frame.shape[1], 3),dtype='uint8')
    gray_img = cv.cvtColor(Frame,cv.COLOR_BGR2GRAY)
    # cv.imshow("gray_img",gray_img)

    
    # Detect the Edges by Canny
    canny = cv.Canny(gray_img,125,175)
    countours,hierarchies = cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    draw_countour = cv.drawContours(blank_img,countours,-1,(255,255,255),1)
    # cv.imshow("blank_countours",draw_countour)


    for ct in countours:
        area = cv.contourArea(ct)
        if(area > 1000):
            approx = cv.approxPolyDP(ct, 0.03 * cv.arcLength(ct, True), True)

            if(len(approx)>=6):

                direction = DirectionArrow(ct)
                x, y, w, h = cv.boundingRect(ct)
                cv.rectangle(Frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv.putText(Frame, direction, (x, y - 10),
                cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                
    cv.imshow("live",re_Frame)            

    if(cv.waitKey(20) & 0xFF == ord('d')):
        break
capture.release()
cv.destroyAllWindows() 