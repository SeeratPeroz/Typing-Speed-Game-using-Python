from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import dbConnection as dConnect

# import Typing
import dbConnection as dConnectUser

class Ui_frmFeedback(object):
    def __init__(self):
        self.msgFrom = ''
        self.ExID = open('temID.txt').read()

    
    def setupUi(self, frmFeedback):
  
        # print(Typing.Ui_frmFeedback().btnReset_Clicked().dataID)
    
        frmFeedback.resize(810, 510)
        frmFeedback.setWindowIcon(QIcon('Feedback.png'))
        frmFeedback.setWindowTitle("Feedback")
        
        self.centralwidget = QtWidgets.QWidget(frmFeedback)
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 811, 510))
        self.widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget.setStyleSheet("background-image: url(resizeFeedback.jpg);")
        self.widget.setObjectName("widget")
        
        self.btnSubmit = QtWidgets.QPushButton(self.widget)
        self.btnSubmit.setGeometry(QtCore.QRect(30, 90, 111, 51))
        self.btnSubmit.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnSubmit.setStyleSheet("background:none;\n"
"background-color: green ;\n"
"height: 50px;\n"
"width: 90%;\n"
"margin-bottom: 2%; \n"
"font-size: 24px;\n"
"border-radius: 22%;\n"
"color: white;")
        self.btnSubmit.clicked.connect(self.submited)

        
        self.lblTitle = QtWidgets.QLabel(self.widget)
        self.lblTitle.setGeometry(QtCore.QRect(300, 30, 245, 45))
        self.lblTitle.setStyleSheet("color: rgb(85, 255, 255);\n"
"font: 45pt \"MV Boli\";\n"
"background:none;")
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        
        self.txtMsg = QtWidgets.QTextEdit(self.widget)
        self.txtMsg.setGeometry(QtCore.QRect(30, 170, 731, 301))
        self.txtMsg.setStyleSheet("background:None;\n"
"font: 12pt \"Arial\";")
        self.txtMsg.setObjectName("txtMsg")
        self.txtFrom = QtWidgets.QLineEdit(self.widget)
        self.txtFrom.setGeometry(QtCore.QRect(160, 100, 601, 41))
        self.txtFrom.setStyleSheet("background:none;\n"
"font: 14pt \"Arial\";")
        self.txtFrom.setObjectName("txtFrom")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(20, 150, 751, 16))
        self.line.setStyleSheet("background:none;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(10, 150, 20, 16))
        self.line_2.setStyleSheet("background:none;")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(760, 150, 20, 16))
        self.line_3.setStyleSheet("background:none;")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setGeometry(QtCore.QRect(140, 90, 20, 61))
        self.line_4.setStyleSheet("background:none;")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setGeometry(QtCore.QRect(140, 140, 21, 20))
        self.line_5.setStyleSheet("background:none;")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.widget)
        self.line_6.setGeometry(QtCore.QRect(140, 80, 21, 20))
        self.line_6.setStyleSheet("background:none;")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.newBox = QtWidgets.QMessageBox(self.widget)

        frmFeedback.setCentralWidget(self.centralwidget)

        self.btnSubmit.setText("Submit")
        self.lblTitle.setText("Feedback")
        

        # Taking the id of uer from external source
        x = dConnectUser.dbConnect().userINFO(self.ExID)
        # print("Feed INFO: ",x)
        
        for InfoResult in x:
            pass
        
        self.msgFrom = str(InfoResult[5])
        self.txtFrom.setAlignment(QtCore.Qt.AlignCenter)
        self.txtFrom.setText(self.msgFrom)
        QtCore.QMetaObject.connectSlotsByName(frmFeedback)



    def submited (self):
        self.ExID = open('temID.txt').read()
        Massage = self.txtMsg.toPlainText()
        # print(Massage)
        InSt = dConnectUser.dbConnect().insertFeedback(self.ExID,self.msgFrom, Massage )
        if InSt:
            self.newBox.setText("<h1> Thank you for your feedback </h1>")
            self.newBox.setWindowTitle("Submitted")
            self.newBox.setWindowIcon(QIcon("Information.png"))
            self.newBox.setStyleSheet("color:black; font: 9pt Arial ITC; background:none;")
            self.newBox.show()           
            self.txtMsg.clear()
            frmFeedback.hide()
        else: 
            print("Sorry. Try again.")


frmFeedback = QtWidgets.QMainWindow()
ui = Ui_frmFeedback()
ui.setupUi(frmFeedback)
frmFeedback.show()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     frmFeedback = QtWidgets.QMainWindow()
#     ui = Ui_frmFeedback()
#     ui.setupUi(frmFeedback)
#     frmFeedback.show()
#     sys.exit(app.exec_())
