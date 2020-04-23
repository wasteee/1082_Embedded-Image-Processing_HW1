# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:54:16 2020

@author: fghj8
"""

from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data, io,data_dir,filters, feature
from skimage.color import label2rgb
import skimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
np.set_printoptions(threshold=np.inf)
# settings for LBP
radius = 5  # LBP算法中范围半径的取值
n_points = 24 # 领域像素点数
# 读取图像
image1 =cv2.imread('C:\\Users\\fghj8\\image\\lbp.jpg',1)
cv2.imshow("image1",image1)

plt.hist(image1.ravel(), 255, [0, 256])
plt.show()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

ret,gray = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)#二值化
gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
cv2.imshow("gray",gray)
cv2.imwrite("C:\\Users\\fghj8\\image123.jpg",gray)

# 畫出直方圖
plt.hist(gray.ravel(), 255, [0, 256])
plt.show()


lbp = local_binary_pattern(image1, n_points, radius)
print(lbp.shape)

lbp = lbp / 65739
k = np.array(np.zeros((11,11)))
#m = -1
for i in range(950,960):
    for j in range(100,110):
        k[960-i,110-j] = lbp[i,j]
arr_mean = np.mean(k)
#求方差
arr_var = np.var(k)
#求标准差
arr_std = np.std(k,ddof=1)
print("平均值为：%f" % arr_mean)
print("方差为：%f" % arr_var)
print("标准差为:%f" % arr_std)
#print(m)16777215
# =============================================================================
# img_RGB = cv2.merge((lbp,lbp,))
# cv2.imshow("img_RGB",img_RGB)
# =============================================================================
# =============================================================================
# cv2.imshow("lbp_0",lbp)
# lbp[lbp == 0] = 255
# =============================================================================
cv2.imshow("lbp",lbp)
cv2.imwrite("C:\\Users\\fghj8\\lbp123.jpg",lbp)
plt.hist(lbp.ravel(), 255, [0, 256])
plt.show()
plt.hist(k.ravel(), 255, [0, 256])
plt.show()
# =============================================================================
# print(lbp.ravel())
# =============================================================================

edges = filters.sobel(image1)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()