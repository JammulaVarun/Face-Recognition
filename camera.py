import cv2

cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    ret,frame=cap.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    if ret==False:
        continue

    face=face_cascade.detectMultiScale(gray_frame,1.3,5)
    print(face)


    for(x,y,a,b) in face:
    	 cv2.rectangle(frame,(x,y),(x+a,y+b),(255,0,0),2)

    cv2.imshow("Vdieo Frame",frame)

    key=cv2.waitKey(1) & 0xFF

    if key == ord ('q') :
    	break

cap.release()
cv2.destroyAllWindows()