import sys
import csv
import image_slicer as slicer
import glob
import os
from math import sqrt
from functools import partial

try:
	from PyQt4 import QtGui
except ImportError:
	__version__ = sys.version_info[0]
	if __version__ == 2:
		err = "sudo apt-get install python-qt4"
	elif __version__ == 3:
		err = "sudo apt-get install python3-qt4"
	print("Install PyQt4: %s" %(err))

import mainGUI

slices = 25	
ext = "jpg"

val = open("initialVal.txt", "r")
ini = int(val.read())
val.close()
class mainApp(QtGui.QDialog, mainGUI.mainFrame):
	def __init__(self):
		super(self.__class__, self).__init__()
		os.chdir("Resources/Images")
		self.files = glob.glob("*.%s" %(ext))
		os.chdir("../..")
		self.imgCount = -1
		self.bIcon = self.getIcon("Resources/blank.png")
		self.dim = int(sqrt(slices))
		self.setupUI(self)
		self.setButtons()
		self.Next.clicked.connect(self.nextImg)
	
	def setButtons(self):
		for i in range(self.dim):
			for j in range(self.dim):
				self.arr[(i,j)].clicked.connect(partial(self.toCSV, (i+1,j+1)))

	def toCSV(self, imgID):
		if self.imgCount != -1:
			if self.en[(imgID[0]-1, imgID[1]-1)]:
				self.en[(imgID[0]-1, imgID[1]-1)] = False
				imgFile, ignore = os.path.splitext(self.files[self.imgCount])
				imgName = "%s_%02d_%02d.png" %(imgFile, imgID[0], imgID[1])
				self.arr[(imgID[0]-1, imgID[1]-1)].setIcon(self.bIcon)
				currBox = self.cBox.currentText()
				output = "Mowed"*(currBox == "Mowed") + "Unmowed"*(currBox == "Unmowed") + "Irrelevant"*(currBox == "Irrelevant") + "Unknown"*(currBox == "Unknown")
				toStr = [imgName, output]
				print(toStr)
				with open("mowmowData.csv", "ab") as myFile:
					writer = csv.writer(myFile)
					writer.writerow(toStr)
			else:
				print("Segmentation Fault")

	#to change image, call getIcon with new image, call refreshButton (this method will use the new icon to change images), all calls are from NEXT BUTTON
	def nextImg(self):
		if self.imgCount == -1:
			self.imgCount = ini-1
		self.imgCount += 1
		self.updateCounter()
		imgFile, ignore = os.path.splitext(self.files[self.imgCount])
		self.imageName.setText("<< %s.%s >>" %(imgFile, ext))
		imgName = "Resources/Images/%s.%s" %(imgFile, ext)
		try:
			slicer.slice(imgName, slices)
		except Exception as err:
			print(err)
			sys.exit(1)
		for i in range(self.dim):
			for j in range(self.dim):
				imgName = "Resources/Images/%s_%02d_%02d.png" %(imgFile, i+1, j+1)
				icon = self.getIcon(imgName)
				self.en[(i,j)] = True
				self.arr[(i,j)].setIcon(icon)

	def updateCounter(self):
		val = open("initialVal.txt", "w")
		val.write("%d" %(self.imgCount))
		val.close()


def main():
	app = QtGui.QApplication(sys.argv)
	form = mainApp()
	form.show()
	app.exec_()

if __name__ == "__main__":
	if slices % sqrt(slices) == 0:
		main()
	else:
		print("Slices %d is not square rootable" %(slices))