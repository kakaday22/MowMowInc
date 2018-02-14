import cv2
import numpy as np
import time
import image_slicer as slicer

class Camera:
	def __init__(self, x):
		self.cam = cv2.VideoCapture(x)
		self.i = 0
		self.v = 0

	def __del__(self):
		self.cam.release()

	def captureImage(self, slices):
		ret, frame = self.cam.read()
		fileName = "Resources/Images/image%d.png" %(self.i)
		self.i = self.i + 1
		cv2.imwrite(fileName, frame)
		slicer.slice(fileName, slices)

	def captureVideo(self, fps, length):
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		fileName = "video%d_%dfps.avi" %(self.v, fps)
		self.v = self.v + 1
		out = cv2.VideoWriter(fileName, fourcc, fps, (640,480))
		for x in range(int(length*fps)):
			ret, frame = self.cam.read()
			if ret==True:
				out.write(frame)
			else:
				break


if __name__ == "__main__":
	web = Camera(1)
	web.captureImage(25)
	# web.captureVideo(30.0, 20)