import cv2
import numpy as np

#사진들의 크기 조정
def hconcat_resize_min(img_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(img.shape[0] for img in img_list)
    img_list_resize = [cv2.resize(img, (int(img.shape[1] * h_min / img.shape[0]), h_min), interpolation=interpolation)
                      for img in img_list]
    return cv2.hconcat(img_list_resize)


img1 = cv2.imread("./image/portrait6.jpg")
img2 = cv2.imread("./image/landscape1.jpg")

img1 = cv2.resize(img1, (0,0), None, .5, .5)
img2 = cv2.resize(img2, (0,0), None, .5, .5)

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img_h_resize = hconcat_resize_min([img1, img2])
cv2.imshow('Im H', img_h_resize)


cv2.waitKey()