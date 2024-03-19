import cv2
import numpy as np

src=cv2.imread("ap.jpg",cv2.IMREAD_COLOR)
height,width,channel=src.shape
zero=np.zeros((height,width,1),dtype=np.uint8)
bgz=cv2.merge((b,g,zero))

b= src[:,:,0]
g= src[:,:,1]
r= src[:,:,2]
#b,g,r =cv2.split(src)
#inverse=cv2.merge((b,g,r))

cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
#cv2.imshow("inverse",inverse)
cv2.waitKey()
cv2.destroyAllWindows()
