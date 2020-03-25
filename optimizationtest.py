import cv2
import numpy as np
from matplotlib import pyplot as plt
import timeit

def openingandclosing(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=2)
    return img

img = cv2.imread('G:\\imagetest\\photo.jpeg',0) 
cv2.imshow('org', img)
#Binarization
img[img > 128] = 255
img[img <= 128] = 0

cv2.setUseOptimized(True) 
print ('Enable optimization(SSE2,AVX...):',cv2.useOptimized())
start = timeit.default_timer()
for i in range (0,100):
    img = openingandclosing(img)
stop = timeit.default_timer()
print('Runtime with AVX: ', stop - start,"\n")


img = cv2.imread('G:\\imagetest\\photo.jpeg',0) 

#Binarization
img[img > 128] = 255
img[img <= 128] = 0
cv2.setUseOptimized(False) 
print ('Enable optimization(SSE2,AVX...):',cv2.useOptimized())
start = timeit.default_timer()
for i in range (0,100):
    img = openingandclosing(img)
stop = timeit.default_timer()
print('Runtime without AVX: ', stop - start)


cv2.imshow('after', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
