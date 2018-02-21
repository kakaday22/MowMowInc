# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainGUI.ui'
#
# Created: Thu Feb 15 14:26:22 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.setEnabled(True)
        Frame.resize(500, 350)
        Frame.setMinimumSize(QtCore.QSize(500, 350))
        Frame.setMaximumSize(QtCore.QSize(500, 350))
        self.progressBar = QtGui.QProgressBar(Frame)
        self.progressBar.setGeometry(QtCore.QRect(150, 10, 200, 23))
        self.progressBar.setMinimumSize(QtCore.QSize(200, 23))
        self.progressBar.setMaximumSize(QtCore.QSize(200, 23))
        self.progressBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pbUnknown = QtGui.QPushButton(Frame)
        self.pbUnknown.setGeometry(QtCore.QRect(310, 310, 80, 23))
        self.pbUnknown.setMinimumSize(QtCore.QSize(80, 23))
        self.pbUnknown.setMaximumSize(QtCore.QSize(80, 23))
        self.pbUnknown.setObjectName(_fromUtf8("pbUnknown"))
        self.pbUnmowed = QtGui.QPushButton(Frame)
        self.pbUnmowed.setGeometry(QtCore.QRect(210, 310, 80, 23))
        self.pbUnmowed.setMinimumSize(QtCore.QSize(80, 23))
        self.pbUnmowed.setMaximumSize(QtCore.QSize(80, 23))
        self.pbUnmowed.setObjectName(_fromUtf8("pbUnmowed"))
        self.pbMowed = QtGui.QPushButton(Frame)
        self.pbMowed.setGeometry(QtCore.QRect(110, 310, 80, 23))
        self.pbMowed.setMinimumSize(QtCore.QSize(80, 23))
        self.pbMowed.setMaximumSize(QtCore.QSize(80, 23))
        self.pbMowed.setObjectName(_fromUtf8("pbMowed"))
        self.imageName = QtGui.QLabel(Frame)
        self.imageName.setGeometry(QtCore.QRect(150, 40, 200, 23))
        self.imageName.setMinimumSize(QtCore.QSize(200, 23))
        self.imageName.setMaximumSize(QtCore.QSize(200, 23))
        self.imageName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.imageName.setAlignment(QtCore.Qt.AlignCenter)
        self.imageName.setObjectName(_fromUtf8("imageName"))
        self.i0 = QtGui.QPushButton(Frame)
        self.i0.setGeometry(QtCore.QRect(20, 70, 100, 100))
        self.i0.setMinimumSize(QtCore.QSize(100, 100))
        self.i0.setMaximumSize(QtCore.QSize(100, 100))
        self.i0.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/pokeball.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.i0.setIcon(icon)
        self.i0.setIconSize(QtCore.QSize(100, 100))
        self.i0.setObjectName(_fromUtf8("i0"))
        self.i1 = QtGui.QPushButton(Frame)
        self.i1.setGeometry(QtCore.QRect(120, 70, 100, 100))
        self.i1.setMinimumSize(QtCore.QSize(100, 100))
        self.i1.setMaximumSize(QtCore.QSize(100, 100))
        self.i1.setText(_fromUtf8(""))
        self.i1.setIcon(icon)
        self.i1.setIconSize(QtCore.QSize(100, 100))
        self.i1.setObjectName(_fromUtf8("i1"))
        self.i2 = QtGui.QPushButton(Frame)
        self.i2.setGeometry(QtCore.QRect(20, 170, 100, 100))
        self.i2.setMinimumSize(QtCore.QSize(100, 100))
        self.i2.setMaximumSize(QtCore.QSize(100, 100))
        self.i2.setText(_fromUtf8(""))
        self.i2.setIcon(icon)
        self.i2.setIconSize(QtCore.QSize(100, 100))
        self.i2.setObjectName(_fromUtf8("i2"))
        self.i3 = QtGui.QPushButton(Frame)
        self.i3.setGeometry(QtCore.QRect(120, 170, 100, 100))
        self.i3.setMinimumSize(QtCore.QSize(100, 100))
        self.i3.setMaximumSize(QtCore.QSize(100, 100))
        self.i3.setText(_fromUtf8(""))
        self.i3.setIcon(icon)
        self.i3.setIconSize(QtCore.QSize(100, 100))
        self.i3.setObjectName(_fromUtf8("i3"))
        self.comboBox = QtGui.QComboBox(Frame)
        self.comboBox.setGeometry(QtCore.QRect(300, 120, 81, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setMaxVisibleItems(1)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(290, 200, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Frame)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Dialog", None))
        self.pbUnknown.setText(_translate("Frame", "Unknown", None))
        self.pbUnmowed.setText(_translate("Frame", "Unmowed", None))
        self.pbMowed.setText(_translate("Frame", "Mowed", None))
        self.imageName.setText(_translate("Frame", "<ImgName Goes Here>", None))
        self.comboBox.setItemText(0, _translate("Frame", "Mowed", None))
        self.comboBox.setItemText(1, _translate("Frame", "Unmowed", None))
        self.comboBox.setItemText(2, _translate("Frame", "Irrelevant", None))
        self.pushButton.setText(_translate("Frame", "PushButton", None))

