import cv2 as cv
import matplotlib.pyplot as plt

import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\Lion Heart.jpeg')
#img = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\One_piece.jpeg')
image=cv.resize(img,(840,560),interpolation=cv.INTER_CUBIC)
cv.imshow('Lion',image)

blank = np.zeros(image.shape[:2], dtype='uint8')
circle= cv.circle(blank.copy(), (image.shape[1]//2,image.shape[0]//2 ),200 ,255,thickness=-1)
cv.imshow('circle',circle)
rectangle = cv.rectangle(blank.copy(),(250,250),(600,600),255,-1)
cv.imshow('Rect',rectangle)

mask= cv.bitwise_or(circle,rectangle)
cv.imshow('Mask',mask)

masked = cv.bitwise_and(image,image,mask=mask)
cv.imshow('Masked',masked)

#gray = cv.cvtColor(masked,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#gray_hist = cv.calcHist([image],[0],masked,[256],[0,256])



plt.figure()
plt.title('colour Histogram')
plt.xlabel('Bins')
plt.ylabel('of Pixles')

colours = ('b', 'g','r')
for i,col in enumerate(colours):
    hist = cv.calcHist([masked], [i], mask ,[256],[0,256])
    plt.plot(hist , color = col)
    plt.xlim([0,256])


plt.show()


cv.waitKey(0)