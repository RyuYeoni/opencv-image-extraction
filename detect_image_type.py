import cv2
import numpy as np

#얼굴인식 casecade 사용
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#hog객체 생성 및 설정
body = cv2.HOGDescriptor()
body.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
bodyParams = {'winStride':(8,8), 'padding':(32, 32), 'scale':1.05, 'hitThreshold':0}

#사진들의 크기 똑같이 조정
def hconcat_resize_min(img_list, interpolation=cv2.INTER_CUBIC):
    horizon_min = min(img.shape[0] for img in img_list)
    img_list_resize = [cv2.resize(img, (int(img.shape[1] * horizon_min / img.shape[0]), horizon_min), interpolation=interpolation)
                      for img in img_list]
    return cv2.hconcat(img_list_resize)

#읽을 사진 파일 portrait1~6, landscape1~6 이미지 넣을 수 있음
img1 = cv2.imread("./image/portrait6.jpg")
img2 = cv2.imread("./image/landscape6.jpg")

#색상 gray로 변경
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#얼굴인식 cascade를 사용해서 객체 검출
faces1 = face_cascade.detectMultiScale(gray1, 1.1, 4)
faces2 = face_cascade.detectMultiScale(gray2, 1.1, 4)

#사람 몸 인식해서 객체 검출
human1, r1 = body.detectMultiScale(gray1, **bodyParams)
human2, r2 = body.detectMultiScale(gray2, **bodyParams)

#얼굴의 갯수 검출
count_face1 = 0      #얼굴 갯수 0개로 초기화
for(x, y, w, h) in faces1:
    cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)
    count_face1 += 1     #얼굴이 인식되면 갯수 하나씩 증가

count_face2 = 0
for(x, y, w, h) in faces2:
    cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)
    count_face2 += 1

#사람 몸의 갯수 검출
count_body1 = 0      #사람 몸의 갯수 0개로 초기화
for (x,y,w,h) in human1:
    cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0), 2)
    count_body1 += 1     #사람 몸이 인식되면 갯수 하나씩 증가

count_body2 = 0
for (x,y,w,h) in human2:
    cv2.rectangle(img2,(x,y),(x+w,y+h),(255,0,0), 2)
    count_body2 += 1

#이미지가 인물사진인지 풍경사진인지 검출
find_image_type1 = 0        #이미지타입 0으로 초기화 함
if count_face1 > 0:      #이미지에서 얼굴이 검출되어 count_face > 0이면
    find_image_type1 = 1    #이미지타입에 1 대입

elif count_body1 > 0:      #이미지에서 사람 몸이 검출되어 count_body > 0 이면
    find_image_type1 = 1     #이미지 타입에 1 대입

if find_image_type1 == 0:    #이미지 타입이 0이면 풍경사진이라고 출력
    print("First image is landscape")

elif find_image_type1 == 1:  #이미지 타입이 1이면 인물사진이라고 출력
    print("First image is portrait")

find_image_type2 = 0
if count_face2 > 0:
    find_image_type2 = 1
    
elif count_body2 > 0:
    find_image_type2 = 1

if find_image_type2 == 0:
    print("Second image is landscape")

elif find_image_type2 == 1:
    print("Second image is portrait")

img_horizon_resize = hconcat_resize_min([img1, img2])
cv2.imshow('Imges type', img_horizon_resize)
cv2.waitKey()