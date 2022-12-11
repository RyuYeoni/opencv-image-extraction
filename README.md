
# extract images similar to search terms
---

## Description
1. Enter a search term, the simliar images are saved (crawing)
2. Extract similar images from dataset using opencv
3. Similarity measurement using Hamming distance (pictures may be slightly different)
4. Only those with a Hamming distance of less than 0.2, that is, those with a similarity of 80% or more are output.
---
## Precautions
1. opencv should be installed.
2. Unzip the file named '101_ObjectCategories.tar.gz'. (An image dataset of 10,000 photos)
3. selenium install : pip install selenium==3.14.1
4. beautifulsoup install : pip install beautifulsoup4
5. Install the 'chromedriver.exe' for your version of chrome. 
---
## result
![result1](./result_img/result1.png)
![result2](./result_img/result2.png)
---
## Reference 
- data set : https://data.caltech.edu/records/mzrjq-6wc02
- https://github.com/BaekKyunShin/OpenCV_Project_Python
- https://exit9509.tistory.com/m/17



