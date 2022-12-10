import cv2
from matplotlib import pyplot as plt

body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

img = cv2.imread("./image/portrait6.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

body = body_cascade.detectMultiScale(gray, 1.01, 10)

count_body = 0
for (x,y,w,h) in body:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    count_body += 1

if count_body == 0:
    print("This image is landscape")
else:
    print("This image is portrait")

plt.figure(figsize=(12,12))
plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()