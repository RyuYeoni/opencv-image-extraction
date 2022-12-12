#detect search word

# pip install selenium   //Installing Before Running
# pip install beautifulsoup4   //Installing Before Running
# install Chomedriver  //https://chromedriver.chromium.org/downloads

import os
import sys
import selenium
import cv2
import numpy as np
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup as soups
from selenium.webdriver.common.by import By


# image crawling
def search_selenium(search_name, search_path):
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"  # Search Keyword Address

    browser = webdriver.Chrome('C:/Users/BIT/Desktop/chromedriver.exe')
    browser.get(search_url)

    last_height = browser.execute_script("return document.body.scrollHeight")   # Browser Height Found

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")   # Scroll down to the end of browser

        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                browser.find_element(By.CSS_SELECTOR, ".mye4qd").click()    # Click if "See more results" appears while scrolling down
            except:
                break
        last_height = new_height

    image_count = len(browser.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd"))

    print("Number of images loaded : ", image_count)
    

    # Number of Image Collections
    # search_limit = int(input("Number of image collections desired : "))
    search_limit = 11
    print("Number of image collections desired", search_limit)

    for i in range(search_limit):
        image = browser.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")[i]
        image.screenshot(search_path + '/' + search_name + '_' +str(i) + ".png")

    browser.close()


search_name = input("search for keyword : ")  # input the keyword
crawling_path = search_name   # create keyword folder
search_path = "./download_images/" + crawling_path   # keyword floder path
try:
    if not os.path.exists(search_path):  # If no duplicate folder names exist, create
        os.makedirs(search_path)
    else:   # If duplicated, exit the program after printing the statement
        print('A folder previously downloaded with the same [search word, number of images] exists.')
        sys.exit(0)
except OSError:
    print('os error')
    sys.exit(0)

search_selenium(search_name, search_path)

# image show
image = cv2.imread('./download_images/'+ search_name + '/' +search_name + '_10.png')  # Reading images from downloaded folders

height, width, channel = image.shape
print('original shape: ', height, width, channel)

image_c = cv2.resize(image, (600, 500))  # Resize the image

height, width, channel = image_c.shape
print('change shape: ', height, width, channel)

image_c = cv2.putText(image_c, search_name, (500, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))  # put text keyword (white)
# image_c = cv2.putText(image_c, search_name, (500, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))   # put text keyword (black)

if image_c is None:   # Output a statement if image load fails
    print('Image load failed')
    sys.exit()

cv2.imshow('image', image_c) #showing image
cv2.waitKey()
cv2.destroyAllWindows()
