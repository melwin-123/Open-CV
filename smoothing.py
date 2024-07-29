import cv2 as cv

img = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\Lion Heart.jpeg')
image=cv.resize(img,(840,560),interpolation=cv.INTER_CUBIC)
cv.imshow('Lion',image)

average = cv.blur(image,(3,3))
cv.imshow('Avg Blur',average )

gausian = cv.GaussianBlur(image,(3,3),0)
cv.imshow('GausianBlur',gausian)

median = cv.medianBlur(image,3)
cv.imshow('MedianBlur',median)

bilateral = cv.bilateralFilter(image, 10, 35, 25)
cv.imshow('Bilateral',bilateral)


k=cv.waitKey(0)
if k == ord('d'):
    cv.destroyAllWindows