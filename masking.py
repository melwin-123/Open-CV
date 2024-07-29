import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\Lion Heart.jpeg')
image=cv.resize(img,(840,560),interpolation=cv.INTER_CUBIC)
cv.imshow('Lion',image)

blank = np.zeros(image.shape[:2], dtype='uint8')
cv.imshow('Blank',blank)
mask = cv.circle(blank, (image.shape[1]//2,image.shape[0]//2),100,255,thickness=-1)
cv.imshow('Mask',mask)

masked = cv.bitwise_and(image,image,mask=mask)
cv.imshow('Masked',masked)


k=cv.waitKey(0)
if k == ord('d'):
    cv.destroyAllWindows
