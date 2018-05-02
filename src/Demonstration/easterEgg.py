import cv2

# This class just displays an animation of a coin flip :)
class easterEgg:
	def __init__(self):
		self.counter = 0

	def flip(self):
		self.counter = (self.counter + 1) % 44
		img = cv2.imread("coin/coin%0.2d.png" %(self.counter))
		cv2.moveWindow("coin flip", 50, 50)
		cv2.imshow("coin flip", img)
		cv2.waitKey(1)

	def destroy(self):
		cv2.destroyAllWindows()

if __name__ == "__main__":
	coin = easternEgg()
	while(1):
		coin.flip()