import cv2 as cv
import numpy as np

image = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\One_piece.jpeg')
cv.imshow('One Piece',image)

blank = np.zeros(image.shape, dtype = 'uint8')
cv.imshow("blank",blank)

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

#canny = cv.Canny(blur,125,175)
#cv.imshow('Canny',canny)

ret, treshold =cv.threshold(gray,125,175,cv.THRESH_BINARY)
cv.imshow('Tresh',treshold)

contours, hierarchies = cv.findContours(treshold,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found! ')

cv.drawContours(blank,contours,-1,(0,0,255),5)
cv.imshow('Draw',blank)

cv.waitKey(0)