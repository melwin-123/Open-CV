import cv2 as cv

img = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\Lion Heart.jpeg')
image=cv.resize(img,(840,560),interpolation=cv.INTER_CUBIC)
cv.imshow('Lion',image)

gray = cv.cvtColor(image , cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

threshold,thresh =cv.threshold(gray,115,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

threshold,thresh_inv =cv.threshold(gray,115,255,cv.THRESH_BINARY_INV)
cv.imshow('Thresh_inv',thresh_inv)

threshold,thresh_trunc =cv.threshold(gray,115,255,cv.THRESH_TRUNC)
cv.imshow('Thresh_trunc',thresh_trunc)


adp_threshold =cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,19,9 )
cv.imshow('Apd_Thresh',adp_threshold)

adp_threshold1 =cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,19,9 )
cv.imshow('Apd_Thresh1',adp_threshold1)

k=cv.waitKey(0)
if k == ord('d'):
    cv.destroyAllWindows