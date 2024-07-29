import numpy as np
import cv2 as cv

def nothing(x):
    print(x)


cv.namedWindow('image')

cv.createTrackbar('Cp', 'image', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image',0,1,nothing)
while(1):
    img = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\Lion Heart.jpeg')
    image=cv.resize(img,(840,560),interpolation=cv.INTER_CUBIC)
    pos = cv.getTrackbarPos('Cp', 'image')
    cv.putText(image, str(pos), (50,150),cv.FONT_HERSHEY_SIMPLEX,4,(0,0,255))
    k = cv.waitKey(1) & 0xFF
    if k == ord('d'):
        break

    
    s = cv.getTrackbarPos(switch,'image')

    if s==0:
        pass
    else:
        image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    image = cv.imshow('image',image)    
cv.destroyAllWindows()