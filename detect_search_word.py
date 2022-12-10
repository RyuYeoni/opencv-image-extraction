# pip install git+https://github.com/Joeclinton1/google-images-download.git

from google_images_download import google_images_download  #importing the library
import cv2
import numpy as np

def googleImageCrawling(keyword, limit):  #image crawling
    response = google_images_download.googleimagesdownload()   #class instantiation

    arguments = {"keywords" : keyword, "limit" : limit, "print_urls" : True, 
                 "chromedriver" : "./chromedriver", "format" : "jpg"}   #creating list of arguments
    paths = response.download(arguments)  #passing the arguments to the function
    print(paths)   #printing absolute paths of the downloaded images

keyword = input("keyword: ")  #if input the multiple keywords, use '', to enter them.
limit = int(input("count: "))  #input the image count

googleImageCrawling(keyword, limit)


# image show
image = cv2.imread('./downloads/'+ keyword +'/' + keyword +'.jpg')

height, width, channel = image.shape
print('original shape: ', height, width, channel)

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()
