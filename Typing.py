from PyQt5 import QtCore, QtGui, QtWidgets
import time as tm
from PyQt5.QtGui import *
from pathlib import Path
import sys
import time
import threading
import random
from PyQt5.QtWidgets import QMainWindow, QLabel, QCheckBox, QWidget
from PyQt5.QtCore import QSize  
import timeit
import dbConnection as dConnect




class Ui_MainWindow(object):

    def __init__(self):
        MainWindow.resize(1000, 600)  
        self.ch = ''     
        # Declare Importan Widgets     
        self.panel = QtWidgets.QWidget(MainWindow)
        self.pnlType = QtWidgets.QWidget(self.panel)
        self.pnlWelcome = QtWidgets.QWidget(self.panel)
        self.pnlLogin = QtWidgets.QWidget(self.panel)
        self.pnlRegister = QtWidgets.QWidget(self.panel)
        self.pnlWmsg = QtWidgets.QWidget(self.panel)
        self.pnlMainMenu = QtWidgets.QWidget(self.panel)

        
        
        # Declaring Element for Login Panel
        self.txtLuser = QtWidgets.QLineEdit(self.pnlLogin)
        self.txtLpass = QtWidgets.QLineEdit(self.pnlLogin)
        self.lblTitle = QtWidgets.QLabel(self.pnlLogin)
        self.lblLogin = QtWidgets.QLabel(self.pnlLogin)
        self.lblCreate = QtWidgets.QLabel(self.pnlLogin)
        self.lblRights = QtWidgets.QLabel(self.pnlLogin)
        self.btnLogin = QtWidgets.QPushButton(self.pnlLogin)
        self.btnSignUp = QtWidgets.QPushButton(self.pnlLogin)
        self.btnGuest = QtWidgets.QPushButton(self.pnlLogin)
        self.btnHelp = QtWidgets.QPushButton(self.pnlLogin)
        self.line = QtWidgets.QFrame(self.pnlLogin)
        self.line1 = QtWidgets.QFrame(self.pnlLogin)
        self.line2 = QtWidgets.QFrame(self.pnlLogin)
        self.line3 = QtWidgets.QFrame(self.pnlLogin)
        self.line4 = QtWidgets.QFrame(self.pnlLogin)
        self.line5 = QtWidgets.QFrame(self.pnlLogin)
        self.line6 = QtWidgets.QFrame(self.pnlLogin)
        self.line7 = QtWidgets.QFrame(self.pnlLogin)
        self.line8 = QtWidgets.QFrame(self.pnlLogin)
        self.line10 = QtWidgets.QFrame(self.pnlLogin)
        self.logmsg =QtWidgets.QMessageBox(self.pnlRegister)

        
        # Declaring Element for Register Panel
        self.txtLastNameP = QtWidgets.QLineEdit(self.pnlRegister)        
        self.txtPassP = QtWidgets.QLineEdit(self.pnlRegister)
        self.txtEmail = QtWidgets.QLineEdit(self.pnlRegister)        
        self.txtName = QtWidgets.QLineEdit(self.pnlRegister)        
        self.txtUName = QtWidgets.QLineEdit(self.pnlRegister)        
        self.btnSignUpP = QtWidgets.QPushButton(self.pnlRegister)        
        self.btnCanelR = QtWidgets.QPushButton(self.pnlRegister)        
        self.label = QtWidgets.QLabel(self.pnlRegister)        
        self.line_2 = QtWidgets.QFrame(self.pnlRegister)
        self.line_3 = QtWidgets.QFrame(self.pnlRegister)        
        self.lblSignUpP = QtWidgets.QLabel(self.pnlRegister)        
        self.btnBackP = QtWidgets.QPushButton(self.pnlRegister)
        self.regis = QtWidgets.QMessageBox(self.pnlRegister)

        
        
        # Delaring Imortant Elements in Type Panel
        self.lblHeading = QtWidgets.QLabel(self.pnlType)
        self.lblType = QtWidgets.QLabel(self.pnlType)
        self.txtType = QtWidgets.QLineEdit(self.pnlType)
        self.lblResult = QtWidgets.QLabel(self.pnlType)
        self.btnReset = QtWidgets.QPushButton(self.pnlType)
        self.msg = QtWidgets.QMessageBox(self.pnlType)
        self.btnsenResatr = QtWidgets.QPushButton(self.pnlType)
        self.btnBack = QtWidgets.QPushButton(self.pnlType)
        self.boxError = QtWidgets.QMessageBox(self.pnlType)
        self.cnt = 0
        self.getRand = ''
        self.totleT = 0.0
        self.startTime = 0.0
        self.stopTime = 0.0
        self.accuracy = 0.0
        self.wpm = 0
        self.keyCnt = 0
        
        
        # pnlWmsg label to show user name
        self.lblWlcUser = QtWidgets.QLabel(self.pnlWmsg)
        
        # import counters
        self.imp = 0
        self.fdb = 0
        self.Hdb = 0
        self.Rdb = 0
        self.dataID = 27

        

        
     #   stdColor = rgb(255, 222, 53);


    def Run_Game(self, MainWindow):

        # Main Window Settings
        MainWindow.resize(1000,600)
        # Setting the Size of Main Window
        MainWindow.setWindowTitle(("Typing Speed"))
        # Setting the Icon for Main Window
        MainWindow.setWindowIcon(QIcon('On Screen Keyboard.png'))
        
        
        self.pnlType.hide()
        self.pnlLogin.hide()
        self.pnlRegister.hide()
        self.pnlWmsg.hide()
        self.pnlMainMenu.hide()
        
#       To call the Welcome Screen Widget  by a Thread
        wlc = threading.Timer(0.0,self.welcScreen)
        wlc.start()
        

        # Setting the Size of Main Widget
        self.pnlType.setGeometry(0,0,1000,600)
        # Appling Background to Main Widget
        self.pnlType.setStyleSheet("background-image: url(background4.jpg);  background-position: center;")
        
        
        # Heading Label Settings
        self.lblHeading.setGeometry(260, 40, 531, 81)
        self.lblHeading.setText("T y p i n g   S p e e d")
        self.lblHeading.setStyleSheet("background-color: red; color:white;")
        self.lblHeading.setStyleSheet("""background:none; 
                                      color:rgb(255, 222, 53);
                                      font: 40pt Kristen ITC;
                                      """)
        self.lblHeading.setAlignment(QtCore.Qt.AlignCenter)
        
        
        # Sentence Label Settings
        self.lblType.setGeometry(90, 160, 841, 111)
        self.lblType.setStyleSheet("""
                                   border-image: url(background4.jpg);
                                   background:none;
                                   color: rgb(255, 255, 255);
                                   font: 20pt MS Sans Serif;
                                   """)
        self.lblType.setWordWarp= True;
        self.lblType.setAlignment(QtCore.Qt.AlignCenter)
        
        
        
        
        # Setting The Line Edit for Typing
        self.txtType.setGeometry(30, 300, 941, 71)
        self.txtType.setStyleSheet("""
                                  background:none;
                                  background-color: black;
                                  border: 3px solid rgb(255, 222, 53);
                                  font: 20pt Myanmar Text;
                                  color: white; 
                                  """)
        self.txtType.setAlignment(QtCore.Qt.AlignCenter)
        self.txtType.setText("")
        self.txtType.textChanged.connect(self.timeStart)
        self.txtType.returnPressed.connect(self.enterKey)
        self.txtType.setToolTip("<html><head/><body><p><span style=\" font-size:9pt;\">Click here to start typing, when typing finished press </span><span style=\" font-size:9pt; font-weight:600;\">Enter key</span><span style=\" font-size:9pt;\"> to show the result.</span></p></body></html>")
        
#        self.getSentence()



        # Label to display the Results
        self.lblResult.setGeometry(110, 410, 809, 51)
        self.lblResult.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResult.setStyleSheet("""
                                     color: rgb(0, 255, 0);
                                     font: 18pt Arial;
                                     background: none;
                                     background-image: url(background4.jpg);
                                     """)     
        self.lblResult.hide()
        
        
        
        # Button to reset the Text field and timer.
        self.btnReset.setGeometry(410, 460, 211, 141)
        self.btnReset.setDefault(True)
        self.btnReset.setStyleSheet("""
                                   background:none;
                                   font: 15pt MV Boli;
                                   border:none;
                                   border-image: url(icon.png);
                           """)
        self.btnReset.hide()
        self.btnReset.setText("Restart")
        self.btnReset.clicked.connect(self.btnReset_Clicked)



        # Button to get different sentence
        self.btnsenResatr.setGeometry(920, 30, 61, 61)
        self.btnsenResatr.setText("")
        self.btnsenResatr.setDefault(True)
        self.btnsenResatr.setStyleSheet("""
                           background:none;
                           font: 15pt MV Boli;
                           border:none;
                           border-image: url(change3.webp);
                           """)
        self.btnsenResatr.setToolTip("<html><head> <style> *{background:none; background-color: black; color:white; font-size:12px; border:none;} </style> </head><body><p>Click to Change the Sentence.<br></p></body></html>")
        self.btnsenResatr.clicked.connect(self.sent)
        
        
        
        
        # Button to go to previous panel
        self.btnBack.setGeometry(20, 30, 61, 61)
        self.btnBack.setText("")
        self.btnBack.setDefault(True)
        self.btnBack.setStyleSheet("""
                                   background:none;
                                   font: 15pt \"MV Boli\";
                                   border:none;
                                   border-image: url(Back1.png);
                                   """)
        self.btnBack.setToolTip("<html><head> <style> *{background:none; background-color: black; color:white; font-size:12px; border:none;} </style> </head><body><p>Click to go to <b> Previous </b> panel  .<br></p></body></html>")
        self.btnBack.clicked.connect(self.showMainMenu)


#------------------------------    LOGIN PANEL    -------------------------------------- 
                                   
        
        
        # Login Panel Settings
        self.pnlLogin.setGeometry(0, 0, 1000, 600)
        self.pnlLogin.setStyleSheet("background-image: url(resizeLogin.jpg);")
        
        # Show Password
        self.btnShowPA = QtWidgets.QPushButton(self.pnlLogin)
        self.btnShowPA.setGeometry(310, 390, 71, 61)
        self.btnShowPA.setStyleSheet("border-image: url(HidePass.png);background:none;")
        self.btnShowPA.setText("")
        self.btnShowPA.setCheckable(True)
        self.btnShowPA.toggle()
        self.btnShowPA.clicked.connect(self.btnstate)        
        
        self.btnShutdown = QtWidgets.QPushButton(self.pnlLogin)
        self.btnShutdown.setGeometry(20, 30, 61, 61)
        self.btnShutdown.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnShutdown.setStyleSheet("background:none;\n"
"font: 15pt \"MV Boli\";\n"
"border:none;\n"
"border-image: url(Shutdown.png);")
        self.btnShutdown.setText("")
        self.btnShutdown.setDefault(True)
        self.btnShutdown.clicked.connect(self.shutdown)
        # self.btnShutdown.clicked.connect(QtCore.QCoreApplication.instance().quit)
        
        # Title Label Settings
        self.lblTitle.setText("Typing Speed Game")
        self.lblTitle.setGeometry(260, 30, 521, 61)
        self.lblTitle.setStyleSheet("""
                                    background:none;
                                    color: white;
                                    font: 75 36pt Arial;
                                    """)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        

        
       
        
        # Login Label Setting
        self.lblLogin.setText("Login Here")
        self.lblLogin.setGeometry(70, 170, 261, 51)
        self.lblLogin.setStyleSheet("""
                                    background:none;
                                    color: white;
                                    font: 75 36pt Arial;
                                    """)
        self.lblLogin.setAlignment(QtCore.Qt.AlignCenter)
        
        
        # Create Account Label Setting
        self.lblCreate.setText("Create Account")
        self.lblCreate.setGeometry(640, 170, 331, 51)
        self.lblCreate.setStyleSheet("""
                                     background:none;
                                     color: white;
                                     font: 75 36pt Arial;
                                     """)
        self.lblCreate.setAlignment(QtCore.Qt.AlignCenter)
        
        # Line alignments
        self.line.setGeometry(60, 320, 281, 20)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line1.setGeometry(370, 220, 20, 281)
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line2.setGeometry(10, 220, 20, 281)
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line4.setGeometry(60, 410, 281, 20)
        self.line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line5.setGeometry(660, 381, 281, 20)
        self.line5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line5.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line6.setGeometry(660, 370, 281, 20)
        self.line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line6.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line7.setGeometry(650, 370, 20, 31)
        self.line7.setStyleSheet("background:none;")
        self.line7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line7.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line8.setGeometry(930, 370, 20, 31)
        self.line8.setStyleSheet("background:none;")
        self.line8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line8.setFrameShadow(QtWidgets.QFrame.Sunken)
    
        self.line3.setGeometry(600, 270, 20, 221)
        self.line3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line10.setGeometry(960, 270, 20, 221)
        self.line10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line10.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        # LineEdit Settings for User
        self.txtLuser.setGeometry(40, 260, 321, 51)
        self.txtLuser.setPlaceholderText("Username")
        self.txtLuser.setStyleSheet("""
                                   background:none;
                                   background-color: black;
                                   border: 3px solid rgb(85, 255, 255);
                                   font: 20pt \"Myanmar Text\";
                                   color: white;
                                   border-radius: 22%;
                                   text-align: center;
                                   padding-top:10px;
                                    """)
        self.txtLuser.setText("")
        self.txtLuser.setAlignment(QtCore.Qt.AlignCenter)
        
        # LineEdit Settings for User
        self.txtLpass.setGeometry(40, 350, 321, 51)
        self.txtLpass.setPlaceholderText("Password")
        self.txtLpass.setStyleSheet("""
                                   background:none;
                                   background-color: black;
                                   border: 3px solid rgb(85, 255, 255);
                                   font: 20pt \"Myanmar Text\";
                                   color: white;
                                   border-radius: 22%;
                                   text-align: center;
                                   padding-top:10px;
                                   """)
        self.txtLpass.setText("")
        self.txtLpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtLpass.setAlignment(QtCore.Qt.AlignCenter)


        # Login Button Settings
        self.btnLogin.setGeometry(40, 440, 321, 61)
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnLogin.setStyleSheet("""
                                    background:none;
                                    background-color: green ;
                                    margin-bottom: 2%;
                                    font-size: 24px;
                                    border-radius: 22%;
                                    color:white;
                                    """) 
        self.btnLogin.setText("LOGIN")
        self.btnLogin.clicked.connect(self.MsgWLC)

        
        # Button for Sing Up
        self.btnSignUp.setGeometry(630, 290, 331, 61)
        self.btnSignUp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSignUp.setStyleSheet("""
                                     background:none;
                                     background-color: green ;
                                     height: 50px;
                                     width: 90%;
                                     margin-bottom: 2%; 
                                     font-size: 24px;
                                     border-radius: 22%;
                                     color: white;
                                     """)       
        self.btnSignUp.setText("Sign Up")
        self.btnSignUp.clicked.connect(self.Register)
        self.btnSignUp.setDefault(True)        
        
        # Button For Login as Guest
        self.btnGuest.setGeometry(630, 420, 331, 61)                
        self.btnGuest.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGuest.setStyleSheet("""
                                    background:none;
                                    background-color: green ;
                                    margin-bottom: 2%; 
                                    font-size: 24px;
                                    border-radius: 22%;
                                    color: white;
                                    """)
        self.btnGuest.setText("Login as Guest")
        self.btnGuest.clicked.connect(self.msgGuest)
        
        
        # Button for Help
        self.btnHelp.setGeometry(920, 30, 61, 61)
        self.btnHelp.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.btnHelp.setStyleSheet("""
                                   background:none;
                                   font: 15pt \"MV Boli\";
                                   border:none;
                                   border-image: url(Question.png);
                                   """)
        self.btnHelp.setText("")
        self.btnHelp.setDefault(True)
        self.btnHelp.clicked.connect(self.seerat)
        
        #Label for Rights 
        self.lblRights.setText("All Rights Reversed @ Siratperoz82@gmail.com")
        self.lblRights.setGeometry(250, 540, 521, 51)
        self.lblRights.setStyleSheet("""
                                     background:none;
                                     color: white;
                                     font: 75 10pt \"Arial\";
                                     """)
        self.lblRights.setAlignment(QtCore.Qt.AlignCenter)
        
        MainWindow.setCentralWidget(self.panel)





# ---------------------------- Registration -----------------------------------
        self.pnlRegister.setGeometry(0, 0, 1000, 600)
        self.pnlRegister.setStyleSheet("background-image:url(R5.jpg);")
        
        self.txtName.setGeometry(60, 210, 351, 51)
        self.txtName.setStyleSheet("    border:  none;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"    font-size: 24px;")
        self.txtName.setAlignment(QtCore.Qt.AlignCenter)
        
        self.txtLastNameP.setGeometry(60, 270, 351, 41)
        self.txtLastNameP.setStyleSheet("    border:  none;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"    font-size: 24px;")
        self.txtLastNameP.setAlignment(QtCore.Qt.AlignCenter)
        

        self.txtPassP.setGeometry(60, 380, 351, 41)
        self.txtPassP.setStyleSheet("    border:  none;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"    font-size: 24px;")
        self.txtPassP.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.txtPassP.setText("")
        self.txtPassP.setAlignment(QtCore.Qt.AlignCenter)                
        self.txtPassP.setEchoMode(QtWidgets.QLineEdit.Password)            

        
        self.txtUName.setGeometry(60, 330, 351, 41)
        self.txtUName.setStyleSheet("    border:  none;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"    font-size: 24px;")
        self.txtUName.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.txtUName.setAlignment(QtCore.Qt.AlignCenter)     
        

        self.txtEmail.setGeometry(60, 430, 351, 41)
        self.txtEmail.setStyleSheet("    border:  none;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"    font-size: 24px;")
        self.txtEmail.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.txtEmail.setAlignment(QtCore.Qt.AlignCenter)
        
        
        
        self.btnSignUpP.setGeometry(70, 500, 141, 41)
        self.btnSignUpP.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnSignUpP.setStyleSheet("background:none;\n"
" font-size: 24px;\n"
" color: white;\n"
"  background-color: green ;\n"
"border-radius:10%;")
        self.btnSignUpP.clicked.connect(self.UserReg)

        
        
        self.btnCanelR.setGeometry(260, 500, 141, 51)
        self.btnCanelR.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.btnCanelR.setStyleSheet("background:none;\n"
" font-size: 24px;\n"
" color: white;\n"
"  background-color: green ;\n"
"border-radius:10%;")
        self.btnCanelR.clicked.connect(self.Back2Login)
        
        

        self.label.setGeometry(140, 50, 201, 121)
        self.label.setStyleSheet("\n"
"border-radius:100%;\n"
"border-image:url(avatart.png);")
        self.label.setText("")
        
        

        self.line_2.setGeometry(30, 210, 16, 331)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        
        
        
        self.line_3.setGeometry(420, 210, 16, 331)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)        
        
        

        self.lblSignUpP.setGeometry(390, 30, 261, 81)
        self.lblSignUpP.setStyleSheet("color: rgb(85, 255, 255);\n"
"font: 52pt \"Rage Italic\";")        
        
        
        
        
        self.chkShowPA = QtWidgets.QPushButton(self.pnlRegister)
        self.chkShowPA.setGeometry(360, 370, 61, 61)
        self.chkShowPA.setStyleSheet("border-image: url(HidePass.png);background:none;")
        self.chkShowPA.setText("")
        self.chkShowPA.setCheckable(True)    
        self.chkShowPA.toggle()
        self.chkShowPA.clicked.connect(self.btnstate2)
        
        
        self.btnBackP.setGeometry(20, 20, 61, 51)
        self.btnBackP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBackP.setStyleSheet("background:none;\n"
"font: 15pt \"MV Boli\";\n"
"border:none;\n"
"border-image: url(Back1.png);")
        self.btnBackP.setText("")
        self.btnBackP.setDefault(True)
        self.btnBackP.clicked.connect(self.Back2Login)


        self.txtLastNameP.setPlaceholderText("Last Name")
        self.txtPassP.setPlaceholderText("Password")
        self.txtEmail.setPlaceholderText("Email")
        self.txtName.setPlaceholderText("Name")
        self.txtUName.setPlaceholderText("UserName")
        self.btnSignUpP.setText("Sign Up")
        self.btnCanelR.setText("Cancel")
        self.lblSignUpP.setText("Sign Up")

                 # Register Panel Tab order   
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.chkShowPA, self.txtName)
        MainWindow.setTabOrder(self.txtName, self.txtLastNameP)
        MainWindow.setTabOrder(self.txtLastNameP, self.txtUName)
        MainWindow.setTabOrder(self.txtUName, self.txtPassP)
        MainWindow.setTabOrder(self.txtPassP, self.txtEmail)
        MainWindow.setTabOrder(self.txtEmail, self.btnSignUpP)
        MainWindow.setTabOrder(self.btnSignUpP, self.btnCanelR)
        

        
# --------------------------------- Main Menu ------------------------------------
        
        # Declaring Important elements for Main Menu
        self.btnMenuBack = QtWidgets.QPushButton(self.pnlMainMenu)
        self.lblMenuTitle = QtWidgets.QLabel(self.pnlMainMenu)
        self.btnMenuStart = QtWidgets.QPushButton(self.pnlMainMenu)
        self.lblDiffcult = QtWidgets.QLabel(self.pnlMainMenu)
        self.lblGameType = QtWidgets.QLabel(self.pnlMainMenu)
        self.combDiff = QtWidgets.QComboBox(self.pnlMainMenu)
        self.line_3 = QtWidgets.QFrame(self.pnlMainMenu)
        self.lblMain = QtWidgets.QLabel(self.pnlMainMenu)
        self.combGType = QtWidgets.QComboBox(self.pnlMainMenu)
        self.btnMenuUser = QtWidgets.QPushButton(self.pnlMainMenu)
        self.btnRecord = QtWidgets.QPushButton(self.pnlMainMenu)
        self.lblHistory = QtWidgets.QLabel(self.pnlMainMenu)
        self.btnMenuHelp = QtWidgets.QPushButton(self.pnlMainMenu)
        self.lblMenuRight = QtWidgets.QLabel(self.pnlMainMenu)
        self.btnFeedback = QtWidgets.QPushButton(self.pnlMainMenu)


        self.line_9 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_11 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_13 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_14 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_27 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_28 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_31 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_32 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_33 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_34 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_35 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_38 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_39 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_40 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_41 = QtWidgets.QFrame(self.pnlMainMenu)        
        self.line_37 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_10 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_8 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_7 = QtWidgets.QFrame(self.pnlMainMenu)        
        self.line_6 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_5 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_4 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_2 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line = QtWidgets.QFrame(self.pnlMainMenu)
        
        self.pnlMainMenu.setGeometry(0, 0, 1000, 600)
        self.pnlMainMenu.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pnlMainMenu.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pnlMainMenu.setStyleSheet("background:none;background-image:url(Main.jpg);")
        self.pnlMainMenu.setObjectName("pnlMainMenu")
        
        self.btnMenuBack.setGeometry(20, 30, 61, 61)
        self.btnMenuBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMenuBack.setStyleSheet("background:none;\n"
"font: 15pt \"MV Boli\";\n"
"border:none;\n"
"border-image: url(rlogout.png);")
        self.btnMenuBack.setText("")
        self.btnMenuBack.setDefault(True)
        self.btnMenuBack.clicked.connect(self.Back2Login)

        
        self.lblMenuTitle.setGeometry(320, 30, 361, 81)
        self.lblMenuTitle.setStyleSheet("background:none;\n"
"color: rgb(0, 255, 0);\n"
"font: 48pt \"Algerian\";")
        self.lblMenuTitle.setAlignment(QtCore.Qt.AlignCenter)        
        
        self.btnMenuStart.setGeometry(60, 430, 381, 61)
        self.btnMenuStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMenuStart.setStyleSheet("background:none; background-color: green ; margin-bottom: 2%;  font-size: 24px; border-radius: 15%; color: white;")
        self.btnMenuStart.setObjectName("btnMenuStart")
        self.btnMenuStart.clicked.connect(self.showTyping)
        
        
        self.lblDiffcult.setGeometry(80, 250, 121, 41)
        self.lblDiffcult.setStyleSheet("background:none;\n"
"color: white;\n"
"font: 75 20pt \"Arial\";\n"
"")
        self.lblGameType.setGeometry(70, 340, 151, 41)
        self.lblGameType.setStyleSheet("background:none;\n"
"color: white;\n"
"font: 75 20pt \"Arial\";\n"
"")        
        
        self.combDiff.setGeometry(240, 260, 201, 31)
        self.combDiff.setStyleSheet("""font: 75 12pt Arial; 
                                    background:none;
                                    """)
        self.combDiff.addItem("")
        self.combDiff.addItem("")
        self.combDiff.addItem("")
        self.combDiff.addItem("")
        
        self.line.setGeometry(60, 400, 381, 20)
        self.line.setStyleSheet("background:none;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line_2.setGeometry(50, 400, 20, 21)
        self.line_2.setStyleSheet("background:none;")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line_3.setGeometry(430, 400, 20, 21)
        self.line_3.setStyleSheet("background:none;")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)        
        
        self.lblMain.setGeometry(130, 160, 231, 41)
        self.lblMain.setStyleSheet("background:none;\n"
"font: 75 28pt \"Arial\";\n"
"color: rgb(255, 222, 53);\n"
"")
        
        self.line_4.setGeometry(30, 230, 20, 261)
        self.line_4.setStyleSheet("background:none;")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line_5.setGeometry(450, 230, 20, 261)
        self.line_5.setStyleSheet("background:none;")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line_6.setGeometry(50, 300, 20, 21)
        self.line_6.setStyleSheet("background:none;")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        

        self.line_7.setGeometry(60, 300, 381, 20)
        self.line_7.setStyleSheet("background:none;")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line_8.setGeometry(430, 300, 20, 21)
        self.line_8.setStyleSheet("background:none;")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line_9.setGeometry(30, 510, 20, 21)
        self.line_9.setStyleSheet("background:none;")
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line_10.setGeometry(40, 510, 421, 20)
        self.line_10.setStyleSheet("background:none;")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line_11.setGeometry(450, 510, 20, 21)
        self.line_11.setStyleSheet("background:none;")
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.combGType.setGeometry(240, 350, 201, 31)
        self.combGType.setStyleSheet("font: 75 12pt Arial; background:none;")
        self.combGType.addItem("")
        self.combGType.addItem("")
        self.combGType.addItem("")
        
        self.btnMenuUser.setGeometry(590, 330, 351, 61)
        self.btnMenuUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMenuUser.setStyleSheet("background:none; background-color: green ; margin-bottom: 2%;  font-size: 24px; border-radius: 15%; color: white;")
        self.btnMenuUser.clicked.connect(self.showUserInfo)
       
        self.btnRecord.setGeometry(590, 230, 351, 61)
        self.btnRecord.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRecord.setStyleSheet("background:none; background-color: green ; margin-bottom: 2%;  font-size: 24px; border-radius: 15%; color: white;")
        self.btnRecord.clicked.connect(self.record)
        self.btnFeedback.setGeometry(590, 430, 351, 61)
        self.btnFeedback.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFeedback.setStyleSheet("background:none; background-color: green ; margin-bottom: 2%;  font-size: 24px; border-radius: 15%; color: white;")
        self.btnFeedback.clicked.connect(self.showFeedback)
        
        self.line_13.setGeometry(30, 220, 21, 16)
        self.line_13.setStyleSheet("background:none;")
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setGeometry(450, 220, 21, 16)
        self.line_14.setStyleSheet("background:none;")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setGeometry(950, 220, 20, 280)
        self.line_27.setStyleSheet("background:none;")
        self.line_27.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setGeometry(950, 210, 21, 16)
        self.line_28.setStyleSheet("background:none;")
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setGeometry(560, 220, 20, 280)
        self.line_31.setStyleSheet("background:none;")
        self.line_31.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)        
        self.line_32.setGeometry(560, 210, 21, 16)
        self.line_32.setStyleSheet("background:none;")
        self.line_32.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setGeometry(570, 400, 20, 21)
        self.line_33.setStyleSheet("background:none;")
        self.line_33.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_34.setGeometry(580, 400, 371, 20)
        self.line_34.setStyleSheet("background:none;")
        self.line_34.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_34.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_35.setGeometry(940, 400, 20, 21)
        self.line_35.setStyleSheet("background:none;")
        self.line_35.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_35.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_36 = QtWidgets.QFrame(self.pnlMainMenu)
        self.line_36.setGeometry(940, 300, 20, 21)
        self.line_36.setStyleSheet("background:none;")
        self.line_36.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_36.setFrameShadow(QtWidgets.QFrame.Sunken)        
        self.line_37.setGeometry(570, 300, 20, 21)
        self.line_37.setStyleSheet("background:none;")
        self.line_37.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setGeometry(580, 300, 371, 20)
        self.line_38.setStyleSheet("background:none;")
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setGeometry(560, 510, 20, 21)
        self.line_39.setStyleSheet("background:none;")
        self.line_39.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_40.setGeometry(950, 510, 20, 21)
        self.line_40.setStyleSheet("background:none;")
        self.line_40.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setGeometry(570, 510, 391, 20)
        self.line_41.setStyleSheet("background:none;")
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        
        self.lblHistory.setGeometry(640, 160, 231, 41)
        self.lblHistory.setStyleSheet("background:none;\n"
"font: 75 28pt \"Arial\";\n"
"color: rgb(255, 222, 53);\n"
"")
        self.lblHistory.setAlignment(QtCore.Qt.AlignCenter)
        

        self.btnMenuHelp.setGeometry(920, 30, 61, 61)
        self.btnMenuHelp.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.btnMenuHelp.setStyleSheet("background:none;\n"
"font: 15pt \"MV Boli\";\n"
"border:none;\n"
"border-image: url(info.png);")
        self.btnMenuHelp.setText("")
        self.btnMenuHelp.clicked.connect(self.seerat)
        self.btnMenuHelp.setDefault(True)
        
        self.lblMenuRight.setGeometry(360, 550, 301, 31)
        self.lblMenuRight.setStyleSheet("background:none;\n"
"color: white;\n"
"font: 75 10pt \"Arial\";")
        self.lblMenuRight.setAlignment(QtCore.Qt.AlignCenter)
        

        self.lblMenuTitle.setText("Main Menu")
        self.btnMenuStart.setText("Let\'s Start")
        self.lblDiffcult.setText("Difficulty:")
        self.lblGameType.setText("Game-Type:")
        self.combDiff.setItemText(0, "Select")
        self.combDiff.setItemText(1, "Beginner")
        self.combDiff.setItemText(2, "Intermediate")
        self.combDiff.setItemText(3, "Advance")
        self.lblMain.setText("Typing Speed")
        self.combGType.setItemText(0, "Select")
        self.combGType.setItemText(1, "Alphabets ")
        self.combGType.setItemText(2, "Alphabets + Digits")
        self.btnMenuUser.setText("User INFO")
        self.btnRecord.setText("Records")
        self.btnFeedback.setText("Feedback")
        self.lblHistory.setText("History")
        self.lblMenuRight.setText("All Rights Reversed @ Siratperoz82@gmail.com")
        
        # self.combDiff.currentIndexChanged.connect(self.showdiff)
        # self.combGType.currentIndexChanged.connect(self.showdiff)
        self.combDiff.activated.connect(self.showdiff)

    def seerat (self):
        from imp import reload
        if (self.Hdb == 0):
            import DEV
            self.Hdb  = 1
        else:
            import DEV
            reload(DEV)
            


    def record (self):
        from imp import reload
        if (self.Rdb == 0):
            import Records
            self.Rdb  = 1
        else:
            import Records
            reload(Records)        

    def sent (self):
        self.getSentence("Advance.txt")
    def showdiff (self):
        # if (self.combDiff.currentText() == 'Beginner' and self.combGType.currentText() == 'Alphabets'):
        #     ch = 'BeginnerSents.txt'
        #     print(ch)
        # elif (self.combDiff.currentText() == 'Beginner' and self.combGType.currentText() == 'Alphabets + Digits'):
        #     print("TO BASH")
        # elif (self.combDiff.currentText() == 'Intermediate' and self.combGType.currentText() == 'Alphabets'):
        #     ch = 'BeginnerSents1.txt'
        #     print(ch)        
        # elif (self.combDiff.currentText() == 'Intermediate' and self.combGType.currentText() == 'Alphabets + Digits'):
        #     ch = 'IntermediateSents.txt'
        #     print(ch)
        # elif (self.combDiff.currentText() == 'Advance' and self.combGType.currentText() == 'Alphabets'):
        #     ch = 'IntermediateSents1.txt'
        #     print(ch)
        # elif (self.combDiff.currentText() == 'Advance' and self.combGType.currentText() == 'Alphabets + Digits'):
        #     ch = 'AdvanceSents.txt'
        #     print(ch)     

        self.cnt = 0
        self.getRand = ''
        self.totleT = 0.0
        self.startTime = 0.0
        self.stopTime = 0.0
        self.accuracy = 0.0
        self.wpm = 0
        self.keyCnt = 0
        if (self.combDiff.currentText() == 'Beginner'):
            self.ch = 'BeginnerSents.txt'
            print(self.ch)
        elif (self.combDiff.currentText() == 'Intermediate'):
            self.ch = 'Intermediate.txt'
            print(self.ch)
        elif (self.combDiff.currentText() == 'Advance'):
            self.ch = 'Advance.txt'
            print(self.ch)                
        self.getSentence(self.ch)

# 


       
        
    
    # function To Display Welcome Screen Widget
    def welcScreen(self):
        # Setting the Size of Widget
        self.pnlWelcome.setGeometry(0, 0, 1000, 600)
        # Appling the image in the widget
        self.pnlWelcome.setStyleSheet("border-image: url(welcome.jpg);")
        #Setting Cursor to Waitting Mode
        self.pnlWelcome.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))

        # Adding delay
        time.sleep(3)
        # Hidding the panel
        self.pnlWelcome.hide()
        self.LoginPanel()
        
        
    # FUNCTION FOR Guest Button    
    def msgGuest (self):
        guestSignal = dConnect.dbConnect().guestInfo()
        if (guestSignal != 'Nabod'):
            self.pnlLogin.hide()            
            # Panel Settings
            self.pnlWmsg.setGeometry(0, 0, 1000, 600)
            self.pnlWmsg.show()
            self.pnlWmsg.setStyleSheet("background-image:url(WLC1.jpg);")
            self.pnlWmsg.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        
            # pnlWmsg label to show user name
            self.lblWlcUser.setGeometry(160, 360, 691, 81)
            self.lblWlcUser.setStyleSheet("font: 75 35pt \"Arial\";\n"
                                          "background:none;\n"
                                          "color: rgb(255, 170, 0);")
            self.lblWlcUser.setAlignment(QtCore.Qt.AlignCenter)
            self.lblWlcUser.setText(guestSignal)
            self.lblWlcUser.show()
            # 3 second wait and display main menu
            wlc2 = threading.Timer(2.0,self.MainMenu)
            wlc2.start()
        else:
            pass
            
            
            
        
    #   Login Panel Settings.
    def LoginPanel (self):
        self.pnlLogin.show()
        
        
    def showMainMenu (self):
        self.pnlType.hide()
        self.pnlMainMenu.show()

    
    # Function to get Random Sentence 
    def getSentence(self,choices):
        try:    
            # sents = 'Sentences.txt'
            file = choices
            mySentence = open(file).read()
            sp = mySentence.split('\n')
            randomSen = random.choice(sp)
            if (randomSen != ''):
                self.getRand = randomSen
                self.lblType.setText(randomSen)
            else:
                self.getSentence()
        except Exception as ex:
            error = str(ex)
            self.boxError.setText("The Sentence file is not found\n."+error) 
            self.boxError.setWindowTitle("Error")
            self.boxError.setWindowIcon(QIcon("Error.png"))
            self.boxError.setStyleSheet("color:black; font: 9pt Arial; background:none; background-color:white;")
            self.boxError.show()
        
    
    
    # Function to start timer
    def timeStart(self):
        if (self.cnt == 0 and self.txtType.text() !=""):
            try:
                
                self.startTime = timeit.default_timer()
                
            except Exception as s:
                er = str(s)
                self.boxError.setText("Error:\n."+er) 
                self.boxError.setWindowTitle("Error")
                self.boxError.setWindowIcon(QIcon("Error.png"))
                self.boxError.setStyleSheet("color:black; font: 9pt Arial; background:none; background-color:white;")
                self.boxError.show()

            self.cnt+=1
                
        else:
            pass
    

    
        
    # Funtion after the Enter key is pressed to calculate time
    def enterKey(self):
        if (self.keyCnt == 0):
            
            self.stopTime = timeit.default_timer()
            self.totleT =  self.stopTime -  self.startTime
            # print("This is the Stop Time:  ", f"{self.stopTime:.2f}")
            # print("This is the Total Time:   ", f'{self.totleT:.2f}'," Sec") 
            
            # print("The text from PC: ",self.getRand)  
            
            valid = 0
            for i,x in enumerate(self.txtType.text()):
                try:
                    if (self.getRand[i] == x):
                        valid+=1
                except:
                    pass
            # print("Valid words: ",valid)
            
            # to show accuracy we need to divide the lenght of words in 5 * by 100
            # we can estimate the average lenght of words as 5. To shwo accuracy as
            # Average we need to divide it by 100
            
            self.accuracy = valid/len(self.getRand)*100
            # print("Total Accuracy: ",f"{self.accuracy:.2f}"," %")
            
            # To calculate the Word pre Minute 
            
            self.wpm = int(len(self.getRand)*60 / (5*self.totleT))
            # print("Words per Minute: ", f"{self.wpm:.2f}"," wpm")
            
            # Converting LineEdit into string to set it for label
            tmt = str(f'{self.totleT:.2f}')
            acc = str(f"{self.accuracy:.2f}")
            WPM = str( f"{self.wpm:.0f}")
            
            self.lblResult.show()
            self.lblResult.setText("Time: "+tmt+" Sec                Accuracy: "+acc+" %                Wpm: "+WPM+" wpm")
            
            ExID = open('temID.txt').read()
            # print(ExID)
            dConnect.dbConnect().instRecord(ExID,self.ch,tmt,WPM,acc)
            
            # to SHOW Reset Button
            self.btnReset.show()
            self.keyCnt +=1
        else:
            self.RestMessage()
            #print("You should reset teh game.")
        
        
        
    # Function Reset the Screen
    def btnReset_Clicked(self):
        #print("FUck you")
        self.cnt = 0
        self.getRand = ''
        self.totleT = 0.0
        self.startTime = 0.0
        self.stopTime = 0.0
        self.accuracy = 0.0
        self.wpm = 0
        self.keyCnt = 0
        self.showdiff()
        self.txtType.setText("")
        self.lblResult.setText("")
        self.btnReset.hide()
        self.lblResult.hide()
        
    def RestMessage(self):
        self.msg.setText("<font size=15 > You must press <b>Restart</b> button </font>")
        self.msg.setWindowTitle("Warning")
        self.msg.setWindowIcon(QIcon("Warning.png"))
        self.msg.setStyleSheet("color:yellow; font: 9pt Kristen ITC; background:none; border-image:url(Copy of restart.jpg)")
        self.msg.show()


    # Login Sing up Button
    def Register(self):
        self.txtName.setText("")
        self.txtEmail.setText("")
        self.txtLastNameP.setText("")
        self.txtPassP.setText("")
        self.txtUName.setText("")
        self.pnlLogin.hide()
        self.pnlRegister.show()


    # Register Back button    
    def Back2Login(self):
        self.txtLpass.setText("")
        self.txtLuser.setText("")
        self.pnlRegister.hide()
        self.pnlMainMenu.hide()
        self.pnlLogin.show()
        
                    

    # Show Welcome Message when user login
    def MsgWLC (self):
        UserDBname = dConnect.dbConnect().checkLogin(self.txtLuser.text(),self.txtLpass.text())
        Error = str(UserDBname)
        print(Error)
        if (UserDBname != "N/A USER"):
            self.pnlLogin.hide()            
            # Panel Settings
            self.pnlWmsg.setGeometry(0, 0, 1000, 600)
            self.pnlWmsg.show()
            self.pnlWmsg.setStyleSheet("background-image:url(WLC1.jpg);")
            self.pnlWmsg.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        
            # pnlWmsg label to show user name
            self.lblWlcUser.setGeometry(160, 360, 691, 81)
            self.lblWlcUser.setStyleSheet("font: 75 35pt \"Arial\";\n"
                                          "background:none;\n"
                                          "color: rgb(255, 170, 0);")
            self.lblWlcUser.setAlignment(QtCore.Qt.AlignCenter)
            self.lblWlcUser.setText(UserDBname)
            # 3 second wait and display main menu
            wlc2 = threading.Timer(2.0,self.MainMenu)
            wlc2.start()
        else:
            self.logmsg.setText("Error: "+"Worng User or Password")
            self.logmsg.setWindowTitle("Error")
            self.logmsg.setWindowIcon(QIcon("Error.png"))
            self.logmsg.setStyleSheet("color:black; font: 10pt Kristen ITC; background:none;")
            self.logmsg.show()
    
        
    # Function to display the Main Menu
    def MainMenu (self):
        self.pnlWmsg.hide()        
        self.pnlMainMenu.show()
        
    # Function to start UserInfo Window
    def showUserInfo (self):
        from imp import reload
        if (self.imp == 0):
            import UserInfo
            self.imp  = 1
        else:
            import UserInfo
            reload(UserInfo)
            

    # Function to start Feedback Window
    def showFeedback (self):
        from imp import reload
        if (self.fdb == 0):
            import Feedback
            self.fdb  = 1
        else:
            import Feedback
            reload(Feedback)
        

    
    # Function to start Typing Window
    def showTyping (self):
        self.pnlMainMenu.hide()
        self.pnlType.show()
        
        
        
    # Function to display password     
    def btnstate(self):
        if  (self.btnShowPA.isChecked()):
            self.btnShowPA.setStyleSheet("border-image: url(HidePass.png);background:none;")
            self.txtLpass.setEchoMode(QtWidgets.QLineEdit.Password)
            

        else:
            self.btnShowPA.setStyleSheet("border-image: url(showPass.png);background:none;")
            self.txtLpass.setEchoMode(QtWidgets.QLineEdit.Normal)
           
            
            
     # Function to display password     
    def btnstate2(self):
        if  self.chkShowPA.isChecked():
            self.chkShowPA.setStyleSheet("border-image: url(HidePass.png);background:none;")
            self.txtPassP.setEchoMode(QtWidgets.QLineEdit.Password)            

        else:
            self.chkShowPA.setStyleSheet("border-image: url(showPass.png);background:none;")
            self.txtPassP.setEchoMode(QtWidgets.QLineEdit.Normal)
            
          
            
    # Function to shutdown the program
    def shutdown (self):
        MainWindow.hide()
        sys.exit(app.exec_())
        QtWidgets.QApplication.instance().quit
    
    
    # Function to register the user on Database
    def UserReg (self):      
        InSt = dConnect.dbConnect().InsertInfo(self.txtName.text(),self.txtLastNameP.text(),self.txtUName.text(),self.txtPassP.text(),self.txtEmail.text())
        if (InSt != -100):    
            self.regis.setText("<h1> You have sucessfully registered </h1>")
            self.regis.setWindowTitle("Registered")
            self.regis.setWindowIcon(QIcon("Information.png"))
            self.regis.setInformativeText(f"<b>Mr: {self.txtName.text()} {self.txtLastNameP.text()}")
            self.regis.setDetailedText(f"""
GameID:    {InSt}
UserName: {self.txtUName.text()}
Password: {self.txtPassP.text()}
""")
            self.regis.setStyleSheet("color:black; font: 10pt Arial ITC; background:none;")
            self.regis.show()
            self.Back2Login()
        else:
            self.regis.setText("Error: Please enter a different Username.")
            self.regis.setWindowTitle("Error")
            self.regis.setWindowIcon(QIcon("Error.png"))
            self.regis.setStyleSheet("color:black; font: 12pt Kristen ITC; background:none;")
            self.regis.show()
          
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.Run_Game(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# TO get the text from a line edit

           # j = self.txtType.text()
            # print(j)
