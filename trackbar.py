import numpy as np
import cv2 as cv

def nothing(x):
    print(x)
image = np.zeros((300,512,3),np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)
while(1):
    cv.imshow('image',image)
    k = cv.waitKey(1) & 0xFF
    if k == ord('d'):
        break

    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')
    s = cv.getTrackbarPos(switch,'image')

    if s==0:
        image[:] = 0
    else:
        image[:] = [b,g,r]
cv.destroyAllWindows()