# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Drivw E\BCS\Semester 3\Python\Project\Part 3\All Part 3\User Info.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import dbConnection as dConnectUser
from PyQt5.QtWidgets import QApplication
# from dbConnection as dConnectUser


class Ui_frmUserInfo(object):


    def setupUi(self, frmUserInfo):
                
        

        
        
        frmUserInfo.resize(550, 640)
        frmUserInfo.setWindowIcon(QIcon('UserInfo.png'))
        frmUserInfo.setWindowTitle("User Information")
        
        self.UserPanel = QtWidgets.QWidget(frmUserInfo)

        self.pnlUserInfo = QtWidgets.QWidget(self.UserPanel)
        self.pnlUserInfo.setGeometry(QtCore.QRect(0, 0, 550, 640))
        self.pnlUserInfo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pnlUserInfo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pnlUserInfo.setStyleSheet("background:black;")
        self.pnlUserInfo.setObjectName("pnlUserInfo")
        
        self.lblPic = QtWidgets.QLabel(self.pnlUserInfo)
        self.lblPic.setGeometry(QtCore.QRect(180, 120, 201, 121))
        self.lblPic.setStyleSheet("background:none;\n"
"border-radius:100%;\n"
"border-image:url(avatart.png);")
        self.lblPic.setText("")
        self.lblPic.setObjectName("lblPic")
        
        self.lblTitle = QtWidgets.QLabel(self.pnlUserInfo)
        self.lblTitle.setGeometry(QtCore.QRect(160, 10, 261, 81))
        self.lblTitle.setStyleSheet("color: rgb(85, 255, 255);\n"
"font: 45pt \"MV Boli\";\n"
"background:none;")
        self.lblTitle.setObjectName("lblTitle")
        
        self.lblGameID = QtWidgets.QLabel(self.pnlUserInfo)
        self.lblGameID.setGeometry(QtCore.QRect(90, 290, 100, 31))
        self.lblGameID.setStyleSheet("color:white;\n"
"font: 14pt \"Arial\";\n"
"background:none;")
        self.lblGameID.setObjectName("lblGameID")
        self.lblSetGameID = QtWidgets.QLabel(self.pnlUserInfo)
        self.lblSetGameID.setGeometry(QtCore.QRect(260, 290, 110, 31))
        self.lblSetGameID.setStyleSheet("color:white;\n"
"font: 14pt \"Arial\";\n"
"background:none;")
        self.lblSetGameID.setObjectName("lblSetGameID")
        self.lblName = QtWidgets.QLabel(self.pnlUserInfo)
        self.lblName.setGeometry(QtCore.QRect(90, 340, 100, 31))
        self.lblName.setStyleSheet("color:white;\n"
"font: 14pt \"Arial\";\n"
"background:none;")
        self.lblName.setObjectName("lblName")
        self.lblLast = QtWidgets.QLabel(self.pnlUserInfo)
        self.lblLast.setGeometry(QtCore.QRect(90, 390, 100, 31))
        self.lblLast.setStyleSheet("color:white;\n"
"font: 14pt \"Arial\";\n"
"background:none;")
        self.lblLast.setObjectName("lblLast")
        self.lblPass = QtWidgets.QLabel(self.pnlUserInfo)
        self.lblPass.setGeometry(QtCore.QRect(90, 440, 100, 31))
        self.lblPass.setStyleSheet("background:none;\n"
"color:white;\n"
"font: 14pt \"Arial\";")
        self.lblPass.setObjectName("lblPass")
        self.lblEmail = QtWidgets.QLabel(self.pnlUserInfo)
        self.lblEmail.setGeometry(QtCore.QRect(90, 490, 100, 31))
        self.lblEmail.setStyleSheet("color:white;\n"
"font: 14pt \"Arial\";\n"
"background:none;")
        self.lblEmail.setObjectName("lblEmail")
        self.lblSetName = QtWidgets.QLabel(self.pnlUserInfo)
        self.lblSetName.setGeometry(QtCore.QRect(260, 340, 120, 31))
        self.lblSetName.setStyleSheet("color:white;\n"
"font: 14pt \"Arial\";\n"
"background:none;")
        self.lblSetName.setObjectName("lblSetName")
        self.lblSetLast = QtWidgets.QLabel(self.pnlUserInfo)
        self.lblSetLast.setGeometry(QtCore.QRect(260, 390, 110, 31))
        self.lblSetLast.setStyleSheet("color:white;\n"
"font: 14pt \"Arial\";\n"
"background:none;")
        self.lblSetLast.setObjectName("lblSetLast")
        
        self.lblSetPass = QtWidgets.QLabel(self.pnlUserInfo)
        self.lblSetPass.setGeometry(QtCore.QRect(260, 440, 110, 31))
        self.lblSetPass.setStyleSheet("""
                                      color:white;
                                      font: 14pt \"Arial\";
                                      background:none; 
                                      """)
        self.lblSetPass.setInputMethodHints(QtCore.Qt.ImhNone)
        

        self.lblSetEmail = QtWidgets.QLabel(self.pnlUserInfo)
        self.lblSetEmail.setGeometry(QtCore.QRect(260, 490, 201, 31))
        self.lblSetEmail.setStyleSheet("color:white;\n"
"background:none;\n"
"font: 10pt \"Arial\";")

        self.btnShow = QtWidgets.QPushButton(self.pnlUserInfo)
        self.btnShow.setGeometry(QtCore.QRect(410, 440, 51, 31))
        self.btnShow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnShow.setStyleSheet("background:none;\n"
"font: 15pt \"MV Boli\";\n"
"border:none;\n"
"border-image: url(HidePass.png);")
        self.btnShow.setText("")
        self.btnShow.setDefault(True)
        self.btnShow.clicked.connect(self.showPass)

        self.line = QtWidgets.QFrame(self.pnlUserInfo)
        self.line.setGeometry(QtCore.QRect(40, 290, 20, 270))
        self.line.setStyleSheet("background:None;")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_2.setGeometry(QtCore.QRect(40, 280, 21, 16))
        self.line_2.setStyleSheet("background:none;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_5 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_5.setGeometry(QtCore.QRect(70, 320, 411, 20))
        self.line_5.setStyleSheet("background:none;")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.line_6 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_6.setGeometry(QtCore.QRect(60, 320, 20, 21))
        self.line_6.setStyleSheet("background:None;")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.line_7 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_7.setGeometry(QtCore.QRect(470, 320, 20, 21))
        self.line_7.setStyleSheet("background:None;")
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.line_8 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_8.setGeometry(QtCore.QRect(60, 370, 20, 21))
        self.line_8.setStyleSheet("background:None;")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")

        self.line_9 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_9.setGeometry(QtCore.QRect(470, 370, 20, 21))
        self.line_9.setStyleSheet("background:None;")
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        self.line_10 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_10.setGeometry(QtCore.QRect(70, 370, 411, 20))
        self.line_10.setStyleSheet("background:none;")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")

        self.line_11 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_11.setGeometry(QtCore.QRect(470, 420, 20, 21))
        self.line_11.setStyleSheet("background:None;")
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_12.setGeometry(QtCore.QRect(70, 420, 411, 20))
        self.line_12.setStyleSheet("background:none;")
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_13.setGeometry(QtCore.QRect(60, 420, 20, 21))
        self.line_13.setStyleSheet("background:None;")
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_14.setGeometry(QtCore.QRect(470, 470, 20, 21))
        self.line_14.setStyleSheet("background:None;")
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_15.setGeometry(QtCore.QRect(60, 470, 20, 21))
        self.line_15.setStyleSheet("background:None;")
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_16.setGeometry(QtCore.QRect(70, 470, 411, 20))
        self.line_16.setStyleSheet("background:none;")
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_17.setGeometry(QtCore.QRect(470, 520, 20, 21))
        self.line_17.setStyleSheet("background:None;")
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_18.setGeometry(QtCore.QRect(70, 520, 411, 20))
        self.line_18.setStyleSheet("background:none;")
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_19.setGeometry(QtCore.QRect(60, 520, 20, 21))
        self.line_19.setStyleSheet("background:None;")
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_20.setGeometry(QtCore.QRect(40, 550, 21, 16))
        self.line_20.setStyleSheet("background:none;")
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_21.setGeometry(QtCore.QRect(490, 280, 21, 16))
        self.line_21.setStyleSheet("background:none;")
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_22.setGeometry(QtCore.QRect(490, 550, 21, 16))
        self.line_22.setStyleSheet("background:none;")
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.line_23 = QtWidgets.QFrame(self.pnlUserInfo)
        self.line_23.setGeometry(QtCore.QRect(490, 290, 20, 270))
        self.line_23.setStyleSheet("background:None;")
        self.line_23.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        
        self.btnDone = QtWidgets.QPushButton(self.pnlUserInfo)
        self.btnDone.setGeometry(QtCore.QRect(120, 560, 311, 41))
        self.btnDone.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDone.setStyleSheet("    border: none;\n"
"    outline: none;\n"
"    height: 40px;\n"
"    color: #fff;\n"
"    font-size: 18px;\n"
"    border-radius: 20px;\n"
"    background: #fb2525;\n"
"")
        
        # self.lblTitle.setText("User Info")
        # self.lblGameID.setText("Game ID: ")
        # self.lblSetGameID.setText("#20313")
        # self.lblName.setText("Name:")
        # self.lblLast.setText("Last Name:")
        # self.lblPass.setText("Password:")
        # self.lblEmail.setText("Email:")
        # self.lblSetName.setText("Baseer")
        # self.lblSetLast.setText("Ahmadzai")
        # self.lblSetPass.setText("#*******")
        # self.lblSetEmail.setText("SeeratPeroz82@gmail.com")
        # self.btnDone.setText("DONE")
        
        # to take the ID of User
        ExID = open('temID.txt').read()
 
        x = dConnectUser.dbConnect().userINFO(ExID)
        # print("User INFO: ",x)
        
        for InfoResult in x:
            pass
        print(InfoResult)
        ID = str(InfoResult[0])
        Nam = str(InfoResult[1])
        Last = str(InfoResult[2])
        self.PASsS = str(InfoResult[4])
        EMAIL = str(InfoResult[5])
        self.lblTitle.setText("User Info")
        self.lblGameID.setText("Game ID: ")
        self.lblSetGameID.setText(ID)
        self.lblName.setText("Name:")
        self.lblLast.setText("Last Name:")
        self.lblPass.setText("Password:")
        self.lblEmail.setText("Email:")
        self.lblSetName.setText(Nam)
        self.lblSetLast.setText(Last)
        self.lblSetPass.setText("#*******")
        self.lblSetEmail.setText(EMAIL)
        self.btnDone.setText("DONE")
        
        
        self.btnDone.clicked.connect(self.Exit)
        # self.btnDone.clicked.connect(QApplication.instance().quit)

        
        frmUserInfo.setCentralWidget(self.UserPanel)

        QtCore.QMetaObject.connectSlotsByName(frmUserInfo)






    # function to show password
    def showPass (self):
        self.btnShow.setStyleSheet("background:none;\n"
"font: 15pt \"MV Boli\";\n"
"border:none;\n"
"border-image: url(showPass.png);")
        self.lblSetPass.setText(self.PASsS)

        
    def Exit (self):
        try:
            frmUserInfo.hide()
            # sys.exit()
        except Exception as ex:
            print(ex)



frmUserInfo = QtWidgets.QMainWindow()
ui = Ui_frmUserInfo()
ui.setupUi(frmUserInfo)
frmUserInfo.show()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     frmUserInfo = QtWidgets.QMainWindow()
#     ui = Ui_frmUserInfo()
#     ui.setupUi(frmUserInfo)
#     frmUserInfo.show()
#     sys.exit(app.exec_())