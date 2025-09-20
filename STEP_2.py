import cv2 as cv
import numpy as np

# blank or black image creating ...
img = np.zeros((500,500,3),dtype="uint8")
cv.imshow("blank_img",img)

# paint image in certain colour ...
img [:] = 0,144,255
cv.imshow("clorour",img)

# paint at particular portion (SQUARE) ...
img [200:300 , 200:300] = 0,0,0
cv.imshow("portion_colour",img)

# paint at particular portion (RECTANGLE) ...
img [350:400 , 200:300] = 0,0,0
cv.imshow("portion_colour",img)

# using reactangle function ...
cv.rectangle(img ,(100,450),(400,100),(2,56,234),thickness=-1)
cv.imshow("rectangle",img)

# using circle function ...
cv.circle(img,(250,350),50,(0,0,0),thickness=-1)
cv.imshow("circle",img)

# draw line ...
cv.line(img,(250,0),(250,350),(255,255,255),thickness=2)
cv.imshow("line",img)

# write text on image ...
cv.putText(img,"IAM LOKI",(0,50),cv.FONT_HERSHEY_TRIPLEX,1.0,(140,10,0),thickness=2)
cv.imshow("text",img)

cv.waitKey(0)
