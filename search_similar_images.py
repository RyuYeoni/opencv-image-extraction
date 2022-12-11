
# 1. 검색어에 맞게 이미지 추출, 저장

from selenium import webdriver # pip install selenium==3.14.1
from bs4 import BeautifulSoup as soups #pip install beautifulsoup4



def imgsearch(search_name, search_path, search_limit) : #검색할 이미지 내용, 경로, 이미지 개수(10개로 설정)
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch" #이미지의 주소, str(search_name)만 다르고 나머지 형식(url 패턴)은 같음
    
    path = webdriver.Chrome('./chromedriver.exe') #chromedriver 설치 경로
    path.get(search_url)
    
    image_count = len(path.find_elements_by_tag_name("img")) #오브젝트(이미지)를 얻어내서 그것의 개수를 image_count 에 저장
    print("확인된 이미지 개수 : ", image_count) # 전체 확인된 오브젝트(이미지)의 개수를 출력

    path.implicitly_wait(2) # 2초 대기

    for i in range( search_limit ) : # 검색하고자 하는 이미지 개수만큼 for문 반복 (개수는 10으로 설정)
            image = path.find_elements_by_class_name('rg_i.Q4LuWd')[i] #rg_i.Q4LuWd: 다운 받을 이미지의 공통적인 태그의 클래스명, 검색어에 맞는 오브젝트(이미지)를 얻어 image 에 저장
            image.screenshot("./imgdownload/" + str(i) + ".png") #imgdownload 라는 폴더에 0.png~9.png 까지 총 10개의 사진 저장
    path.close()

if __name__ == "__main__" :

    search_name = input("검색하고 싶은 이미지 : ")
    search_limit = int(10) # 검색 사진 수를 10개로 설정
    search_path = "Your Path"
    
    imgsearch(search_name, search_path, search_limit)
    print('수집이 완료되었습니다.')
    print('곧 비슷한 사진이 있으면 출력됩니다.')

    

# 2. 이미지 데이터셋에서 비슷한 이미지 찾기

import cv2
import numpy as np
import glob
import random

# 입력 이미지 읽고 나타내기
img_index=[0,1,2,3,4,5,6,7,8,9]
choice_index=random.choice(img_index)

img = cv2.imread("./imgdownload/"+str(choice_index)+".png") #저장된 10개 이미지 중 하나를 랜덤으로 읽어옴
if img is None: #파일에 문제가 있는 경우
    print('Image load failed')
    sys.exit()
cv2.imshow('input', img) #이미지 띄어줌

# image data set의 경로
dataset_dir = './101_ObjectCategories'

# 16x16 크기의 평균 해쉬로 변환해주는 함수
def imgtrans(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (16, 16)) #이미지를 16X16 사이즈로 조정
    avg = gray.mean()  #mean 함수: 평균 구하기
    px = 1 * (gray > avg) #전체 픽셀값 평균보다 큼 : 1, 작음 : 0
    return px

# 해밍거리 측정 함수
def hamming(a, b):
    a = a.reshape(1,-1) #행을 1로 해서 자동으로 재배열
    b = b.reshape(1,-1) #행을 1로 해서 자동으로 재배열
    # 같은 자리의 값이 서로 다른 것들의 합
    distance = (a !=b).sum()
    return distance

input_hash = imgtrans(img)   # 입력 이미지 해쉬 변환

img_path = glob.glob(dataset_dir+'/**/*.jpg')  # 이미지 데이터셋 디렉토리의 모든 영상 파일 경로
count=0 #비슷한 사진 수

for path in img_path:
    # 데이터셋 중 한 개씩 읽기
    img = cv2.imread(path)
    # 데이터셋 사진 해쉬 변환
    a_hash = imgtrans(img)
    # 입력 사진과 데이터셋 사진의 해밍 거리 측정
    dst = hamming(input_hash, a_hash)
    if dst/256 < 0.2: # 해밍거리 20% 이내만 출력(유사도 80%만 출력)
        print(path, dst/256)
        cv2.imshow(path, img)
        count=count+1
        
print("비슷한 사진의 개수:"+str(count))
if count==0:
    print("비슷한 사진을 찾을 수 없습니다.")

cv2.waitKey(0) #아무키나 누르면
cv2.destroyAllWindows() #창이 닫힘

