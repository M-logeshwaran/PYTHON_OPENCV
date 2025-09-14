import cv2 as cv


# resize frame
def resize(Frame,scale):
    width = int(Frame.shape[1]*scale)
    height = int(Frame.shape[0]*scale)
    dimension = (width,height)

    return cv.resize(Frame,dimension,interpolation=cv.INTER_AREA)


# reading images
img = cv.imread(r'/home/loki/Pictures/wallpaper/black_lake.jpg')
r_img = resize(img,0.15)
cv.imshow('black_lake',r_img)
cv.waitKey(0)


# reading video
capture = cv.VideoCapture(r'/home/loki/Pictures/wallpaper/zenitsu.mp4')
while True:
    isTrue, Frame = capture.read()
    r_frame = resize(Frame,0.75)

    cv.imshow('ZENITSU_AURA',r_frame)

    if( cv.waitKey(20) & 0xFF == ord('d') ):
        break


capture.realese()
cv.destroyAllWindows()
