import cv2
import numpy as np
import time
import image_slicer as slicer

"""
Camera class that helps to capture image or videos
"""

class Camera:
	"""
	Initializer
	@param x: the camera you are trying to connect to
		0 for internal camera
		some# for USB cameras usually 1
	"""
	def __init__(self, x):
		self.cam = cv2.VideoCapture(x)
		self.i = 0
		self.v = 0

	# When destroying the object close the camera
	def __del__(self):
		self.cam.release()

	"""
	function to capture and slice images
	@param slices: the number of slices to slice the newly capture image
	"""
	def captureImage(self, slices):
		ret, frame = self.cam.read()
		fileName = "Resources/Images/image%d.png" %(self.i)
		self.i = self.i + 1
		cv2.imwrite(fileName, frame)
		slicer.slice(fileName, slices)

	"""
	function to capture videos
	@param fps: the number of frames per second you want to make the video
	@param length: the number of seconds you want the video to last
	"""
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