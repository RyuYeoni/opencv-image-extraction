import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


img = cv2.imread("./image/portrait3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

count = 0
for(x, y, w, h) in faces:
    print(x, y, w, h)
    count += 1
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

if count == 0:
    print("This image is landscape")

else:
    print("This image is portrait")

cv2.imshow('img', img)
cv2.waitKey()