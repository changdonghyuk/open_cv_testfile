import cv2

src=cv2.imread("cat.jpg",cv2.IMREAD_COLOR)
hsv=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)

lower_red=cv2.inRange(hsv,(0,50,100),(5,255,255))
upper_red=cv2.inRange(hsv,(0,50,100),(180,255,255))
added_red=cv2.addWeighted(lower_red,5.0,upper_red,5.0,0.0)

red=cv2.bitwise_and(hsv,hsv,mask=added_red)
red=cv2.cvtColor(red,cv2.COLOR_HSV2BGR)

cv2.imshow("src",red)
cv2.waitKey()
cv2.destroyAllWindows()
