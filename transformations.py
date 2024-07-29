import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread(r"C:\Users\Melwin Daniel\OneDrive\Pictures\balls.jpg", cv.IMREAD_GRAYSCALE)
_,mask =cv.threshold(image , 170, 255, cv.THRESH_BINARY)

titles = ['image','mask']
images = [image,mask]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()