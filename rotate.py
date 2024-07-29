import cv2 as cv
import numpy as np

image = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\One_piece.jpeg')
cv.imshow('One Piece',image)

def rotate(image, angle, rotPoint = None):
 
    (height,width) = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,scale=1.0) 
    dimensions = (width,height)
    return cv.warpAffine(image, rotMat,dimensions)

rotated = rotate(image,45)
cv.imshow('Rotated',rotated)

rotated_rotate = rotate(rotated,45)
cv.imshow("Rotated_rotate",rotated_rotate)

#resize
resized = cv.resize(image, (100,100),interpolation=cv.INTER_CUBIC)
cv.imshow('Resize',resized)

#fliping
flip = cv.flip(image,1)
cv.imshow('Flip',flip)

cropped =image[100:200, 200:300]
cv.imshow('Crop',cropped)


k=cv.waitKey(0)
if k == ord('d'):
    cv.destroyAllWindows

     



