import cv2

src=cv2.imread("cat.jpg",cv2.IMREAD_COLOR)
gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

sobel=cv2.Sobel(gray,cv2.CV_8U,1,0,3)
can=cv2.Canny(gray,cv2.CV_8U,1,0,3)
cv2.imshow("src",sobel)
cv2.imshow("src",can)
cv2.waitKey()
cv2.destroyAllWindows()
