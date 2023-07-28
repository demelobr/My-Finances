# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/demelobr/Documents/My Codes/Qt/My Finances/ui/register.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        MainWindow.setMaximumSize(QtCore.QSize(400, 600))
        MainWindow.setStyleSheet("background-color: rgb(31, 35, 38);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fr_top = QtWidgets.QFrame(self.centralwidget)
        self.fr_top.setGeometry(QtCore.QRect(0, 0, 400, 45))
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
        self.fr_error_msg.setFrameShape(QtWidgets.QFrame.NoFrame)
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
        self.lb_error_msg.setStyleSheet("color: rgb(255, 255, 255);")
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/close/icons/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.fr_error_msg)
        self.fr_content = QtWidgets.QFrame(self.centralwidget)
        self.fr_content.setGeometry(QtCore.QRect(0, 45, 400, 520))
        self.fr_content.setStyleSheet("")
        self.fr_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content.setObjectName("fr_content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fr_content)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fr_register_area = QtWidgets.QFrame(self.fr_content)
        self.fr_register_area.setMaximumSize(QtCore.QSize(350, 450))
        self.fr_register_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_register_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_register_area.setObjectName("fr_register_area")
        self.lb_logo = QtWidgets.QLabel(self.fr_register_area)
        self.lb_logo.setGeometry(QtCore.QRect(135, 50, 80, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_logo.setFont(font)
        self.lb_logo.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_logo.setObjectName("lb_logo")
        self.ld_name = QtWidgets.QLineEdit(self.fr_register_area)
        self.ld_name.setGeometry(QtCore.QRect(50, 100, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_name.setFont(font)
        self.ld_name.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_name.setMaxLength(20)
        self.ld_name.setObjectName("ld_name")
        self.ld_username = QtWidgets.QLineEdit(self.fr_register_area)
        self.ld_username.setGeometry(QtCore.QRect(50, 160, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_username.setFont(font)
        self.ld_username.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_username.setMaxLength(20)
        self.ld_username.setObjectName("ld_username")
        self.ld_password = QtWidgets.QLineEdit(self.fr_register_area)
        self.ld_password.setGeometry(QtCore.QRect(50, 220, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_password.setFont(font)
        self.ld_password.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_password.setMaxLength(20)
        self.ld_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ld_password.setObjectName("ld_password")
        self.ld_confirm_password = QtWidgets.QLineEdit(self.fr_register_area)
        self.ld_confirm_password.setGeometry(QtCore.QRect(50, 280, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_confirm_password.setFont(font)
        self.ld_confirm_password.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_confirm_password.setMaxLength(20)
        self.ld_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ld_confirm_password.setObjectName("ld_confirm_password")
        self.ld_email = QtWidgets.QLineEdit(self.fr_register_area)
        self.ld_email.setGeometry(QtCore.QRect(50, 340, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_email.setFont(font)
        self.ld_email.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_email.setMaxLength(40)
        self.ld_email.setObjectName("ld_email")
        self.btn_register = QtWidgets.QPushButton(self.fr_register_area)
        self.btn_register.setGeometry(QtCore.QRect(200, 410, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_register.setFont(font)
        self.btn_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_register.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(0, 139, 209);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 130, 215);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 122, 209);\n"
"}")
        self.btn_register.setObjectName("btn_register")
        self.frame = QtWidgets.QFrame(self.fr_register_area)
        self.frame.setGeometry(QtCore.QRect(150, 0, 50, 50))
        self.frame.setStyleSheet("background-image: url(:/logo/finance-menor.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4.addWidget(self.fr_register_area)
        self.fr_button = QtWidgets.QFrame(self.centralwidget)
        self.fr_button.setGeometry(QtCore.QRect(0, 565, 400, 35))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ld_name, self.ld_username)
        MainWindow.setTabOrder(self.ld_username, self.ld_password)
        MainWindow.setTabOrder(self.ld_password, self.ld_confirm_password)
        MainWindow.setTabOrder(self.ld_confirm_password, self.ld_email)
        MainWindow.setTabOrder(self.ld_email, self.btn_register)
        MainWindow.setTabOrder(self.btn_register, self.btn_close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Register"))
        self.lb_error_msg.setText(_translate("MainWindow", "Error"))
        self.lb_logo.setText(_translate("MainWindow", "My Finances"))
        self.ld_name.setPlaceholderText(_translate("MainWindow", "Name"))
        self.ld_username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.ld_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.ld_confirm_password.setPlaceholderText(_translate("MainWindow", "Confirm password"))
        self.ld_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.btn_register.setText(_translate("MainWindow", "Register"))
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
