import cv2 as cv
import matplotlib.pyplot as plt

def resize(Frame,scale):
    width = int(Frame.shape[1]*scale)
    height = int(Frame.shape[0]*scale)
    dimension = (width,height)
    return cv.resize(Frame,dimension,interpolation=cv.INTER_AREA)

# reading image
img = cv.imread(r'C:\Users\Admin\OneDrive\Pictures\spiderman.png')
img = resize(img,0.4)
cv.imshow("original_img",img)
plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB))  # it show img in RGB format
plt.show()

# convert BGR to GRAY
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("BGR_to_GRAY",gray_img)

# convert BGR to LSV
lsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("BGR_to_LSV",lsv_img)

# convert BGR to HSV
hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("BGR_to_HSV",hsv_img)

# convert BGR to LAB
lab_img = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("BGR_to_LAB",lab_img)

# convert BGR to RGB
rgb_img = cv.cvtColor(lab_img,cv.COLOR_LAB2RGB)
cv.imshow("BGR_to_RGB",rgb_img)

cv.waitKey(0)