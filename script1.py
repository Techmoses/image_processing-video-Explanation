import cv2
print("Package import")

img = cv2.imread("photo4.jpg")

cv2.imshow("Output",img)
cv2.waitKey(0)
