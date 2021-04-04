# -*- coding: utf-8 -*-
# Made with <3 by Bonsai & Wasaby

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon("./images/logo.jpg"))
        MainWindow.resize(1020, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1020, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1020, 600))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(231, 230, 236);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.search = QtWidgets.QFrame(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(0, 0, 340, 80))
        self.search.setStyleSheet("background-color: transparent;\n"
"border: solid #cec7c9; border-width: 0px 1px 0px 0px;")
        self.search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search.setObjectName("search")
        
        self.search_contact = QtWidgets.QLineEdit(self.search)
        self.search_contact.setGeometry(QtCore.QRect(34, 38, 227, 27))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.search_contact.setFont(font)
        self.search_contact.setStyleSheet("border: none;\n"
"border-radius: 5px; \n"
"background-color: rgba(150, 150, 150, 100);\n"
"padding: 5px;")
        self.search_contact.setObjectName("search_contact")
        
        self.new_message = QtWidgets.QPushButton(self.search)
        self.new_message.setGeometry(QtCore.QRect(281, 40, 38, 27))
        self.new_message.setStyleSheet("border: none;\n"
"background-color: white;\n"
"border-radius: 5px;")
        self.new_message.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/new_message.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_message.setIcon(icon)
        self.new_message.setIconSize(QtCore.QSize(100, 18))
        self.new_message.setObjectName("new_message")
        self.new_message.clicked.connect(self.newMessage)
        
        self.contacts = QtWidgets.QFrame(self.centralwidget)
        self.contacts.setGeometry(QtCore.QRect(0, 80, 340, 521))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.contacts.setFont(font)
        self.contacts.setStyleSheet("background-color: transparent;\n"
"border: solid #cec7c9; border-width: 1px;")
        self.contacts.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contacts.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contacts.setObjectName("contacts")
        
        self.bonsai = QtWidgets.QFrame(self.contacts)
        self.bonsai.setGeometry(QtCore.QRect(0, 0, 340, 80))
        self.bonsai.setStyleSheet("background-color: #2d7ef1;\n"
"border: solid #cec7c9; border-width: 1px 0px 0px 0px;")
        self.bonsai.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bonsai.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bonsai.setObjectName("bonsai")
        self.bonsai.setVisible(False)
        
        self.pdp = QtWidgets.QLabel(self.bonsai)
        self.pdp.setGeometry(QtCore.QRect(34, 10, 60, 60))
        self.pdp.setStyleSheet("border: none;")
        self.pdp.setText("")
        self.pdp.setPixmap(QtGui.QPixmap("./images/pdp_bonsai.png"))
        self.pdp.setScaledContents(True)
        self.pdp.setIndent(-10)
        self.pdp.setObjectName("pdp")
        
        self.username = QtWidgets.QLabel(self.bonsai)
        self.username.setGeometry(QtCore.QRect(109, 10, 60, 18))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setStyleSheet("border: none;\n"
"color: white;")
        self.username.setObjectName("username")
        
        self.catchphrase = QtWidgets.QLabel(self.bonsai)
        self.catchphrase.setGeometry(QtCore.QRect(109, 30, 150, 18))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.catchphrase.setFont(font)
        self.catchphrase.setStyleSheet("border: none;\n"
"color: white;")
        self.catchphrase.setObjectName("catchphrase")
        
        self.wasaby = QtWidgets.QFrame(self.contacts)
        self.wasaby.setGeometry(QtCore.QRect(34, 80, 306, 80))
        self.wasaby.setStyleSheet("background-color: transparent;\n"
"border: solid #cec7c9; border-width: 0px 0px 1px 0px;")
        self.wasaby.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wasaby.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wasaby.setObjectName("wasaby")
        self.wasaby.setVisible(False)
        
        self.pdp_2 = QtWidgets.QLabel(self.wasaby)
        self.pdp_2.setGeometry(QtCore.QRect(0, 10, 60, 60))
        self.pdp_2.setStyleSheet("border: none;")
        self.pdp_2.setText("")
        self.pdp_2.setPixmap(QtGui.QPixmap("./images/pdp_wasaby.png"))
        self.pdp_2.setScaledContents(True)
        self.pdp_2.setIndent(-10)
        self.pdp_2.setObjectName("pdp_2")
        
        self.username_2 = QtWidgets.QLabel(self.wasaby)
        self.username_2.setGeometry(QtCore.QRect(75, 10, 60, 18))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.username_2.setFont(font)
        self.username_2.setStyleSheet("border: none;\n"
"color: black;")
        
        self.username_2.setObjectName("username_2")
        self.catchphrase_2 = QtWidgets.QLabel(self.wasaby)
        self.catchphrase_2.setGeometry(QtCore.QRect(75, 30, 150, 18))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.catchphrase_2.setFont(font)
        self.catchphrase_2.setStyleSheet("border: none;\n"
"color: rgb(150, 150, 150);")
        self.catchphrase_2.setObjectName("catchphrase_2")
        
        self.current_conv = QtWidgets.QFrame(self.centralwidget)
        self.current_conv.setGeometry(QtCore.QRect(340, 0, 680, 80))
        self.current_conv.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.current_conv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.current_conv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.current_conv.setObjectName("current_conv")
        
        self.to = QtWidgets.QLabel(self.current_conv)
        self.to.setGeometry(QtCore.QRect(34, 38, 25, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.to.setFont(font)
        self.to.setStyleSheet("color: rgb(125, 125, 125);")
        self.to.setObjectName("to")
        
        self.coquishell = QtWidgets.QLabel(self.current_conv)
        self.coquishell.setGeometry(QtCore.QRect(64, 38, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.coquishell.setFont(font)
        self.coquishell.setObjectName("coquishell")
        
        self.details = QtWidgets.QLabel(self.current_conv)
        self.details.setGeometry(QtCore.QRect(601, 38, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.details.setFont(font)
        self.details.setStyleSheet("color: rgb(38, 143, 255);")
        self.details.setObjectName("details")
        self.details.setOpenExternalLinks(True)
        
        self.conv = QtWidgets.QFrame(self.centralwidget)
        self.conv.setGeometry(QtCore.QRect(340, 80, 680, 476))
        self.conv.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.conv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conv.setObjectName("conv")
        
        self.frame = QtWidgets.QFrame(self.conv)
        self.frame.setGeometry(QtCore.QRect(365, 431, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame.setFont(font)
        self.frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame.setStyleSheet("border: none;\n"
"background-color: rgb(38, 143, 255);\n"
"color: white;\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.request = QtWidgets.QLabel(self.frame)
        self.request.setGeometry(QtCore.QRect(0, 0, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.request.setFont(font)
        self.request.setObjectName("request")
        
        self.frame_2 = QtWidgets.QFrame(self.conv)
        self.frame_2.setGeometry(QtCore.QRect(15, 15, 300, 406))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame_2.setFont(font)
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setStyleSheet("border: none;\n"
"background-color: rgb(225, 225, 225);\n"
"color: black;\n"
"border-radius: 15px;\n"
"padding: 5px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.answer = QtWidgets.QLabel(self.frame_2)
        self.answer.setGeometry(QtCore.QRect(0, 0, 300, 406))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.answer.setFont(font)
        self.answer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.answer.setWordWrap(True)
        self.answer.setObjectName("answer")
        
        self.typing = QtWidgets.QFrame(self.centralwidget)
        self.typing.setGeometry(QtCore.QRect(340, 555, 680, 45))
        self.typing.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.typing.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.typing.setFrameShadow(QtWidgets.QFrame.Raised)
        self.typing.setObjectName("typing")
        
        self.message = QtWidgets.QLineEdit(self.typing)
        self.message.setGeometry(QtCore.QRect(34, 10, 567, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.message.setFont(font)
        self.message.setStyleSheet("border: none;\n"
"border-radius: 12px; \n"
"background-color: rgba(150, 150, 150, 100);\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.message.setObjectName("message")
        
        self.send = QtWidgets.QPushButton(self.typing)
        self.send.setGeometry(QtCore.QRect(610, 10, 25, 25))
        self.send.setStyleSheet("border: none;\n"
"background-color: transparent;\n"
"border-radius: 10px;")
        self.send.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send.setIcon(icon1)
        self.send.setIconSize(QtCore.QSize(29, 29))
        self.send.setObjectName("send")
        self.send.clicked.connect(self.shell)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.status = "up"

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coquishell"))
        self.search_contact.setPlaceholderText(_translate("MainWindow", "Search"))
        self.username.setText(_translate("MainWindow", "Bonsaï"))
        self.catchphrase.setText(_translate("MainWindow", "If your homeless..."))
        self.username_2.setText(_translate("MainWindow", "Wasaby"))
        self.catchphrase_2.setText(_translate("MainWindow", "...just by a house!"))
        self.to.setText(_translate("MainWindow", "To:"))
        self.coquishell.setText(_translate("MainWindow", "Coquishell"))
        self.details.setText(_translate("MainWindow", "<a style='text-decoration: none; color: rgb(52, 129, 254); outline: 0; cursor: auto;' href='https://doodling.fr'>Details</a>"))
        self.request.setText(_translate("MainWindow", "Made for SurpriseHacks hackaton !"))
        self.answer.setText(_translate("MainWindow", "What if you send: \"help\"?"))
        self.message.setPlaceholderText(_translate("MainWindow", "iMessage"))
        self.send.setShortcut(_translate("MainWindow", "Return"))
        
    def newMessage(self):
        if not self.bonsai.isVisible() and not self.wasaby.isVisible() and self.status == "up":
            self.bonsai.setVisible(True)
            return
        if self.bonsai.isVisible() and not self.wasaby.isVisible() and self.status == "up":
            self.wasaby.setVisible(True)
            self.status = "down"
            return
        elif self.bonsai.isVisible() and not self.wasaby.isVisible() and self.status == "down":
            self.bonsai.setVisible(False)
            self.status = "up"
            return
        elif self.bonsai.isVisible() and self.wasaby.isVisible() and self.status == "down":
            self.wasaby.setVisible(False)
            return

    def shell(self):
        message = self.message.text()
        args = message.split(" ")
        
        if message != "":
            if args[0] == "cd":
                if len(args) == 2 and args[1] != "":
                    try:
                        os.chdir(args[1])
                        self.answer.setText("Current directory : %s" % os.getcwd())
                        self.answer.returncode = 0
                    except FileNotFoundError:
                        self.answer.setText("Directory / file not found!")
                else:
                    self.answer.setText("No directory / file specified!")
            elif args[0] == "color":
                try:
                    args_color = message.split(" ")[1]
                except IndexError:
                    self.answer.setText("No color specified!")
                    self.request.setText(message)
                    self.message.clear()
                    return
                    
                args_list = list(args_color)
                print(args_list)

                colors = {
                    "0": "12, 12, 12",  # black
                    "1": "0 , 255, 218",  # dark_blue
                    "2": "19, 161, 14",  # dark_green
                    "3": "58, 150, 221",  # dark_cyan
                    "4": "197, 15, 31",  # dark_red
                    "5": "136, 23, 152",  # dark_magenta
                    "6": "193, 156, 0",  # dark_yellow
                    "7": "204, 204, 204",  # dark_white
                    "8": "118, 118, 118",  # bright_black
                    "9": "59, 120, 255",  # bright_blue
                    "A": "22, 198, 12",  # bright_green
                    "B": "97, 214, 214",  # bright_cyan
                    "C": "231, 72, 86",  # bright_red
                    "D": "180, 0, 158",  # bright_magenta
                    "E": "249, 241, 165",  # bright_yellow
                    "F": "242, 242, 242"  # white
                }
        
                for arg in args_list:
                    if arg.upper() not in colors:
                        self.answer.setText("Invalid color!")
                        return

                if len(args_color) == 2:
                    bg_color = colors[args_list[0].upper()]
                    font_color = colors[args_list[1].upper()]
                    print(bg_color, font_color)
                    self.conv.setStyleSheet("background-color: rgb(%s) !important;" % bg_color)
                    self.answer.setStyleSheet("color: rgb(%s);" % font_color)
                    self.request.setStyleSheet("color: rgb(%s);" % font_color)
                    print("background-color: rgb(%s); color: rgb(%s);" % (bg_color, font_color))
                elif len(args_color) == 1:
                    font_color = colors[args_list[0].upper()]
                    print(font_color)
                    self.answer.setStyleSheet("color: rgb(%s);" % font_color)
                    self.request.setStyleSheet("color: rgb(%s);" % font_color)
                    print("color: rgb(%s);" % font_color)
                else:
                    self.answer.setText("No color specified!")
            else:
                answer = subprocess.run(message, shell=True, capture_output=True, text=True)
            self.message.clear()
            self.request.setText(message)

            if args[0] != "cd" and args[0] != "color" and answer.returncode == 0 or message == "help":
                self.answer.setText(answer.stdout)
            elif args[0] != "cd" and args[0] != "color":
                self.answer.setText(answer.stderr)
                print(answer.returncode)
        else:
            print("No command entered!") 
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
