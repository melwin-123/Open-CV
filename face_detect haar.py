import cv2

face_cassade = cv2.CascadeClassifier(r'C:\Users\Melwin Daniel\OneDrive\Pictures\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while (True):
    ret, frame= cap.read()

    image = cv2.imread(r'C:\Users\Melwin Daniel\OneDrive\Pictures\Faces.jpeg')
    img = cv2.resize(image,(500,500))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Face',gray)

    face = face_cassade.detectMultiScale(gray,1.1, 4)
    print({len(face)})

    for (x , y, w, h) in face:
        cv2.rectangle(frame, (x, y),(x+w, y+h),(255, 0, 0), 2)

    cv2.imshow('Image', frame)
    #cv2.waitKey(0)
    k = cv2.waitKey(30) &0xff
    if k == ord('d'):
        break
cap.release()    