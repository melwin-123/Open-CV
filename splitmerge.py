import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\Lion Heart.jpeg')

image=cv.resize(img,(840,560),interpolation=cv.INTER_CUBIC)

cv.imshow('Lion',image)


b,g,r = cv.split(image)

cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)


print(image.shape)
print(b.shape)
print(g.shape)
print(r.shape)



k=cv.waitKey(0)
if k == ord('d'):
    cv.destroyAllWindows