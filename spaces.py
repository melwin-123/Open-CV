import cv2 as cv

img = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\Lion Heart.jpeg')

image=cv.resize(img,(840,560),interpolation=cv.INTER_CUBIC)

cv.imshow('Lion',image)

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV

hsv= cv.cvtColor(image,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

lab = cv.cvtColor(image,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)


k=cv.waitKey(0)
if k == ord('d'):
    cv.destroyAllWindows