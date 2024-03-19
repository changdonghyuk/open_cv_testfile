import cv2


src=cv2.imread("cat.jpg",cv2.IMREAD_COLOR)
dst=cv2.bitwise_not(src)
dst2=cv2.bitwise_xor(src)
dst3=cv2.bitwise_and(src)


cv2.imshow("src",src)
cv2.imshow("dst",dst)
cv2.imshow("dst2",dst2)
cv2.imshow("dst3",dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()