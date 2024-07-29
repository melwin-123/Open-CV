import cv2 as cv

img = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\Lion Heart.jpeg')
image2 = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\One_piece.jpeg')
image =cv.resize(img,(840,560),interpolation=cv.INTER_CUBIC)
image3 =cv.resize(image2,(840,560),interpolation=cv.INTER_CUBIC)
print(img.shape)
print(img.size)
print(img.dtype)
print(image2)
b,g,r = cv.split(image)
image = cv.merge((b,g,r))

#ball = image[300:360 , 350:410]
#image[273:333 , 100:160] = ball

dst = cv.add(image, image3)
#dst = cv.addWeighted(image, 1, image3, .3, 0)



cv.imshow('Image',dst)
cv.waitKey(0)
cv.destroyAllWindows()