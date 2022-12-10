import cv2
import numpy as np

def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)


img1 = cv2.imread("./image/portrait6.jpg")
img2 = cv2.imread("./image/landscape1.jpg")

img1 = cv2.resize(img1, (0,0), None, .5, .5)
img2 = cv2.resize(img2, (0,0), None, .5, .5)

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

im_h_resize = hconcat_resize_min([img1, img2])
cv2.imshow('Im H', im_h_resize)


cv2.waitKey()