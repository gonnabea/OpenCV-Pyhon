import cv2

# img = cv2.imread("Resources/gentlemen.jpg")
#
# cv2.imshow("Output", img)
#
# cv2.waitKey(0) // 이미지 불러오기

# cap = cv2.VideoCapture("Resources/sample.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(delay=1) & 0xFF == ord('q'):
#         break // 특정 경로로 비디오 불러오기

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(10, 120)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(delay=1) & 0xFF == ord('q'):
#         break // 웹캠 사용
