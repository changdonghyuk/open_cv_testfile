import cv2

src=cv2.imread("cat.jpg",cv2.IMREAD_COLOR)
dst=cv2.blur(src,(2,2),anchor=(-1,-1),borderType=cv2.BORDER_CONSTANT)

cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()

