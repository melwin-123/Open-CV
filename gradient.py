import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\Lion Heart.jpeg')
image=cv.resize(img,(840,560),interpolation=cv.INTER_CUBIC)
cv.imshow('Lion',image)

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

lap = cv.Laplacian(gray, cv.CV_32F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

cv.waitKey(0)