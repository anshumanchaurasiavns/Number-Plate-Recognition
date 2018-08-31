# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QDialog, QApplication
from challan import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import mysql.connector
from PyQt5.QtGui import *
import sys

class Ui_Form(object):
    def challan(self,Form):
        w1 = AppWindow2()
        self.lbl = QtWidgets.QLabel(self.frame_4)
        self.lbl.setGeometry(QtCore.QRect(-30, 0, 381, 121))
        self.lbl.setText("Anything else here")
        self.lbl.setObjectName("label")
        # wn.hide()
        wn1.show()


    def home(self,Form):
        pass

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(1564, 880)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1561, 121))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color: white;")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(-30, 0, 381, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/logo3.png"))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(1140, 0, 421, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(110, 30, 115, 26))
        self.comboBox.setStyleSheet("<html>\n"
"<body>\n"
"Resources\n"
"</body>\n"
"</html>")
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/images.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/contactus.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/feedback1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/aboutus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon4, "")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setGeometry(QtCore.QRect(250, 30, 100, 26))
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setMaxVisibleItems(10)
        self.comboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_2.setMinimumContentsLength(0)
        self.comboBox_2.setModelColumn(0)
        self.comboBox_2.setObjectName("comboBox_2")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/images (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_2.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/logout.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_2.addItem(icon6, "")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(0, 120, 341, 821))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.dockWidget = QtWidgets.QDockWidget(self.frame_3)
        self.dockWidget.setGeometry(QtCore.QRect(0, 440, 341, 381))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidget.setEnabled(False)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.textEdit = QtWidgets.QTextEdit(self.dockWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(0, -10, 341, 361))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton.setStyleSheet("background-color:#3366CC;color:white;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 110, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:#3366CC;color:white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 220, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:#3366CC;color:white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 330, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:#3366CC;color:white;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(340, 120, 1221, 751))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setStyleSheet("background-color:white;")

        self.retranslateUi(Form)
        self.comboBox_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Number Plate Recognitation System"))
        self.comboBox.setItemText(0, _translate("Form", "Resources"))
        self.comboBox.setItemText(1, _translate("Form", "Contact Us"))
        self.comboBox.setItemText(2, _translate("Form", "Feadback"))
        self.comboBox.setItemText(3, _translate("Form", "About Us"))
        self.comboBox_2.setItemText(0, _translate("Form", "Account"))
        self.comboBox_2.setItemText(1, _translate("Form", "Logout"))
        self.dockWidget.setWindowTitle(_translate("Form", "Recent Items"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Aything</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Like This</p></body></html>"))
        self.pushButton.setText(_translate("Form", "Home"))
        self.pushButton.clicked.connect(self.home)
        self.pushButton_2.setText(_translate("Form", "Challan"))
        self.pushButton_2.clicked.connect(self.challan)
        self.pushButton_3.setText(_translate("Form", "Search"))
        self.pushButton_4.setText(_translate("Form", "Inquiry"))


class AppWindow1(QDialog,QApplication):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.show()
        
        

app = QApplication(sys.argv)
wn = AppWindow1()
'''sys.exit(app.exec_())'''
'''this is removed one runing as whole and show
wn.show()
sys.exit(app.exec_())'''


