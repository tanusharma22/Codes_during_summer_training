import cv2
img = cv2.imread("rose.jpg")
img2 = cv2.imread("white.jpg")
print(img.shape)
print(img2.shape)
img2[0:100, 0:200]=img[0:100, 0:200]

cv2.imshow("edited",img2)
cv2.waitKey(0)
