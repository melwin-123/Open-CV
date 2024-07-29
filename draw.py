import cv2 as cv
import numpy as np

#blank = np.zeros((500,500,3), dtype='uint8')
blank1 = np.zeros((500,500,3), dtype='uint8')

#blank[200:300,300:400] = 0,0,255
#cv.imshow('Blank',blank)
#cv.imshow('Green',blank1)


cv.rectangle(blank1, (0,0), (250,250), (0,250,0), thickness=-1)

#img =cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\One_piece.jpeg')

cv.imshow('Rectangle',blank1)

cv.circle(blank1,(50,50),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank1)

cv.line(blank1,(50,100),(100,200),(255,0,0),thickness=3)
cv.imshow('Line', blank1)

cv.waitKey(0)