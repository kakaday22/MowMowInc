import cv2
import sys

videoFile = sys.argv[1] # get filePath to video from the command line as an argument
vidcap = cv2.VideoCapture(videoFile) # open file
status, img = vidcap.read()
count = 0
while status: # save each frame of the video until there are no more frames
	cv2.imwrite("Resources/Images/image%d.png" %(count), img)
	count += 1
	status, img = vidcap.read()

print("Done")