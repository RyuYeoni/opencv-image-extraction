import cv2

body = cv2.HOGDescriptor()
body.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
bodyParams = {'winStride':(8,8), 'padding':(32, 32),
                'scale':1.05, 'hitThreshold':0}

img = cv2.imread("./image/portrait5.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
human, r = body.detectMultiScale(gray, **bodyParams)

count_body = 0
for (x,y,w,h) in human:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    count_body += 1

if count_body == 0:
    print('This image is landscape')

else:
    print('This image is portrait')

cv2.imshow('img', img)
cv2.waitKey()