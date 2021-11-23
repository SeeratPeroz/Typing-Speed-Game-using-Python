# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Drivw E\BCS\Semester 3\Python\Project\Part 3\All Part 3\Records.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
from tkinter.ttk import *
import dbConnection as dConnectRecord

class Ui_MainWindow(object):


        
    def setupUi(self, MainWindow):        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.Rpanel = QtWidgets.QWidget(MainWindow)
        self.Rpanel.setObjectName("Rpanel")
        self.pnlMainMenu = QtWidgets.QWidget(self.Rpanel)
        self.pnlMainMenu.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.pnlMainMenu.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pnlMainMenu.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pnlMainMenu.setStyleSheet("background-image:url(ResizeRecord.jpg);")
        self.pnlMainMenu.setObjectName("pnlMainMenu")
        self.btnMenuBack = QtWidgets.QPushButton(self.pnlMainMenu)
        self.btnMenuBack.setGeometry(QtCore.QRect(20, 30, 61, 61))
        self.btnMenuBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMenuBack.setStyleSheet("background:none;\n"
"font: 15pt \"MV Boli\";\n"
"border:none;\n"
"border-image: url(Back1.png);")
        self.btnMenuBack.setText("")
        self.btnMenuBack.setDefault(True)
        self.btnMenuBack.setObjectName("btnMenuBack")
        self.lblMenuTitle = QtWidgets.QLabel(self.pnlMainMenu)
        self.lblMenuTitle.setGeometry(QtCore.QRect(320, 20, 361, 81))
        self.lblMenuTitle.setStyleSheet("background:none;\n"
"color: rgb(0, 255, 0);\n"
"font: 48pt \"Algerian\";")
        self.lblMenuTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMenuTitle.setObjectName("lblMenuTitle")
        self.lblMenuRight = QtWidgets.QLabel(self.pnlMainMenu)
        self.lblMenuRight.setGeometry(QtCore.QRect(370, 540, 301, 31))
        self.lblMenuRight.setStyleSheet("background:none;\n"
"color: white;\n"
"font: 75 10pt \"Arial\";")
        self.lblMenuRight.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMenuRight.setObjectName("lblMenuRight")
        self.btnHistory = QtWidgets.QPushButton(self.pnlMainMenu)
        self.btnHistory.setGeometry(QtCore.QRect(140, 190, 761, 91))
        self.btnHistory.setStyleSheet("    border: none;\n"
"    outline: none;\n"
"\n"
"    color: black;\n"
"    font-size: 54px;\n"
"    border-radius: 30px;\n"
"    background: rgb(0, 255, 0);")
        self.btnHistory.setObjectName("btnHistory")
        self.btnFeedback = QtWidgets.QPushButton(self.pnlMainMenu)
        self.btnFeedback.setGeometry(QtCore.QRect(140, 350, 761, 91))
        self.btnFeedback.setStyleSheet("    border: none;\n"
"    outline: none;\n"
"\n"
"    color: black;\n"
"    font-size: 54px;\n"
"    border-radius: 30px;\n"
"    background: rgb(0, 255, 0);")
        self.btnFeedback.setObjectName("btnFeedback")
        self.line = QtWidgets.QFrame(self.pnlMainMenu)
        self.line.setGeometry(QtCore.QRect(120, 310, 791, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_2.setGeometry(QtCore.QRect(110, 290, 3, 61))
        self.line_2.setStyleSheet("background:none;")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_5 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_5.setGeometry(QtCore.QRect(910, 290, 3, 61))
        self.line_5.setStyleSheet("background:none;")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        
        self.btnHistory.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMenuBack.clicked.connect(self.Exit)
        self.btnHistory.clicked.connect(self.feed)
        self.btnFeedback.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFeedback.clicked.connect(self.feedmsg)
        
        MainWindow.setCentralWidget(self.Rpanel)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnMenuBack.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click to Change the Sentence.</p></body></html>"))
        self.lblMenuTitle.setText(_translate("MainWindow", "Records"))
        self.lblMenuRight.setText(_translate("MainWindow", "All Rights Reversed @ Siratperoz82@gmail.com"))
        self.btnHistory.setText(_translate("MainWindow", "Typing History"))
        self.btnFeedback.setText(_translate("MainWindow", "Feedback History"))




    def Exit (self):
        try:
            MainWindow.hide()
            # sys.exit()
        except Exception as ex:
            print(ex)
            
            
    def feed (self):
        
        ExID = open('temID.txt').read()
        x = dConnectRecord.dbConnect().recordINFO(ExID)
                        

            
        root = Tk()
        root.geometry("800x340")
        root.title("Typing Histroy")
        
        cols = ("Record-ID", "Full-Name", "UserName", "Level", "Time", "Word-PM", "Accuracy")
        tree = Treeview(root, columns = cols, show='headings')
        tree.pack()
        for col in cols:
            tree.heading(col, text= col)
        tree.column("Record-ID", width=80)
        tree.column("Full-Name" , width= 150)
        tree.column("UserName" , width= 150)
        tree.column("Level", width= 100)
        tree.column("Time", width= 100)
        tree.column("Word-PM", width= 100)
        tree.column("Accuracy", width= 100)
        for i in x:
            tree.insert("","end", values= (i[0],i[1],i[2],i[3],str(i[4])+" Sec",str(i[5])+" Wpm",str(i[6])+"%"))
     
        root.mainloop()


    def feedmsg (self):
        ExID = open('temID.txt').read()
        x = dConnectRecord.dbConnect().feedInfo(ExID)        
        
        
        root = Tk()
        root.geometry("850x340")
        root.title("Feedback History")
        
        cols = ("GameID","UserName", "Email","Message")
        tree = Treeview(root, columns = cols, show='headings')
        tree.pack()
        for col in cols:
            tree.heading(col, text= col)
        tree.column("GameID", width=80)
        tree.column("UserName" , width= 150)
        tree.column("Email" , width= 200)
        tree.column("Message" , width= 400)

 
        
        for i in x:
            tree.insert("","end", values= (i[0],i[1],i[2] ,i[3]))

        root.mainloop()   


MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
