import numpy as np
import cv2

cap =cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_file='output.mp4'
fps=30
w = 640#1280#1920
h = 480#720#1080
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,h)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,w)
out=cv2.VideoWriter(output_file,fps,fourcc,(w,h))

while(cap.isOpened()):
    
    ret,frame = cap.read()
    if ret is False:
        print("cant camera")
        break
    
    cv2.imshow("Camera",frame)
    out.write(frame)
    key=cv2.waitKey(1)  
    
    if key & 0xFF ==ord('l'):
        print("캡쳐")
        cv2.imwrite("D:/" + str(now) + ".png", frame)
        now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    if key & 0xFF == ord('q'):
        break
 
cap.release()
out.release()
cv2.destroyAllWindows()