from PyQt5 import QtCore, QtGui, QtWidgets


def pnlREG(self):
        self.pnlLogin = QtWidgets.QWidget(self.centralwidget)
        self.pnlLogin.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.pnlLogin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pnlLogin.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pnlLogin.setStyleSheet("background-image:url(R5.jpg);")
        self.pnlLogin.setObjectName("pnlLogin")
        
        
        self.lineEdit = QtWidgets.QLineEdit(self.pnlLogin)
        self.lineEdit.setGeometry(QtCore.QRect(60, 290, 351, 51))
        self.lineEdit.setStyleSheet("    border:  none;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"    font-size: 24px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.pnlLogin)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 360, 351, 51))
        self.lineEdit_2.setStyleSheet("    border:  none;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"    font-size: 24px;")
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.pnlLogin)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 420, 351, 51))
        self.lineEdit_3.setStyleSheet("    border:  none;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"    font-size: 24px;")
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.pnlLogin)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 220, 351, 51))
        self.lineEdit_4.setStyleSheet("    border:  none;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"    font-size: 24px;")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        
        
        self.pushButton = QtWidgets.QPushButton(self.pnlLogin)
        self.pushButton.setGeometry(QtCore.QRect(70, 500, 141, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet("background:none;\n"
" font-size: 24px;\n"
" color: white;\n"
"  background-color: green ;\n"
"border-radius:10%;")
        self.pushButton.setObjectName("pushButton")
        
        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.pnlLogin)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 500, 141, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_2.setStyleSheet("background:none;\n"
" font-size: 24px;\n"
" color: white;\n"
"  background-color: green ;\n"
"border-radius:10%;")
        self.pushButton_2.setObjectName("pushButton_2")
        
        
        
        self.label = QtWidgets.QLabel(self.pnlLogin)
        self.label.setGeometry(QtCore.QRect(140, 50, 201, 121))
        self.label.setStyleSheet("\n"
"border-radius:100%;\n"
"border-image:url(avatart.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        
        
        
        self.line_2 = QtWidgets.QFrame(self.pnlLogin)
        self.line_2.setGeometry(QtCore.QRect(30, 210, 16, 331))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        
        
        
        self.line_3 = QtWidgets.QFrame(self.pnlLogin)
        self.line_3.setGeometry(QtCore.QRect(420, 210, 16, 331))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        
        
        
        
        self.label_2 = QtWidgets.QLabel(self.pnlLogin)
        self.label_2.setGeometry(QtCore.QRect(390, 30, 261, 81))
        self.label_2.setStyleSheet("color: rgb(85, 255, 255);\n"
"font: 52pt \"Rage Italic\";")
        self.label_2.setObjectName("label_2")
        
        
        
        
        
        self.checkBox = QtWidgets.QCheckBox(self.pnlLogin)
        self.checkBox.setGeometry(QtCore.QRect(350, 370, 51, 41))
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.checkBox.setObjectName("checkBox")
      
        
        
        
        self.pushButton_3 = QtWidgets.QPushButton(self.pnlLogin)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 20, 61, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background:none;\n"
"font: 15pt \"MV Boli\";\n"
"border:none;\n"
"border-image: url(Back1.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.checkBox, self.lineEdit_4)
        mainWindow.setTabOrder(self.lineEdit_4, self.lineEdit)
        mainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        mainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        mainWindow.setTabOrder(self.lineEdit_3, self.pushButton)
        mainWindow.setTabOrder(self.pushButton, self.pushButton_2)


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("mainWindow", "Last Name"))
        self.lineEdit_2.setPlaceholderText(_translate("mainWindow", "Password"))
        self.lineEdit_3.setPlaceholderText(_translate("mainWindow", "Email"))
        self.lineEdit_4.setPlaceholderText(_translate("mainWindow", "Name"))
        self.pushButton.setText(_translate("mainWindow", "Sign Up"))
        self.pushButton_2.setText(_translate("mainWindow", "Cancel"))
        self.label_2.setText(_translate("mainWindow", "Sign Up"))
        self.checkBox.setText(_translate("mainWindow", "Show"))
        self.pushButton_3.setToolTip(_translate("mainWindow", "<html><head/><body><p>Click to Change the Sentence.</p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
