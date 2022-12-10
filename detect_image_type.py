import cv2

#얼굴인식 casecade 사용
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#hog객체 생성 및 설정
body = cv2.HOGDescriptor()
body.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
bodyParams = {'winStride':(8,8), 'padding':(32, 32), 'scale':1.05, 'hitThreshold':0}

#읽을 사진 파일
img = cv2.imread("./image/portrait6.jpg")
#색상 gray로 변경
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#얼굴인식 cascade를 사용해서 객체 검출
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#사람 몸 인식해서 객체 검출
human, r = body.detectMultiScale(gray, **bodyParams)

#얼굴의 갯수 검출
count_face = 0      #얼굴 갯수 0개로 초기화
for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    count_face += 1     #얼굴이 인식되면 갯수 하나씩 증가

#사람 몸의 갯수 검출
count_body = 0      #사람 몸의 갯수 0개로 초기화
for (x,y,w,h) in human:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 2)
    count_body += 1     #사람 몸이 인식되면 갯수 하나씩 증가

#이미지가 인물사진인지 풍경사진인지 검출
find_image_type = 0        #이미지타입 0으로 초기화 함
if count_face > 0:      #이미지에서 얼굴이 검출되어 count_face > 0이면
    find_image_typent = 1    #이미지타입에 1 대입
    
if count_body > 0:      #이미지에서 사람 몸이 검출되어 count_body > 0 이면
    find_image_type = 1     #이미지 타입에 1 대입

if find_image_type == 0:    #이미지 타입이 0이면 풍경사진이라고 출력
    print("This image is landscape")

elif find_image_type == 1:  #이미지 타입이 1이면 인물사진이라고 출력
    print("This image is portrait")

cv2.imshow('img', img)
cv2.waitKey()