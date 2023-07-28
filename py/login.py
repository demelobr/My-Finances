# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/demelobr/Documents/My Codes/Qt/My Finances/ui/login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(31, 35, 38);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fr_top = QtWidgets.QFrame(self.centralwidget)
        self.fr_top.setMinimumSize(QtCore.QSize(0, 0))
        self.fr_top.setMaximumSize(QtCore.QSize(16777215, 45))
        self.fr_top.setStyleSheet("")
        self.fr_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_top.setObjectName("fr_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fr_top)
        self.horizontalLayout.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fr_error_msg = QtWidgets.QFrame(self.fr_top)
        self.fr_error_msg.setMaximumSize(QtCore.QSize(350, 16777215))
        self.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128);\n"
"border-radius: 5px;")
        self.fr_error_msg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_error_msg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_error_msg.setObjectName("fr_error_msg")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fr_error_msg)
        self.horizontalLayout_2.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_error_msg = QtWidgets.QLabel(self.fr_error_msg)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_error_msg.setFont(font)
        self.lb_error_msg.setStyleSheet("color: rgb(255,255,255);")
        self.lb_error_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_error_msg.setObjectName("lb_error_msg")
        self.horizontalLayout_2.addWidget(self.lb_error_msg)
        self.btn_close = QtWidgets.QPushButton(self.fr_error_msg)
        self.btn_close.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-image: url(:/close/cil-x.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(50,50,50);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35,35,35);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.fr_error_msg)
        self.verticalLayout.addWidget(self.fr_top)
        self.fr_content = QtWidgets.QFrame(self.centralwidget)
        self.fr_content.setStyleSheet("")
        self.fr_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content.setObjectName("fr_content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fr_content)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fr_login_area = QtWidgets.QFrame(self.fr_content)
        self.fr_login_area.setMaximumSize(QtCore.QSize(350, 450))
        self.fr_login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_login_area.setObjectName("fr_login_area")
        self.fr_logo = QtWidgets.QFrame(self.fr_login_area)
        self.fr_logo.setGeometry(QtCore.QRect(114, 40, 121, 121))
        self.fr_logo.setStyleSheet("background-image: url(:/logo/finance-maior.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.fr_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_logo.setObjectName("fr_logo")
        self.lb_name_logo = QtWidgets.QLabel(self.fr_login_area)
        self.lb_name_logo.setGeometry(QtCore.QRect(125, 150, 100, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lb_name_logo.setFont(font)
        self.lb_name_logo.setMouseTracking(True)
        self.lb_name_logo.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_name_logo.setObjectName("lb_name_logo")
        self.ld_username = QtWidgets.QLineEdit(self.fr_login_area)
        self.ld_username.setGeometry(QtCore.QRect(50, 220, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_username.setFont(font)
        self.ld_username.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_username.setMaxLength(30)
        self.ld_username.setObjectName("ld_username")
        self.ld_password = QtWidgets.QLineEdit(self.fr_login_area)
        self.ld_password.setGeometry(QtCore.QRect(50, 280, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_password.setFont(font)
        self.ld_password.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ld_password.setObjectName("ld_password")
        self.lb_question = QtWidgets.QLabel(self.fr_login_area)
        self.lb_question.setGeometry(QtCore.QRect(50, 340, 191, 19))
        font = QtGui.QFont()
        font.setBold(True)
        self.lb_question.setFont(font)
        self.lb_question.setStyleSheet("color: rgb(200,200,200);")
        self.lb_question.setObjectName("lb_question")
        self.btn_click_here = QtWidgets.QPushButton(self.fr_login_area)
        self.btn_click_here.setGeometry(QtCore.QRect(240, 340, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_click_here.setFont(font)
        self.btn_click_here.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_click_here.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 140, 227);\n"
"    border-radius: 1px;\n"
"    margin: 0,0,0,0;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(0, 130, 215);\n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgb(0, 122, 209);\n"
"}")
        self.btn_click_here.setObjectName("btn_click_here")
        self.btn_login = QtWidgets.QPushButton(self.fr_login_area)
        self.btn_login.setGeometry(QtCore.QRect(200, 380, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(0, 139, 209);\n"
"    background-color: rgb(85, 170, 255);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 130, 215);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 122, 209);\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_4.addWidget(self.fr_login_area)
        self.verticalLayout.addWidget(self.fr_content)
        self.fr_button = QtWidgets.QFrame(self.centralwidget)
        self.fr_button.setMaximumSize(QtCore.QSize(16777215, 35))
        self.fr_button.setStyleSheet("")
        self.fr_button.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_button.setObjectName("fr_button")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fr_button)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_credits = QtWidgets.QLabel(self.fr_button)
        self.lb_credits.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-right: 5px;")
        self.lb_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_credits.setObjectName("lb_credits")
        self.horizontalLayout_3.addWidget(self.lb_credits)
        self.verticalLayout.addWidget(self.fr_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ld_username, self.ld_password)
        MainWindow.setTabOrder(self.ld_password, self.btn_click_here)
        MainWindow.setTabOrder(self.btn_click_here, self.btn_login)
        MainWindow.setTabOrder(self.btn_login, self.btn_close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lb_error_msg.setText(_translate("MainWindow", "Error"))
        self.lb_name_logo.setText(_translate("MainWindow", "<html><head/><body><p>My Finances</p></body></html>"))
        self.ld_username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.ld_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lb_question.setText(_translate("MainWindow", "You don\'t have your account?"))
        self.btn_click_here.setText(_translate("MainWindow", "Click here!"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.lb_credits.setText(_translate("MainWindow", "<html><head/><body><p>Alfa v1.0.0, developer by <span style=\" font-weight:600;\">Bruno Melo.</span></p></body></html>"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
