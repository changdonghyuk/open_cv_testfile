import numpy as np
import cv2
cap =cv2.VideoCapture(0)
topleft = (0,300)
fontsize= 0
bold = 0

def on_bold_trackbar(value):
    global bold
    bold = value
def on_fontsize_trackbar(value):
    global fontsize
    fontsize =value

cv2.namedWindow("camera")
cv2.createTrackbar("bold","camera",bold,10,on_bold_trackbar)
cv2.createTrackbar("fontsize","camera",fontsize,50,on_fontsize_trackbar)
while(cap.isOpened()):
    ret,frame= cap.read()
    if ret is False:
        print("can't receive")
        break
    key=cv2.waitKey(1)  
    cv2.putText(frame,"TEXT",topleft,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(0,255,255),1+bold)
    cv2.putText(frame,"TEXT",topleft,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(0,255,255),1+fontsize)
    cv2.imshow("camera",frame) 
    if key & 0xFF ==ord('l'):
        print("캡쳐")
        cv2.imwrite("./" + str(now) + ".jpg", frame)
        now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    if key & 0xFF == ord('q'):
        break

  
cap.release()
cv2.destroyAllWindows()