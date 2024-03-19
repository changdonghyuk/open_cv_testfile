import numpy as np
import cv2

cap =cv2.VideoCapture(0)
topleft = (50,50)
bottomright = (300,300)

point =(200,200)
radius=50
def click(event,x,y,flag,param):
    global point,pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print("in pressed",x,y)
        point =(x,y)
cv2.namedWindow("camera")
cv2.setMouseCallback("camera",click)

while(cap.isOpened()):
    ret,frame=cap.read()
    
    cv2.line(frame, topleft ,bottomright,(0,255,0),5)
    
    cv2.rectangle(frame,[pt+30 for pt in  topleft], [pt-30 for pt in bottomright],(0,0,255),5)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'me',[pt+80 for pt in topleft],font,2,(0,255,255),10)
    key=cv2.waitKey(33)  
    cv2.imshow("camera",frame)
    if key & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()