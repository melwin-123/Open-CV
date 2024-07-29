import cv2 as cv

image = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\One_piece.jpeg')
cv.imshow('One Piece',image)

#gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#blur = cv.GaussianBlur(image,(3,3),cv.BORDER_TRANSPARENT)
#cv.imshow('Blur',blur)

#canny = cv.Canny(blur,125,175)
#cv.imshow('Canny',canny)

#dilated = cv.dilate(canny,(3,3),iterations=3)
#cv.imshow('Dilated',dilated)

#eroded = cv.erode(dilated,(3,3),iterations=3)
#cv.imshow('Eroded',eroded)

resized = cv.resize(image,(100,100),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

cropped = image[50:100, 100:200]
cv.imshow('Cropped',cropped)



cv.waitKey(0)