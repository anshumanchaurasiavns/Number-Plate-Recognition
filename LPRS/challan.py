# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'challan.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import mysql.connector
from PyQt5.QtGui import *
from challan2 import *
import Main1


pno="x23z"
class Ui_Form1(object):
    location=''
    fname=''
    ext=''
    def processimg(self):
        global pno
        #print(pno)
        #wn6 = AppWindow3()
        #wn2.setpln(pno)
        wn2.ui.execute(self)
        wn2.show()
        wn1.hide()
        

    def image(self):
        location=self.lineEdit.text()
        fname=location+'\\'+self.lineEdit_2.text()
        ext=fname+'.'+self.lineEdit_3.text()
        print(ext)
        self.label_5.setPixmap(QtGui.QPixmap(ext))
        Main1.main(ext)
        
    def setupUi1(self,Form):
        Form.setObjectName("Form")
        Form.resize(1093, 731)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1091, 731))
        self.frame.setStyleSheet("background-color: #3366CC;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(70, 60, 921, 581))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("Background-color:white;\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(530, 90, 371, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("Background-color:white;\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 150, 371, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("Background-color:white;\n"
"\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 210, 371, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("Background-color:white;\n"
"\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(440, 90, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(410, 150, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(400, 210, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(530, 340, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("Background-color:white;background-color: #4CAF50; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;border-radius: 12px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.image)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 340, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("Background-color:white;background-color: #4CAF50; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;border-radius: 12px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(420, 270, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(530, 270, 371, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("Background-color:white;\n"
"\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 420, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("Background-color:white;background-color: #4CAF50; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;border-radius: 12px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 351, 401))
        self.label_5.setText("")
#        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/Anshuman/source/repos/LPRS/LPRS/carimg/5.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(120, 30, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Challan"))
        self.label.setText(_translate("Form", "Location"))
        self.label_2.setText(_translate("Form", "Image Name"))
        self.label_3.setText(_translate("Form", "File extension"))
        self.pushButton.setText(_translate("Form", "Choose Image"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        self.label_4.setText(_translate("Form", "Image Size"))
        self.pushButton_3.setText(_translate("Form", "Process Image"))
        self.label_6.setText(_translate("Form", "Image Preview"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Video"))
        self.pushButton_3.clicked.connect(self.processimg)


class AppWindow2(QDialog,QApplication):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form1()
        self.ui.setupUi1(self)

    def setpln(self,pno1):
        global pno
        pno=pno1
        print(pno+"pno\n"+pno1+"pno1challan")
        
app = QApplication(sys.argv)
wn1 = AppWindow2()
'''wn1.show()
sys.exit(app.exec_())       
this is removed one runing as whole and show'''
        
        



