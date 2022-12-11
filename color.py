import os
import pickle
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
from PIL import Image
train_file_path = os.path.join(os.getcwd(), '/cifar-100-python/train')
images_dir_path = os.path.join(os.getcwd(), '/Users/gomin/opencv-image-extraction')
def draw_color_histogram_from_image(file_name):
    image_path = os.path.join(images_dir_path, file_name)
    # 이미지 열기
    img = Image.open(image_path)
    cv_image = cv.imread(image_path)

    # Image 시각화
    f=plt.figure(figsize=(10,3))
    im1 = f.add_subplot(1,2,1)
    im1.grid(False)
    im1.imshow(img)
    im1.set_title("Image")

    # Histogram 시각화
    im2 = f.add_subplot(1,2,2)
    color = ('b','g','r')     # OpenCV에서는 RGB를 BGR로 쓴다.
    for i,col in enumerate(color):
        # image에서 i번째 채널의 히스토그램을 뽑아서(0:blue, 1:green, 2:red)
        histr = cv.calcHist([cv_image],[i],None,[256],[0,256])   
        # 채널 색상과 맞춰 그래프를 그린다.
        im2.plot(histr,color = col)   

    im2.grid(False)
    im2.set_title("Histogram")
draw_color_histogram_from_image('village.jpg')
def get_histogram(image):
    histogram = []

    # Create histograms per channels, in 4 bins each.
    for i in range(3):
        channel_histogram = cv.calcHist(images=[image],
                                         channels=[i],
                                         mask=None,
                                         histSize=[4],  # 히스토그램 구간을 4개로 한다.
                                         ranges=[0, 256])
        histogram.append(channel_histogram)  

    histogram = np.concatenate(histogram)
    histogram = cv.normalize(histogram, histogram)

    return histogram
filename = train[b'filenames'][0].decode()
file_path = os.path.join(images_dir_path, filename)
image = cv.imread(file_path)
histogram = get_histogram(image)
histogram