import cv2 as cv


def resize(Frame, scale):
    width = int(Frame.shape[1] * scale)
    height = int(Frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(Frame, dimension, interpolation=cv.INTER_AREA)


img = cv.imread(r"/home/loki/Pictures/wallpaper/wallpaperflare.com_wallpaper.jpg")
re_img = resize(img , 0.40)
if img is None:
    print("image not found !")
    exit()

# Gray_scale image ...
gray_img = cv.cvtColor(re_img,cv.COLOR_BGR2GRAY)
cv.imshow("image",gray_img)

# crop image ...
crop_img = gray_img[250:500 , : ]
cv.imshow("crop_image",crop_img)

# Blur image ...
blur_img = cv.GaussianBlur(re_img,(7,7),cv.BORDER_DEFAULT) 
cv.imshow("blur_img",blur_img)

# Edge cascade ...
img_edge = cv.Canny(blur_img,125,175)
cv.imshow("edge_img",img_edge)

# Diallated image ...
dialte_img = cv.dilate(img_edge,(7,7),iterations=1)
cv.imshow("dialte_img",dialte_img)

# eroding image ...
erode_img = cv.erode(dialte_img,(3,3),iterations=1)
cv.imshow("erode_image",erode_img)

cv.waitKey(0)
