import cv2 as cv
import numpy as np

image = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\One_piece.jpeg')

cv.imshow('One Piece',image)

def transulate(image, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)

transulated = transulate(image, -100, 100)
cv.imshow('Trasulated',transulated)

cv.waitKey(0)

