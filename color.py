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
import numpy as np
from PIL import Image

data = np.zeros([32, 32, 3], dtype=np.uint8)
image = Image.fromarray(data, 'RGB')
image
from PIL import Image
import os

# 연습용 파일 경로
image_path = os.path.join(os.getcwd(), '/Users/gomin/opencv-image-extraction/village.jpg')

# 이미지 열기
img = Image.open(image_path)

# width와 height 출력
print(img.width)
print(img.height)

# JPG 파일 형식으로 저장해보기
new_image_path = os.path.join(os.getcwd(), '/Users/gomin/opencv-image-extraction/village.jpg')
img = img.convert('RGB')
img.save(new_image_path)
resized_image = img.resize((100,200))

resized_image_path = os.path.join(os.getcwd(), '/Users/gomin/opencv-image-extraction/village_resized.jpg')
resized_image.save(resized_image_path)
resized_image
box = (300, 100, 600, 400)
area = img.crop(box)

cropped_image_path = os.path.join(os.getcwd(), '/Users/gomin/opencv-image-extraction/village_cropped.jpg')
area.save(cropped_image_path)
area
import os
import pickle
from PIL import Image

dir_path = os.path.join(os.getcwd(), '/Users/gomin/opencv-image-extraction')
train_file_path = os.path.join(dir_path, 'train')

with open(train_file_path, 'rb') as f:
    train = pickle.load(f, encoding='bytes')

print(type(train))
train[b'filenames'][0:5]
train[b'data'][0:5]
train[b'data'][0].shape
image_data = train[b'data'][0].reshape([32, 32, 3], order='F')   
image = Image.fromarray(image_data)    # Pillow를 사용하여 Numpy 배열을 Image객체로 만들어서
image 
image_data = image_data.swapaxes(0, 1) #Return a view of the array with `axis1` and `axis2` interchanged.
image = Image.fromarray(image_data)
image