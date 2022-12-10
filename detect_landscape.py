import cv2
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
body = cv2.HOGDescriptor()
body.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
bodyParams = {'winStride':(8,8), 'padding':(32, 32),
                'scale':1.05, 'hitThreshold':0}

img = cv2.imread("./image/landscape1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
human, r = body.detectMultiScale(gray, **bodyParams)

count_face = 0
for(x, y, w, h) in faces:
    print(x, y, w, h)
    count_face += 1
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

count_body = 0
for (x,y,w,h) in human:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    count_body += 1

count = 0
if count_face > 0:
    count = 1
    
if count_body > 0:
    count = 1

if count == 0:
    print("This image is landscape")

elif count == 1:
    print("This image is portrait")

cv2.imshow('img', img)
cv2.waitKey()