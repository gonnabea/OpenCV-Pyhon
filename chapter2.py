import cv2
import numpy as np

img = cv2.imread("Resources/gentlemen.jpg")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7), 0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray) # 흑백 이미지
cv2.imshow("Blur Image", imgBlur) # 흑백 + 블러 효과
cv2.imshow("Canny Image", imgCanny) # 외곽선 검출 이미지
cv2.imshow("Dialation Image", imgDialation) # 외곽선 팽창시키기
cv2.imshow("Eroded Image", imgEroded) # 외곽선 검출 수축시키기

cv2.waitKey(0)