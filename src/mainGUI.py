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
	def _translate(context, text, disambig):
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

	def createPB(self, num, imgSize):
		self.arr = {}
		self.en = {}
		currSettings = [20,70,imgSize[0], imgSize[1]]
		imgName = "Resources/blank.png"
		icon  = self.getIcon(imgName)
		for i in range(num[0]): #for every row
			for j in range(num[1]): #for every col
				self.en[(i,j)] = True
				self.arr[(i,j)] = QtGui.QPushButton(self.Frame)
				self.arr[(i,j)].setGeometry(QtCore.QRect(*tuple(currSettings)))
				self.arr[(i,j)].setMinimumSize(QtCore.QSize(*imgSize))
				self.arr[(i,j)].setMaximumSize(QtCore.QSize(*imgSize))
				# self.arr[(i,j)].setText(_fromUtf8(imgName))
				self.arr[(i,j)].setIcon(icon)
				self.arr[(i,j)].setIconSize(QtCore.QSize(*imgSize))
				self.arr[(i,j)].setObjectName(_fromUtf8("(%d,%d)" %(i,j)))
				currSettings[0] += imgSize[0]+2
			currSettings[0] = 20
			currSettings[1] += imgSize[1]+2

	def createComboBox(self):
		self.cBox = QtGui.QComboBox(self.Frame)
		self.cBox.setGeometry(QtCore.QRect(20,40,81,23))
		self.cBox.setEditable(False)
		self.cBox.setMaxVisibleItems(4)
		self.cBox.setObjectName(_fromUtf8("comboBox"))
		self.cBox.addItem(_fromUtf8("Mowed"))
		self.cBox.addItem(_fromUtf8("Unmowed"))
		self.cBox.addItem(_fromUtf8("Irrelevant"))
		self.cBox.addItem(_fromUtf8("Unknown"))

	def getIcon(self, img):
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(img)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		return icon

	def restrainlateUi(self):
		self.Frame.setWindowTitle(_translate("Frame", "MowMow Inc Data Collection Tool", None))
		self.Next.setText(_translate("Frame", "Next", None))