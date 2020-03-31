import cv2
import numpy as np
from matplotlib import pyplot as plt
import timeit
import os
print(cv2. __version__ )
def opening(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)
    return img

def closing(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=2)
    return img

img = cv2.imread('G:\\imagetest\\photo.jpeg',0) 
cv2.imshow('org', img)
#Binarization
img[img > 128] = 255
img[img <= 128] = 0
cv2.imwrite('G:\\imagetest\\Binarization.jpeg',img)

cv2.setUseOptimized(True) 
print('----------opening x100----------','\n')
print ('Enable optimization(SSE2,AVX...):',cv2.useOptimized())
opening_with_avx = img
start = timeit.default_timer()
for i in range (0,100):
    opening_with_avx = opening(opening_with_avx)
stop = timeit.default_timer()
t1 = stop - start
print('Runtime with AVX: ', t1,"\n")
            


opening_without_avx = img
cv2.setUseOptimized(False) 

print ('Enable optimization(SSE2,AVX...):',cv2.useOptimized())
start = timeit.default_timer()
for i in range (0,100):
    opening_without_avx = opening(opening_without_avx)
stop = timeit.default_timer()
t2 = stop - start
print('Runtime without AVX: ', t2,'\n')
print('Speedup:',t2/t1,'\n')

print('----------closing x100----------','\n')
closing_whit_avx = img

cv2.setUseOptimized(True) 
print ('Enable optimization(SSE2,AVX...):',cv2.useOptimized())
start = timeit.default_timer()
for i in range (0,100):
    closing_whit_avx = closing(closing_whit_avx)
stop = timeit.default_timer()
t1_ = stop - start
print('Runtime with AVX: ', t1_,"\n")



closing_whitout_avx = img
cv2.setUseOptimized(False) 
print ('Enable optimization(SSE2,AVX...):',cv2.useOptimized())
start = timeit.default_timer()
for i in range (0,100):
    closing_whitout_avx = closing(closing_whitout_avx)
stop = timeit.default_timer()
t2_ = stop - start
print('Runtime without AVX: ', t2_,'\n')
print('Speedup:',t2_/t1_)

cv2.imwrite('G:\\imagetest\\opening_with_avx.jpeg',opening_with_avx)
cv2.imwrite('G:\\imagetest\\closing_whit_avx.jpeg',closing_whit_avx)
cv2.imshow('afteropening', opening_with_avx)
cv2.imshow('afterclosing', closing_whit_avx)
cv2.waitKey(0)
cv2.destroyAllWindows()


