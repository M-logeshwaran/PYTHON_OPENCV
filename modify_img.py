
import cv2 as cv
import numpy as np

def resize(Frame, scale):
    width = int(Frame.shape[1] * scale)
    height = int(Frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(Frame, dimension, interpolation=cv.INTER_AREA)


# slow process
def recolor(r_img,k):
    for row in range(r_img.shape[0]):
        for col in range(r_img.shape[1]):
            pixel = r_img[row, col]
            if pixel[0] < 200 and pixel[1] < 100 and pixel[2] < 100:
                r_img[row, col] = [128, 0, 128]  # Set to new color (BGR)
                k += 1
    return r_img            


# fast process
def recolor1 (r_img):
    # Create a mask for pixels where all channels < 200
    mask = (r_img[:, :, 0] < 100) & (r_img[:, :, 1] < 200) & (r_img[:, :, 2] < 200)
    # Set those pixels to [128, 0, 128] (BGR)
    r_img[mask] = [220, 225 , 225]
    return r_img


img = cv.imread(r"/home/loki/Pictures/wallpaper/wallpaperflare.com_wallpaper.jpg")
r_img = resize(img, 0.40)
k = 1
r_cimg=recolor(r_img,k)


capture = cv.VideoCapture(r"/home/loki/Pictures/wallpaper/zenitsu.mp4")
while(True):
    isTrue,Frame = capture.read()
    r_cframe = recolor1(Frame)
    cv.imshow("video",r_cframe)

    if(cv.waitKey(20) & 0xff == ord("d")):
        break



capture.release()
cv.imshow("image", r_cimg)
cv.waitKey(0)
cv.destroyAllWindows()


            