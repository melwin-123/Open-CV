import cv2 as cv

#image = cv.imread(r'C:\Users\Melwin Daniel\OneDrive\Desktop\Netflix CP\Source\One_piece.jpeg')
#cv.imshow('One Piece',image,)

cap = cv.VideoCapture(0)
fourcc =cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while (True):
    ret, frame= cap.read()
    if ret == True:

    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
       cv.imshow('frame',frame)
       out.write(frame)

       #print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
       #print(cap.get(cv.CAP_PROP_FRAME_WIDTH))

       if cv.waitKey(1) & 0xFF == ord('d'):
           break   
    else:
        break   
cap.release()
out.release()
cv.destroyAllWindows()

#k=cv.waitKey(0)
#if k == ord('d'):
#    cv.destroyAllWindows