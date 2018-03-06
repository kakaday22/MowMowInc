# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import numpy as np

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(connectSlotsByNameext, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class mainFrame(object):
	def setupUI(self, Frame):
		dimension = (self.dim,self.dim)
		imgQlty = (640,480)
		crossSize = (imgQlty[0]/self.dim, imgQlty[1]/self.dim)
		self.Frame = Frame
		height = 70+dimension[1]*(crossSize[1]+2)
		defaultSize = (38+dimension[0]*(crossSize[0]+2), height+70)
		minSize = maxSize = defaultSize
		self.setFrame(defaultSize, minSize, maxSize)		
		self.createPB(dimension, crossSize)
		self.createComboBox()
		self.createProgressBar()
		
		self.imageName = QtGui.QLabel(self.Frame)
		self.imageName.setGeometry(QtCore.QRect((defaultSize[0]/2-100),40,200,23))
		self.imageName.setMinimumSize(QtCore.QSize(200,23))
		self.imageName.setMaximumSize(QtCore.QSize(200,23))
		self.imageName.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.imageName.setAlignment(QtCore.Qt.AlignCenter)
		self.imageName.setText(_fromUtf8("PRESS NEXT"))
		
		self.Next = QtGui.QPushButton(self.Frame)
		self.Next.setGeometry(QtCore.QRect((defaultSize[0]/2-40),height,80,50)) # 310
		self.Next.setMinimumSize(QtCore.QSize(80,50))
		self.Next.setMaximumSize(QtCore.QSize(80,50))
		self.Next.setObjectName(_fromUtf8("Next"))

		self.restrainlateUi()
		QtCore.QMetaObject.connectSlotsByName(self.Frame)

	def setFrame(self, defaultSize, minSize, maxSize):
		self.Frame.setObjectName(_fromUtf8("Data Collection"))
		self.Frame.setEnabled(True)
		self.Frame.resize(*defaultSize)
		self.Frame.setMinimumSize(QtCore.QSize(*minSize))
		self.Frame.setMaximumSize(QtCore.QSize(*maxSize))

	"""
	Function that creates buttons
	@param num: number of buttons to create
	@param imgSize, size of the image
	""" 
	def createPB(self, num, imgSize):
		self.arr = {} # initialize empty button list
		self.en = {} # initialize empty enable list
		currSettings = [20,70,imgSize[0], imgSize[1]] #default position and image size
		imgName = "Resources/blank.png"
		icon  = self.getIcon(imgName) # get default icon
		for i in range(num[0]): #for every row
			for j in range(num[1]): #for every col
				self.en[(i,j)] = True # enable button
				self.arr[(i,j)] = QtGui.QPushButton(self.Frame) #creates instance of button
				self.arr[(i,j)].setGeometry(QtCore.QRect(*tuple(currSettings))) #sets default sizes and position
				self.arr[(i,j)].setMinimumSize(QtCore.QSize(*imgSize)) # set minimum size
				self.arr[(i,j)].setMaximumSize(QtCore.QSize(*imgSize)) # set maximum size
				self.arr[(i,j)].setIcon(icon) # sets icon (black screen)
				self.arr[(i,j)].setIconSize(QtCore.QSize(*imgSize)) # sets icon size
				self.arr[(i,j)].setObjectName(_fromUtf8("(%d,%d)" %(i,j))) # set object name
				currSettings[0] += imgSize[0]+2 # math to position button every col
			currSettings[0] = 20 # reset col position to initial
			currSettings[1] += imgSize[1]+2 # math to position button every row


	"""
	Function that creates comboBoxex
	"""
	def createComboBox(self):
		self.cBox = QtGui.QComboBox(self.Frame) # create instance of comboBox
		self.cBox.setGeometry(QtCore.QRect(20,40,81,23)) # sets default sizes and positions
		self.cBox.setEditable(False) # disable editable (so no one can add custom labels)
		self.cBox.setMaxVisibleItems(4) # set visible items
		self.cBox.setObjectName(_fromUtf8("comboBox")) #set object name
		self.cBox.addItem(_fromUtf8("Mowed"))  # add items
		self.cBox.addItem(_fromUtf8("Unmowed")) # add items
		self.cBox.addItem(_fromUtf8("Irrelevant")) # add items
		self.cBox.addItem(_fromUtf8("Unknown")) # add items


	"""
	Function that creates progressBars
	"""
	def createProgressBar(self):
		self.pBar = QtGui.QProgressBar(self.Frame) #create instance of progressBar
		self.pBar.setGeometry(QtCore.QRect(150, 10, 200, 23)) # sets default sizes and positions
		self.pBar.setMinimumSize(QtCore.QSize(200, 23)) # set minimum size
		self.pBar.setMaximumSize(QtCore.QSize(200, 23)) # set maximum size
		self.pBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu) # no idea what this is :)
		self.pBar.setAcceptDrops(False) # no idea :o
		self.pBar.setAutoFillBackground(False) # no idea :o
		self.pBar.setProperty("value", 100) # set current (%)
		self.pBar.setObjectName(_fromUtf8("progressBar")) # set object Name


	"""
	Function that creates and returns an icon object
	@param img, image path of the icon to create
	@return the icon
	"""
	def getIcon(self, img):
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(img)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		return icon

	"""
	function that sets some other properties
	"""
	def restrainlateUi(self):
		self.Frame.setWindowTitle(_translate("Frame", "MowMow Inc Data Collection Tool", None))
		self.Next.setText(_translate("Frame", "Next", None))