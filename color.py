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
def build_histogram_db():
    histogram_db = {}

    #디렉토리에 모아 둔 이미지 파일들을 전부 가져온다.
    path = images_dir_path
    file_list = os.listdir(images_dir_path)

    for file_name in tqdm(file_list):
        file_path = os.path.join(images_dir_path, file_name)
        image = cv.imread('village.jpg')

        histogram = get_histogram(image)

        histogram_db[file_name] = histogram

    return histogram_db
histogram_db = build_histogram_db()
histogram_db['village.jpg']
def get_target_histogram():
    filename = input("이미지 파일명을 입력하세요 : ")
    if filename not in histogram_db:
        print('유효하지 않은 이미지 파일명입니다.')
        return None
    return histogram_db[filename]
target_histogram = get_target_histogram()
target_histogram
def search(histogram_db, target_histogram, top_k=5):
    results = {}

    # Calculate similarity distance by comparing histograms.
    for file_name, histogram in tqdm(histogram_db.items()):
        distance = cv.compareHist(H1=target_histogram,
                                   H2=histogram,
                                   method=cv.HISTCMP_CHISQR)

        results[file_name] = distance

    results = dict(sorted(results.items(), key=lambda item: item[1])[:top_k])

    return results
result = search(histogram_db, target_histogram)
result
def show_result(result):
    f=plt.figure(figsize=(10,3))
    for idx, filename in enumerate(result.keys()):    
        img_path = os.path.join(images_dir_path, filename)
        
        im = f.add_subplot(1,len(result),idx+1)
        im.grid(False)
        
        img = Image.open(img_path)
        im.imshow(img)
target_histogram = get_target_histogram()
result = search(histogram_db, target_histogram)
show_result(result)