import cv2
import numpy as np

class frameOverlayer:

	"""
	Constructors of the class
	@param imgNamne: the name of the image to be read
	"""
	def __init__(self, imgName):
		self.frame = cv2.imread(imgName)
		self.original = cv2.imread(imgName)
		self.per = 0.25

	"""
	This function changes the image in case a new image needs to be used!
	@param imgName: the name of new Image to be read
	"""
	def setImage(self, imgName):
		self.frame = cv2.imread(imgName)
		self.original = cv2.imread(imgName)

	"""
	Functions that created the overlay depending on the classification of the image frames
	@param classification: the type of classification provided by the CNN
	@param imageDimensions: the dimensions of the image
	@param squareRootOfNumSlices: the number of rows/columns in the image
	@param coordinates: the frame location in respect of the overall picture
	"""
	def overlayRectangle(self, classification, imageDimensions, squareRootOfNumSlices, coordinates):
		self.dim = imageDimensions
		pixelsX, pixelsY = imageDimensions
		cy, cx = coordinates

		rectHeight = pixelsY / squareRootOfNumSlices
		rectWidth = pixelsX / squareRootOfNumSlices

		rectX = rectWidth * (cx - 1)
		rectY = rectHeight * (cy - 1)

		if classification == 1:
			color = (0, 255, 255) # Mowed, YELLOW
		elif classification == 2:
			color = (0, 255, 0) # Unmowed, GREEN
		elif classification == 3:
			color = (0, 0, 255) # Irrelevant, RED
		elif classification == 4:
			color = (255, 0, 0) # Unknown, BLUE

		cv2.rectangle(self.frame, (rectX, rectY), (rectX+rectWidth, rectY+rectHeight), color, -1)
		if coordinates == (10, 10):
			alpha = 0.5
			cv2.addWeighted(self.frame, alpha, self.original, 1-alpha, 0, self.frame)

	"""
	Displays the image with the overlay for a finite amount
	@param time: optional parameters that determinate how long the image is displayed time = 0 will cause to be indefinite 
	"""
	def display(self, time=0):
		cv2.namedWindow("Overlay Picture", cv2.WINDOW_NORMAL)
		cv2.resizeWindow("Overlay Picture", int(self.dim[0]*self.per), int(self.dim[1]*self.per))
		cv2.moveWindow("Overlay Picture", 20, 20)
		cv2.imshow("Overlay Picture", self.frame)
		cv2.waitKey(time*1000)
		cv2.destroyAllWindows()

if __name__ == "__main__":
	over = frameOverlayer("testingImage.jpg")
	items = np.array([1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4])
	items = items.reshape(10,10)
	for i in range(1, 11):
		for j in range(1, 11):
			over.overlayRectangle(items[i-1][j-1], (1280, 720), 10, (i, j))

	over.display(0)



