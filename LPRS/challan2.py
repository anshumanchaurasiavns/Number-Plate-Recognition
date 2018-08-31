# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'challan2.ui'
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
from challan3 import *

pno=''
class Ui_Form2(object):
    sav=0
    def disp(self, Form):
        global pno
        self.lineEdit.setText(pno)

    def challan3(self, Form):
        global pno
        if(self.sav==0):
            print("nothinghere")
            ptype=self.lineEdit_6.text()
            vehicle=self.lineEdit_7.text()
            oname=self.lineEdit_2.text()
            mob=self.lineEdit_3.text()
            email=self.lineEdit_4.text()
            hadd=self.lineEdit_5.text()
            cnx = mysql.connector.connect(user='root', password='',host='localhost',database='plates')
            conn=cnx.cursor()
            result=conn.execute("insert into plate(lpno,ptype,vehicle,oname,mno,email,hadd) values('"+pno+"','"+ptype+"','"+vehicle+"','"+oname+"','"+mob+"','"+email+"','"+hadd+"')")
            print(result)
        wn3.setplno(pno)
        wn3.show()
        wn2.hide()

    def execute(self, Form):
        global pno
        print("executepo"+pno)
        self.lineEdit.setText(pno)
        self.disp(self)
        cnx = mysql.connector.connect(user='root', password='',host='localhost',database='plates')
        conn=cnx.cursor()
        sql="select * from plate where lpno='"+pno+"'"
        #sql="select * from plate"
        print(sql)
        conn.execute(sql)
        data=conn.fetchall()
        for i in data:
            self.lineEdit_6.setText(i[2])
            self.lineEdit_7.setText(i[3])
            self.lineEdit_2.setText(i[4])
            self.lineEdit_3.setText(i[5])
            self.lineEdit_4.setText(i[6])
            self.lineEdit_5.setText(i[7])
            save=1
        
    def enb(self, Form):
        self.lineEdit.setEnabled(True)

    def setupUi2(self, Form):
        Form.setObjectName("Form")
        Form.resize(1172, 802)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1171, 801))
        self.frame.setStyleSheet("background-color: #3366CC;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(120, 100, 961, 591))
        self.frame_2.setStyleSheet("Background-color:white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(40, 70, 291, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/OpenCV_3_License_Plate_Recognition_Python-master/Licence Plate Recogination System/3.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(430, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(530, 70, 271, 22))
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(820, 70, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.enb)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(400, 220, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 220, 271, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(420, 270, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 270, 271, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(530, 320, 271, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(420, 320, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(410, 370, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(530, 370, 271, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(530, 120, 271, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(420, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(530, 170, 271, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(430, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 430, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Image Preview"))
        self.label_3.setText(_translate("Form", "Plate No."))
        self.pushButton.setText(_translate("Form", "Edit"))
        self.label_4.setText(_translate("Form", "Owner Name"))
        self.label_5.setText(_translate("Form", "Mobile No."))
        self.label_6.setText(_translate("Form", "Email Add."))
        self.label_7.setText(_translate("Form", "House Add."))
        self.label_8.setText(_translate("Form", "Plate Type"))
        self.label_9.setText(_translate("Form", "Car/bike"))
        self.pushButton_2.setText(_translate("Form", "Challan"))
        self.pushButton_2.clicked.connect(self.challan3)

class AppWindow3(QDialog,QApplication):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form2()
        self.ui.setupUi2(self)
        #self.ui.execute(self)

    def setpln(self,pno1):
        global pno
        pno=pno1
        print(pno+"pno\n"+pno1+"pno1challan2")
        
app = QApplication(sys.argv)
wn2 = AppWindow3()
print("challan2")
'''wn2.show()
sys.exit(app.exec_())       
this is removed one runing as whole and show'''


