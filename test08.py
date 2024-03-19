import numpy as np
import cv2

cap= cv2.VideoCapture("movie.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

frame_pos = cap.get(cv2.CAP_PROP_POS_FRAMES)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 360) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 860)   

while(cap.isOpened()):
    
    
    if (frame_pos == frame_count):
        cap.open("movie.mp4")
    ret,frame = cap.read()
    cv2.imshow("frame",frame)
    
    key=cv2.waitKey(33)  
    
    if key & 0xFF ==ord('l'):
        print("캡쳐")
        cv2.imwrite("D:/" + str(now) + ".png", frame)
        now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    if key & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()