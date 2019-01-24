import cv2 as cv
import numpy as np
import time as t


def inverse(image):
    new =cv.resize(image,(0,0),fx=0.5,fy=0.5,interpolation=cv.INTER_CUBIC)
    dst =cv.bitwise_not(new)
    cv.imshow('inverse_demo',dst)


src =cv.imread('e:/cat.jpg')
t1 =t.time()
cv.imshow('cat',src)
inverse(src)#调用库函数
t2 =t.time()
time =t2-t1
print('time:%s ms'%time)

cv.waitKey(0)
cv.destroyAllWindows()