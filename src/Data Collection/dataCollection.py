import sys
import csv
import glob
import os
import image_slicer as slicer
import pandas as pd
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

slices = 25 # number of slices
ext = "jpg" # extension of images
pBarCount = 0 # progressBar counter

val = open("initialVal.txt", "r")
ini = int(val.read())
val.close() # recover last known index of images

class mainApp(QtGui.QDialog, mainGUI.mainFrame):
	def __init__(self):
		super(self.__class__, self).__init__()
		os.chdir("Resources/Images")
		self.files = glob.glob("*.%s" %(ext)) # read all images from "Resources/Images"
		os.chdir("../..")
		self.imgCount = -1
		self.dim = int(sqrt(slices))
		self.setupUI(self)
		self.setButtons()
		self.Next.clicked.connect(self.nextImg)
	
	"""
	Function that attaches click events to every button
	Every button will send a different parameter
	"""
	def setButtons(self):
		for i in range(self.dim):
			for j in range(self.dim):
				self.arr[(i,j)].clicked.connect(partial(self.toCSV, (i+1,j+1)))

	"""
	Function that writes to a CSV the imageName slice and its output (Mowed, Unmowed, Irrelevant, Unknown)
	@param imgID: the ID of the button that call the function
	"""
	def toCSV(self, imgID):
		global pBarCount
		if self.imgCount != -1: # check that is not the first screen
			if self.en[(imgID[0]-1, imgID[1]-1)]: # check if button is enable
				#setup variables to update GUI and CSV
				toStr = ""
				pBarCount += 1 # increment progressBar counter
				data = pd.read_csv("mowmowData.csv") # read dataset
				imgFile, ignore = os.path.splitext(self.files[self.imgCount])
				imgName = "%s_%02d_%02d.png" %(imgFile, imgID[0], imgID[1]) # get image file name
				output = str(self.cBox.currentText()) # get text from comboBox aka output
				icon = self.getIcon("Resources/%s.png" %(output)); # get output icon

				#Update GUI components
				self.pBar.setProperty("value", pBarCount*100.0/slices) # update progressBar (%)
				self.en[(imgID[0]-1, imgID[1]-1)] = False # disable button
				self.arr[(imgID[0]-1, imgID[1]-1)].setIcon(icon) # replace image icon with output icon
				
				if data["ImageName"].str.contains(imgName).any(): #replace output if it exist
					data.loc[data["ImageName"] == imgName, "Output"] = output
					toStr = "Replaced Data in %s" %(imgName)
				else: #add new data if it's new
					toAdd = pd.DataFrame([[imgName, output]], columns=["ImageName", "Output"])
					data = data.append(toAdd, ignore_index=True)
					toStr = "Added Data for %s" %(imgName)
				print(toStr)
				data.to_csv("mowmowData.csv", index=False) #write to CSV
			else: #if button is disable
				pBarCount -= 1 #decrement progressBar counter
				self.pBar.setProperty("value", pBarCount*100.0/slices) # update progressBar (%)
				self.en[(imgID[0]-1, imgID[1]-1)] = True # enable button
				imgFile, ignore = os.path.splitext(self.files[self.imgCount])
				imgFile = "Resources/Images/%s_slices/%s_%02d_%02d.png" %(imgFile, imgFile, imgID[0], imgID[1])
				icon = self.getIcon(imgFile) # get image icon
				self.arr[(imgID[0]-1, imgID[1]-1)].setIcon(icon) # replace output icon with image icon

	"""
	Function that fetches next image and reset GUI components
	"""
	def nextImg(self):
		global pBarCount
		if self.pBar.value() != 100: # if progressBar is not 100% print a warning
			print("You need to finish labeling %d images" %(slices-pBarCount))
		else: # if progressBar is 100%
			if self.imgCount == -1: #get proper index when (only executes once at the beginning)
				self.imgCount = ini-1
			self.imgCount += 1 # increment image counter
			if self.imgCount >= len(self.files): # check if you have labeled ALL images
				print("No more images to calculate :)")
				exit(2)
			self.updateCounter() # save image counter to file
			pBarCount = 0 # reset progressBar counter
			imgFile, ignore = os.path.splitext(self.files[self.imgCount])
			imgName = "Resources/Images/%s.%s" %(imgFile, ext) # get image and its path
			
			self.pBar.setProperty("value", pBarCount) # update progressBar (%)
			self.imageName.setText("<< %s.%s >>" %(imgFile, ext)) #update label in GUI
			try:
				tiles = slicer.slice(imgName, slices, False) #slice image
				direc = os.path.dirname("Resources/Images/%s_slices/" %(imgFile))
				if not os.path.exists(direc):
					os.makedirs(direc) # if path doesn't exist create directory
				slicer.save_tiles(tiles, prefix = imgFile, directory = direc) # save slices to directory
			except Exception as err:
				print(err)
				sys.exit(1)
			for i in range(self.dim):
				for j in range(self.dim): #updates button
					imgName = "Resources/Images/%s_slices/%s_%02d_%02d.png" %(imgFile, imgFile, i+1, j+1)
					icon = self.getIcon(imgName)
					self.en[(i,j)] = True #enable button
					self.arr[(i,j)].setIcon(icon) # sets new icons

	"""
	Function that writes image counter to text file for future runs of the program
	"""
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