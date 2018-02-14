import cv2
import sys

videoFile = sys.argv[1]
vidcap = cv2.VideoCapture(videoFile)
status, img = vidcap.read()
count = 0
while status:
	cv2.imwrite("Resources/Images/image%d.png" %(count), img)
	count += 1
	status, img = vidcap.read()

print("Done")