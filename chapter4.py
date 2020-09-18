import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)
# img[200:300,100:300] = 255,0,0


cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # ((출발 X좌표, 출발 Y좌표), (엔드포인트 X좌표, 엔드포인트 Y좌표), BGR 색깔, 선 굵기)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) # ((출발 X좌표, 출발 Y좌표), (엔드포인트 X좌표, 엔드포인트 Y좌표), BGR 색깔, 선 굵기)
cv2.circle(img,(400,50),50,(255,255,0),5) # ((출발 X좌표, 출발 Y좌표), 너비, BGR 색깔, 선 굵기)
cv2.putText(img, "OPENCV", (300,200), cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1) # (내용, 위치, 글씨체, 스케일, 색깔, 굵기)

cv2.imshow("Image", img)

cv2.waitKey(0)