import numpy as np
import cv2 as cv

def clickevent(event , x , y , flags , param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font = cv.FONT_HERSHEY_SIMPLEX
        strXY = str(x) +', '+ str(y)
        cv.putText(img , strXY, (x,y),font,0.5,(255,255,0),2)
        cv.imshow('image',image)
img = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\Lion Heart.jpeg')
image =cv.resize(img,(840,560),interpolation=cv.INTER_CUBIC)
cv.imshow('image',image)
cv.setMouseCallback('image',clickevent)

cv.waitKey(0)
cv.destroyAllWindows