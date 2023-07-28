# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/demelobr/Documents/My Codes/Qt/My Finances/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(31, 35, 38);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fr_top = QtWidgets.QFrame(self.centralwidget)
        self.fr_top.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_top.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_top.setObjectName("fr_top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fr_top)
        self.horizontalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fr_top_logo = QtWidgets.QFrame(self.fr_top)
        self.fr_top_logo.setMaximumSize(QtCore.QSize(145, 16777215))
        self.fr_top_logo.setStyleSheet("")
        self.fr_top_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_top_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_top_logo.setObjectName("fr_top_logo")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fr_top_logo)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fr_logo = QtWidgets.QFrame(self.fr_top_logo)
        self.fr_logo.setMinimumSize(QtCore.QSize(50, 50))
        self.fr_logo.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fr_logo.setStyleSheet("background-image: url(:/logo/finance-menor.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.fr_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_logo.setObjectName("fr_logo")
        self.horizontalLayout_5.addWidget(self.fr_logo)
        self.lb_logo = QtWidgets.QLabel(self.fr_top_logo)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lb_logo.setFont(font)
        self.lb_logo.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.lb_logo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_logo.setObjectName("lb_logo")
        self.horizontalLayout_5.addWidget(self.lb_logo)
        self.horizontalLayout_2.addWidget(self.fr_top_logo)
        self.fr_top_error_msg = QtWidgets.QFrame(self.fr_top)
        self.fr_top_error_msg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fr_top_error_msg.setStyleSheet("")
        self.fr_top_error_msg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_top_error_msg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_top_error_msg.setObjectName("fr_top_error_msg")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fr_top_error_msg)
        self.horizontalLayout_3.setContentsMargins(0, 15, 150, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fr_error_msg = QtWidgets.QFrame(self.fr_top_error_msg)
        self.fr_error_msg.setMaximumSize(QtCore.QSize(350, 35))
        self.fr_error_msg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128);\n"
"border-radius: 5px;")
        self.fr_error_msg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_error_msg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_error_msg.setObjectName("fr_error_msg")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fr_error_msg)
        self.horizontalLayout_4.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lb_error_msg = QtWidgets.QLabel(self.fr_error_msg)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_error_msg.setFont(font)
        self.lb_error_msg.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_error_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_error_msg.setObjectName("lb_error_msg")
        self.horizontalLayout_4.addWidget(self.lb_error_msg)
        self.btn_error_msg = QtWidgets.QPushButton(self.fr_error_msg)
        self.btn_error_msg.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_error_msg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_error_msg.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    /*background-image: url(:/close/cil-x.png);*/\n"
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
        self.btn_error_msg.setText("")
        self.btn_error_msg.setObjectName("btn_error_msg")
        self.horizontalLayout_4.addWidget(self.btn_error_msg)
        self.horizontalLayout_3.addWidget(self.fr_error_msg)
        self.horizontalLayout_2.addWidget(self.fr_top_error_msg)
        self.verticalLayout.addWidget(self.fr_top)
        self.fr_content = QtWidgets.QFrame(self.centralwidget)
        self.fr_content.setStyleSheet("")
        self.fr_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content.setObjectName("fr_content")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.fr_content)
        self.horizontalLayout_6.setContentsMargins(20, 15, 20, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fr_content_left_menu = QtWidgets.QFrame(self.fr_content)
        self.fr_content_left_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.fr_content_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.fr_content_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_content_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content_left_menu.setObjectName("fr_content_left_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fr_content_left_menu)
        self.verticalLayout_2.setContentsMargins(0, 10, 10, 10)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fr_left_menu = QtWidgets.QFrame(self.fr_content_left_menu)
        self.fr_left_menu.setMaximumSize(QtCore.QSize(70, 600))
        self.fr_left_menu.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.fr_left_menu.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"/*background-color: rgb(85, 170, 255);*/\n"
"border-radius: 5px;")
        self.fr_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_left_menu.setObjectName("fr_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fr_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fr_left_menu_top = QtWidgets.QFrame(self.fr_left_menu)
        self.fr_left_menu_top.setMinimumSize(QtCore.QSize(60, 0))
        self.fr_left_menu_top.setStyleSheet("")
        self.fr_left_menu_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_left_menu_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_left_menu_top.setObjectName("fr_left_menu_top")
        self.btn_home = QtWidgets.QPushButton(self.fr_left_menu_top)
        self.btn_home.setGeometry(QtCore.QRect(14, 68, 32, 32))
        self.btn_home.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_home.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-image: url(:/home/graph-home-white-32x32.svg);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QPushButton:hover{\n"
"    background-image: url(:/home/graph-home-green-32x32.svg);\n"
"}")
        self.btn_home.setText("")
        self.btn_home.setObjectName("btn_home")
        self.btn_add = QtWidgets.QPushButton(self.fr_left_menu_top)
        self.btn_add.setGeometry(QtCore.QRect(14, 18, 32, 32))
        self.btn_add.setMaximumSize(QtCore.QSize(35, 35))
        self.btn_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-image: url(:/add/add-white-32x32.svg);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QPushButton:hover{\n"
"    background-image: url(:/add/add-green-32x32.svg);\n"
"}")
        self.btn_add.setText("")
        self.btn_add.setObjectName("btn_add")
        self.btn_transactions = QtWidgets.QPushButton(self.fr_left_menu_top)
        self.btn_transactions.setGeometry(QtCore.QRect(14, 218, 32, 32))
        self.btn_transactions.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_transactions.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_transactions.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-image: url(:/money/graph-total-white-32x32.svg);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QPushButton:hover{\n"
"    background-image: url(:/money/graph-total-green-32x32.svg);\n"
"}")
        self.btn_transactions.setText("")
        self.btn_transactions.setObjectName("btn_transactions")
        self.btn_revenue = QtWidgets.QPushButton(self.fr_left_menu_top)
        self.btn_revenue.setGeometry(QtCore.QRect(14, 118, 32, 32))
        self.btn_revenue.setMinimumSize(QtCore.QSize(32, 32))
        self.btn_revenue.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_revenue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_revenue.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;    \n"
"    background-image: url(:/money/stat-up-white-32x32.svg);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QPushButton:hover{\n"
"    background-image: url(:/money/stat-up-green-32x32.svg);\n"
"}")
        self.btn_revenue.setText("")
        self.btn_revenue.setObjectName("btn_revenue")
        self.btn_expenses = QtWidgets.QPushButton(self.fr_left_menu_top)
        self.btn_expenses.setGeometry(QtCore.QRect(14, 168, 32, 32))
        self.btn_expenses.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_expenses.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_expenses.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;    \n"
"    background-image: url(:/money/stat-down-white-32x32.svg);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QPushButton:hover{\n"
"    background-image: url(:/money/stat-down-green-32x32.svg);\n"
"}")
        self.btn_expenses.setText("")
        self.btn_expenses.setObjectName("btn_expenses")
        self.verticalLayout_3.addWidget(self.fr_left_menu_top)
        self.fr_left_menu_button = QtWidgets.QFrame(self.fr_left_menu)
        self.fr_left_menu_button.setMinimumSize(QtCore.QSize(60, 0))
        self.fr_left_menu_button.setMaximumSize(QtCore.QSize(16777215, 120))
        self.fr_left_menu_button.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_left_menu_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_left_menu_button.setObjectName("fr_left_menu_button")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fr_left_menu_button)
        self.verticalLayout_4.setContentsMargins(14, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_user = QtWidgets.QPushButton(self.fr_left_menu_button)
        self.btn_user.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_user.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-image: url(:/user/user-white-32x32.svg);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QPushButton:hover{\n"
"    background-image: url(:/user/user-green-32x32.svg);\n"
"}")
        self.btn_user.setText("")
        self.btn_user.setObjectName("btn_user")
        self.verticalLayout_4.addWidget(self.btn_user)
        self.btn_settings = QtWidgets.QPushButton(self.fr_left_menu_button)
        self.btn_settings.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_settings.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-image: url(:/settings/settings-white-32x32.svg);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QPushButton:hover{\n"
"    background-image: url(:/settings/settings-green-32x32.svg);\n"
"}\n"
"")
        self.btn_settings.setText("")
        self.btn_settings.setObjectName("btn_settings")
        self.verticalLayout_4.addWidget(self.btn_settings)
        self.verticalLayout_3.addWidget(self.fr_left_menu_button)
        self.verticalLayout_2.addWidget(self.fr_left_menu)
        self.horizontalLayout_6.addWidget(self.fr_content_left_menu)
        self.fr_content_view = QtWidgets.QFrame(self.fr_content)
        self.fr_content_view.setStyleSheet("")
        self.fr_content_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_content_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content_view.setObjectName("fr_content_view")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fr_content_view)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.fr_content_view_top = QtWidgets.QFrame(self.fr_content_view)
        self.fr_content_view_top.setMinimumSize(QtCore.QSize(0, 32))
        self.fr_content_view_top.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fr_content_view_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_content_view_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content_view_top.setObjectName("fr_content_view_top")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.fr_content_view_top)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.fr_content_data_time = QtWidgets.QFrame(self.fr_content_view_top)
        self.fr_content_data_time.setStyleSheet("")
        self.fr_content_data_time.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_content_data_time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content_data_time.setObjectName("fr_content_data_time")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.fr_content_data_time)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lb_date_time = QtWidgets.QLabel(self.fr_content_data_time)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_date_time.setFont(font)
        self.lb_date_time.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_date_time.setText("")
        self.lb_date_time.setObjectName("lb_date_time")
        self.horizontalLayout_12.addWidget(self.lb_date_time)
        self.horizontalLayout_7.addWidget(self.fr_content_data_time)
        self.fr_content_search = QtWidgets.QFrame(self.fr_content_view_top)
        self.fr_content_search.setMaximumSize(QtCore.QSize(300, 16777215))
        self.fr_content_search.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_content_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content_search.setObjectName("fr_content_search")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.fr_content_search)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ld_search = QtWidgets.QLineEdit(self.fr_content_search)
        self.ld_search.setMinimumSize(QtCore.QSize(0, 32))
        self.ld_search.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.ld_search.setFont(font)
        self.ld_search.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_search.setObjectName("ld_search")
        self.horizontalLayout_8.addWidget(self.ld_search)
        self.btn_search = QtWidgets.QPushButton(self.fr_content_search)
        self.btn_search.setMinimumSize(QtCore.QSize(24, 24))
        self.btn_search.setMaximumSize(QtCore.QSize(24, 24))
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_search.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-image: url(:/search/search-white-32x32.svg);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QPushButton:hover{\n"
"    background-image: url(:/search/search-green-32x32.svg);\n"
"}")
        self.btn_search.setText("")
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_8.addWidget(self.btn_search)
        self.horizontalLayout_7.addWidget(self.fr_content_search)
        self.verticalLayout_5.addWidget(self.fr_content_view_top)
        self.tb_content_view = QtWidgets.QTabWidget(self.fr_content_view)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.tb_content_view.setFont(font)
        self.tb_content_view.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tb_content_view.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.tb_content_view.setObjectName("tb_content_view")
        self.tb_home = QtWidgets.QWidget()
        self.tb_home.setObjectName("tb_home")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tb_home)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.fr_content_home_graph = QtWidgets.QFrame(self.tb_home)
        self.fr_content_home_graph.setMinimumSize(QtCore.QSize(0, 300))
        self.fr_content_home_graph.setMaximumSize(QtCore.QSize(16777215, 500))
        self.fr_content_home_graph.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_content_home_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content_home_graph.setObjectName("fr_content_home_graph")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.fr_content_home_graph)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.graphWidget = PlotWidget(self.fr_content_home_graph)
        self.graphWidget.setMinimumSize(QtCore.QSize(300, 250))
        self.graphWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graphWidget.setObjectName("graphWidget")
        self.horizontalLayout_24.addWidget(self.graphWidget)
        self.verticalLayout_9.addWidget(self.fr_content_home_graph)
        self.fr_content_home_footer = QtWidgets.QFrame(self.tb_home)
        self.fr_content_home_footer.setMinimumSize(QtCore.QSize(654, 90))
        self.fr_content_home_footer.setMaximumSize(QtCore.QSize(16777215, 120))
        self.fr_content_home_footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_content_home_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content_home_footer.setObjectName("fr_content_home_footer")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.fr_content_home_footer)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.fr_content_home_filter = QtWidgets.QFrame(self.fr_content_home_footer)
        self.fr_content_home_filter.setMinimumSize(QtCore.QSize(654, 45))
        self.fr_content_home_filter.setMaximumSize(QtCore.QSize(16777215, 45))
        self.fr_content_home_filter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_content_home_filter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content_home_filter.setObjectName("fr_content_home_filter")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.fr_content_home_filter)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.fr_content_home_space = QtWidgets.QFrame(self.fr_content_home_filter)
        self.fr_content_home_space.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_content_home_space.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content_home_space.setObjectName("fr_content_home_space")
        self.horizontalLayout_25.addWidget(self.fr_content_home_space)
        self.fr_home_filter = QtWidgets.QFrame(self.fr_content_home_filter)
        self.fr_home_filter.setMinimumSize(QtCore.QSize(400, 45))
        self.fr_home_filter.setMaximumSize(QtCore.QSize(600, 16777215))
        self.fr_home_filter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_home_filter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_home_filter.setObjectName("fr_home_filter")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.fr_home_filter)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.lb_home_filter_month = QtWidgets.QLabel(self.fr_home_filter)
        self.lb_home_filter_month.setMinimumSize(QtCore.QSize(50, 0))
        self.lb_home_filter_month.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_home_filter_month.setFont(font)
        self.lb_home_filter_month.setObjectName("lb_home_filter_month")
        self.horizontalLayout_23.addWidget(self.lb_home_filter_month)
        self.cb_home_filter_min = QtWidgets.QComboBox(self.fr_home_filter)
        self.cb_home_filter_min.setMinimumSize(QtCore.QSize(0, 26))
        self.cb_home_filter_min.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cb_home_filter_min.setFont(font)
        self.cb_home_filter_min.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.cb_home_filter_min.setObjectName("cb_home_filter_min")
        self.horizontalLayout_23.addWidget(self.cb_home_filter_min)
        self.lb_home_filter_range = QtWidgets.QLabel(self.fr_home_filter)
        self.lb_home_filter_range.setMaximumSize(QtCore.QSize(7, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lb_home_filter_range.setFont(font)
        self.lb_home_filter_range.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_home_filter_range.setObjectName("lb_home_filter_range")
        self.horizontalLayout_23.addWidget(self.lb_home_filter_range)
        self.cb_home_filter_max = QtWidgets.QComboBox(self.fr_home_filter)
        self.cb_home_filter_max.setMinimumSize(QtCore.QSize(0, 26))
        self.cb_home_filter_max.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cb_home_filter_max.setFont(font)
        self.cb_home_filter_max.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.cb_home_filter_max.setObjectName("cb_home_filter_max")
        self.horizontalLayout_23.addWidget(self.cb_home_filter_max)
        self.lb_home_filter_year = QtWidgets.QLabel(self.fr_home_filter)
        self.lb_home_filter_year.setMinimumSize(QtCore.QSize(40, 0))
        self.lb_home_filter_year.setMaximumSize(QtCore.QSize(45, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_home_filter_year.setFont(font)
        self.lb_home_filter_year.setObjectName("lb_home_filter_year")
        self.horizontalLayout_23.addWidget(self.lb_home_filter_year)
        self.ld_home_filter_year = QtWidgets.QLineEdit(self.fr_home_filter)
        self.ld_home_filter_year.setMinimumSize(QtCore.QSize(0, 32))
        self.ld_home_filter_year.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.ld_home_filter_year.setFont(font)
        self.ld_home_filter_year.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_home_filter_year.setObjectName("ld_home_filter_year")
        self.horizontalLayout_23.addWidget(self.ld_home_filter_year)
        self.btn_home_filter = QtWidgets.QPushButton(self.fr_home_filter)
        self.btn_home_filter.setMinimumSize(QtCore.QSize(70, 32))
        self.btn_home_filter.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_home_filter.setFont(font)
        self.btn_home_filter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_home_filter.setStyleSheet("QPushButton{\n"
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
        self.btn_home_filter.setObjectName("btn_home_filter")
        self.horizontalLayout_23.addWidget(self.btn_home_filter)
        self.horizontalLayout_25.addWidget(self.fr_home_filter)
        self.verticalLayout_10.addWidget(self.fr_content_home_filter)
        self.fr_content_home_values = QtWidgets.QFrame(self.fr_content_home_footer)
        self.fr_content_home_values.setMinimumSize(QtCore.QSize(654, 45))
        self.fr_content_home_values.setMaximumSize(QtCore.QSize(16777215, 45))
        self.fr_content_home_values.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_content_home_values.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_content_home_values.setObjectName("fr_content_home_values")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.fr_content_home_values)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.fr_home_values = QtWidgets.QFrame(self.fr_content_home_values)
        self.fr_home_values.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_home_values.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_home_values.setObjectName("fr_home_values")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.fr_home_values)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.lb_home_revenue = ClickLabel(self.fr_home_values)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lb_home_revenue.setFont(font)
        self.lb_home_revenue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lb_home_revenue.setStyleSheet("QLabel{\n"
"    border-radius: 5px;\n"
"    margin-right: 5px;\n"
"    margin-left: 5px;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: rgb(50,50,50);\n"
"}\n"
"QLabel:pressed{\n"
"    background-color: rgb(35,35,35);\n"
"}")
        self.lb_home_revenue.setObjectName("lb_home_revenue")
        self.horizontalLayout_26.addWidget(self.lb_home_revenue)
        self.lb_home_expenses = ClickLabel(self.fr_home_values)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lb_home_expenses.setFont(font)
        self.lb_home_expenses.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lb_home_expenses.setStyleSheet("QLabel{\n"
"    border-radius: 5px;\n"
"    margin-right: 5px;\n"
"    margin-left: 5px;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: rgb(50,50,50);\n"
"}\n"
"QLabel:pressed{\n"
"    background-color: rgb(35,35,35);\n"
"}")
        self.lb_home_expenses.setObjectName("lb_home_expenses")
        self.horizontalLayout_26.addWidget(self.lb_home_expenses)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem)
        self.horizontalLayout_27.addWidget(self.fr_home_values)
        self.lb_home_total = ClickLabel(self.fr_content_home_values)
        self.lb_home_total.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lb_home_total.setFont(font)
        self.lb_home_total.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lb_home_total.setStyleSheet("QLabel{\n"
"    border-radius: 5px;\n"
"    margin-right: 5px;\n"
"    margin-left: 5px;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: rgb(50,50,50);\n"
"}\n"
"QLabel:pressed{\n"
"    background-color: rgb(35,35,35);\n"
"}")
        self.lb_home_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_home_total.setObjectName("lb_home_total")
        self.horizontalLayout_27.addWidget(self.lb_home_total)
        self.verticalLayout_10.addWidget(self.fr_content_home_values)
        self.verticalLayout_9.addWidget(self.fr_content_home_footer)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/home/casa.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tb_content_view.addTab(self.tb_home, icon1, "")
        self.tb_add = QtWidgets.QWidget()
        self.tb_add.setObjectName("tb_add")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tb_add)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.fr_add_content = QtWidgets.QFrame(self.tb_add)
        self.fr_add_content.setMinimumSize(QtCore.QSize(500, 396))
        self.fr_add_content.setMaximumSize(QtCore.QSize(654, 600))
        self.fr_add_content.setStyleSheet("")
        self.fr_add_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_add_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_add_content.setObjectName("fr_add_content")
        self.ld_add_title = QtWidgets.QLineEdit(self.fr_add_content)
        self.ld_add_title.setGeometry(QtCore.QRect(52, 50, 550, 40))
        self.ld_add_title.setMaximumSize(QtCore.QSize(550, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_add_title.setFont(font)
        self.ld_add_title.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_add_title.setMaxLength(40)
        self.ld_add_title.setObjectName("ld_add_title")
        self.ld_add_creditor = QtWidgets.QLineEdit(self.fr_add_content)
        self.ld_add_creditor.setGeometry(QtCore.QRect(52, 130, 550, 40))
        self.ld_add_creditor.setMaximumSize(QtCore.QSize(550, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_add_creditor.setFont(font)
        self.ld_add_creditor.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_add_creditor.setMaxLength(40)
        self.ld_add_creditor.setObjectName("ld_add_creditor")
        self.rb_add_revenues = QtWidgets.QRadioButton(self.fr_add_content)
        self.rb_add_revenues.setGeometry(QtCore.QRect(52, 210, 96, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.rb_add_revenues.setFont(font)
        self.rb_add_revenues.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rb_add_revenues.setStyleSheet("")
        self.rb_add_revenues.setObjectName("rb_add_revenues")
        self.rb_add_expenses = QtWidgets.QRadioButton(self.fr_add_content)
        self.rb_add_expenses.setGeometry(QtCore.QRect(158, 210, 96, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.rb_add_expenses.setFont(font)
        self.rb_add_expenses.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rb_add_expenses.setObjectName("rb_add_expenses")
        self.lb_add_question_rev_exp = QtWidgets.QLabel(self.fr_add_content)
        self.lb_add_question_rev_exp.setGeometry(QtCore.QRect(52, 180, 280, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_add_question_rev_exp.setFont(font)
        self.lb_add_question_rev_exp.setObjectName("lb_add_question_rev_exp")
        self.lb_add_question_title = QtWidgets.QLabel(self.fr_add_content)
        self.lb_add_question_title.setGeometry(QtCore.QRect(52, 20, 410, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_add_question_title.setFont(font)
        self.lb_add_question_title.setObjectName("lb_add_question_title")
        self.lb_add_question_creditor = QtWidgets.QLabel(self.fr_add_content)
        self.lb_add_question_creditor.setGeometry(QtCore.QRect(52, 100, 220, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_add_question_creditor.setFont(font)
        self.lb_add_question_creditor.setObjectName("lb_add_question_creditor")
        self.ld_add_value = QtWidgets.QLineEdit(self.fr_add_content)
        self.ld_add_value.setGeometry(QtCore.QRect(52, 270, 150, 40))
        self.ld_add_value.setMaximumSize(QtCore.QSize(550, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_add_value.setFont(font)
        self.ld_add_value.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_add_value.setMaxLength(40)
        self.ld_add_value.setObjectName("ld_add_value")
        self.lb_add_question_value = QtWidgets.QLabel(self.fr_add_content)
        self.lb_add_question_value.setGeometry(QtCore.QRect(52, 240, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_add_question_value.setFont(font)
        self.lb_add_question_value.setObjectName("lb_add_question_value")
        self.lb_add_question_date = QtWidgets.QLabel(self.fr_add_content)
        self.lb_add_question_date.setGeometry(QtCore.QRect(402, 180, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_add_question_date.setFont(font)
        self.lb_add_question_date.setObjectName("lb_add_question_date")
        self.de_add_date = QtWidgets.QDateEdit(self.fr_add_content)
        self.de_add_date.setGeometry(QtCore.QRect(402, 210, 110, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.de_add_date.setFont(font)
        self.de_add_date.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.de_add_date.setObjectName("de_add_date")
        self.btn_add_register = QtWidgets.QPushButton(self.fr_add_content)
        self.btn_add_register.setGeometry(QtCore.QRect(277, 330, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_add_register.setFont(font)
        self.btn_add_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_register.setStyleSheet("QPushButton{\n"
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
        self.btn_add_register.setObjectName("btn_add_register")
        self.horizontalLayout_11.addWidget(self.fr_add_content)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/add/mais.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tb_content_view.addTab(self.tb_add, icon2, "")
        self.tb_revenue = QtWidgets.QWidget()
        self.tb_revenue.setObjectName("tb_revenue")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tb_revenue)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.fr_revenue_list = QtWidgets.QFrame(self.tb_revenue)
        self.fr_revenue_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fr_revenue_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_revenue_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_revenue_list.setObjectName("fr_revenue_list")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.fr_revenue_list)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.tb_revenue_list = QtWidgets.QTableWidget(self.fr_revenue_list)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.tb_revenue_list.setFont(font)
        self.tb_revenue_list.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"border-radius: 5px;")
        self.tb_revenue_list.setObjectName("tb_revenue_list")
        self.tb_revenue_list.setColumnCount(0)
        self.tb_revenue_list.setRowCount(0)
        self.horizontalLayout_13.addWidget(self.tb_revenue_list)
        self.verticalLayout_6.addWidget(self.fr_revenue_list)
        self.fr_revenue_filter_content = QtWidgets.QFrame(self.tb_revenue)
        self.fr_revenue_filter_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_revenue_filter_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_revenue_filter_content.setObjectName("fr_revenue_filter_content")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.fr_revenue_filter_content)
        self.horizontalLayout_20.setContentsMargins(0, 9, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.fr_revenue_space = QtWidgets.QFrame(self.fr_revenue_filter_content)
        self.fr_revenue_space.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_revenue_space.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_revenue_space.setObjectName("fr_revenue_space")
        self.horizontalLayout_20.addWidget(self.fr_revenue_space)
        self.fr_revenue_filter = QtWidgets.QFrame(self.fr_revenue_filter_content)
        self.fr_revenue_filter.setMinimumSize(QtCore.QSize(600, 0))
        self.fr_revenue_filter.setMaximumSize(QtCore.QSize(700, 16777215))
        self.fr_revenue_filter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_revenue_filter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_revenue_filter.setObjectName("fr_revenue_filter")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.fr_revenue_filter)
        self.horizontalLayout_19.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.lb_revenue_months = QtWidgets.QLabel(self.fr_revenue_filter)
        self.lb_revenue_months.setMinimumSize(QtCore.QSize(50, 0))
        self.lb_revenue_months.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_revenue_months.setFont(font)
        self.lb_revenue_months.setObjectName("lb_revenue_months")
        self.horizontalLayout_19.addWidget(self.lb_revenue_months)
        self.cb_revenue_months_min = QtWidgets.QComboBox(self.fr_revenue_filter)
        self.cb_revenue_months_min.setMinimumSize(QtCore.QSize(0, 26))
        self.cb_revenue_months_min.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cb_revenue_months_min.setFont(font)
        self.cb_revenue_months_min.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.cb_revenue_months_min.setObjectName("cb_revenue_months_min")
        self.horizontalLayout_19.addWidget(self.cb_revenue_months_min)
        self.lb_revenue_filter_range = QtWidgets.QLabel(self.fr_revenue_filter)
        self.lb_revenue_filter_range.setMaximumSize(QtCore.QSize(7, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lb_revenue_filter_range.setFont(font)
        self.lb_revenue_filter_range.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_revenue_filter_range.setObjectName("lb_revenue_filter_range")
        self.horizontalLayout_19.addWidget(self.lb_revenue_filter_range)
        self.cb_revenue_months_max = QtWidgets.QComboBox(self.fr_revenue_filter)
        self.cb_revenue_months_max.setMinimumSize(QtCore.QSize(0, 26))
        self.cb_revenue_months_max.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cb_revenue_months_max.setFont(font)
        self.cb_revenue_months_max.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.cb_revenue_months_max.setObjectName("cb_revenue_months_max")
        self.horizontalLayout_19.addWidget(self.cb_revenue_months_max)
        self.lb_revenue_year = QtWidgets.QLabel(self.fr_revenue_filter)
        self.lb_revenue_year.setMinimumSize(QtCore.QSize(30, 0))
        self.lb_revenue_year.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_revenue_year.setFont(font)
        self.lb_revenue_year.setObjectName("lb_revenue_year")
        self.horizontalLayout_19.addWidget(self.lb_revenue_year)
        self.ld_revenue_year = QtWidgets.QLineEdit(self.fr_revenue_filter)
        self.ld_revenue_year.setMinimumSize(QtCore.QSize(0, 32))
        self.ld_revenue_year.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.ld_revenue_year.setFont(font)
        self.ld_revenue_year.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_revenue_year.setObjectName("ld_revenue_year")
        self.horizontalLayout_19.addWidget(self.ld_revenue_year)
        self.lb_revenues_values = QtWidgets.QLabel(self.fr_revenue_filter)
        self.lb_revenues_values.setMinimumSize(QtCore.QSize(45, 0))
        self.lb_revenues_values.setMaximumSize(QtCore.QSize(45, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_revenues_values.setFont(font)
        self.lb_revenues_values.setObjectName("lb_revenues_values")
        self.horizontalLayout_19.addWidget(self.lb_revenues_values)
        self.ld_revenue_min = QtWidgets.QLineEdit(self.fr_revenue_filter)
        self.ld_revenue_min.setMinimumSize(QtCore.QSize(0, 32))
        self.ld_revenue_min.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.ld_revenue_min.setFont(font)
        self.ld_revenue_min.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_revenue_min.setObjectName("ld_revenue_min")
        self.horizontalLayout_19.addWidget(self.ld_revenue_min)
        self.ld_revenue_max = QtWidgets.QLineEdit(self.fr_revenue_filter)
        self.ld_revenue_max.setMinimumSize(QtCore.QSize(0, 32))
        self.ld_revenue_max.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.ld_revenue_max.setFont(font)
        self.ld_revenue_max.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_revenue_max.setObjectName("ld_revenue_max")
        self.horizontalLayout_19.addWidget(self.ld_revenue_max)
        self.btn_revenue_filter = QtWidgets.QPushButton(self.fr_revenue_filter)
        self.btn_revenue_filter.setMinimumSize(QtCore.QSize(70, 32))
        self.btn_revenue_filter.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_revenue_filter.setFont(font)
        self.btn_revenue_filter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_revenue_filter.setStyleSheet("QPushButton{\n"
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
        self.btn_revenue_filter.setObjectName("btn_revenue_filter")
        self.horizontalLayout_19.addWidget(self.btn_revenue_filter)
        self.horizontalLayout_20.addWidget(self.fr_revenue_filter)
        self.verticalLayout_6.addWidget(self.fr_revenue_filter_content)
        self.fr_revenue_total = QtWidgets.QFrame(self.tb_revenue)
        self.fr_revenue_total.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_revenue_total.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_revenue_total.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_revenue_total.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_revenue_total.setObjectName("fr_revenue_total")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.fr_revenue_total)
        self.horizontalLayout_14.setContentsMargins(0, 9, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lb_revenue_total = QtWidgets.QLabel(self.fr_revenue_total)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lb_revenue_total.setFont(font)
        self.lb_revenue_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_revenue_total.setObjectName("lb_revenue_total")
        self.horizontalLayout_14.addWidget(self.lb_revenue_total)
        self.verticalLayout_6.addWidget(self.fr_revenue_total)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/money/dinheiro(copiar).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tb_content_view.addTab(self.tb_revenue, icon3, "")
        self.tb_expenses = QtWidgets.QWidget()
        self.tb_expenses.setObjectName("tb_expenses")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tb_expenses)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.fr_expenses_list = QtWidgets.QFrame(self.tb_expenses)
        self.fr_expenses_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fr_expenses_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_expenses_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_expenses_list.setObjectName("fr_expenses_list")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.fr_expenses_list)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tb_expenses_list = QtWidgets.QTableWidget(self.fr_expenses_list)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.tb_expenses_list.setFont(font)
        self.tb_expenses_list.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"border-radius: 5px;")
        self.tb_expenses_list.setObjectName("tb_expenses_list")
        self.tb_expenses_list.setColumnCount(0)
        self.tb_expenses_list.setRowCount(0)
        self.horizontalLayout_16.addWidget(self.tb_expenses_list)
        self.verticalLayout_7.addWidget(self.fr_expenses_list)
        self.fr_expenses_filter_content = QtWidgets.QFrame(self.tb_expenses)
        self.fr_expenses_filter_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_expenses_filter_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_expenses_filter_content.setObjectName("fr_expenses_filter_content")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.fr_expenses_filter_content)
        self.horizontalLayout_21.setContentsMargins(0, 9, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.fr_expenses_space = QtWidgets.QFrame(self.fr_expenses_filter_content)
        self.fr_expenses_space.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_expenses_space.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_expenses_space.setObjectName("fr_expenses_space")
        self.horizontalLayout_21.addWidget(self.fr_expenses_space)
        self.fr_expenses_filter = QtWidgets.QFrame(self.fr_expenses_filter_content)
        self.fr_expenses_filter.setMinimumSize(QtCore.QSize(600, 0))
        self.fr_expenses_filter.setMaximumSize(QtCore.QSize(700, 16777215))
        self.fr_expenses_filter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_expenses_filter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_expenses_filter.setObjectName("fr_expenses_filter")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.fr_expenses_filter)
        self.horizontalLayout_22.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.lb_expenses_months = QtWidgets.QLabel(self.fr_expenses_filter)
        self.lb_expenses_months.setMinimumSize(QtCore.QSize(50, 0))
        self.lb_expenses_months.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_expenses_months.setFont(font)
        self.lb_expenses_months.setObjectName("lb_expenses_months")
        self.horizontalLayout_22.addWidget(self.lb_expenses_months)
        self.cb_expenses_months_min = QtWidgets.QComboBox(self.fr_expenses_filter)
        self.cb_expenses_months_min.setMinimumSize(QtCore.QSize(0, 26))
        self.cb_expenses_months_min.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cb_expenses_months_min.setFont(font)
        self.cb_expenses_months_min.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.cb_expenses_months_min.setObjectName("cb_expenses_months_min")
        self.horizontalLayout_22.addWidget(self.cb_expenses_months_min)
        self.lb_expenses_filter_range = QtWidgets.QLabel(self.fr_expenses_filter)
        self.lb_expenses_filter_range.setMaximumSize(QtCore.QSize(7, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lb_expenses_filter_range.setFont(font)
        self.lb_expenses_filter_range.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_expenses_filter_range.setObjectName("lb_expenses_filter_range")
        self.horizontalLayout_22.addWidget(self.lb_expenses_filter_range)
        self.cb_expenses_months_max = QtWidgets.QComboBox(self.fr_expenses_filter)
        self.cb_expenses_months_max.setMinimumSize(QtCore.QSize(0, 26))
        self.cb_expenses_months_max.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cb_expenses_months_max.setFont(font)
        self.cb_expenses_months_max.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.cb_expenses_months_max.setObjectName("cb_expenses_months_max")
        self.horizontalLayout_22.addWidget(self.cb_expenses_months_max)
        self.lb_expenses_year = QtWidgets.QLabel(self.fr_expenses_filter)
        self.lb_expenses_year.setMinimumSize(QtCore.QSize(30, 0))
        self.lb_expenses_year.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_expenses_year.setFont(font)
        self.lb_expenses_year.setObjectName("lb_expenses_year")
        self.horizontalLayout_22.addWidget(self.lb_expenses_year)
        self.ld_expenses_year = QtWidgets.QLineEdit(self.fr_expenses_filter)
        self.ld_expenses_year.setMinimumSize(QtCore.QSize(0, 32))
        self.ld_expenses_year.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.ld_expenses_year.setFont(font)
        self.ld_expenses_year.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_expenses_year.setObjectName("ld_expenses_year")
        self.horizontalLayout_22.addWidget(self.ld_expenses_year)
        self.lb_expenses_values = QtWidgets.QLabel(self.fr_expenses_filter)
        self.lb_expenses_values.setMinimumSize(QtCore.QSize(45, 0))
        self.lb_expenses_values.setMaximumSize(QtCore.QSize(45, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_expenses_values.setFont(font)
        self.lb_expenses_values.setObjectName("lb_expenses_values")
        self.horizontalLayout_22.addWidget(self.lb_expenses_values)
        self.ld_expenses_min = QtWidgets.QLineEdit(self.fr_expenses_filter)
        self.ld_expenses_min.setMinimumSize(QtCore.QSize(0, 32))
        self.ld_expenses_min.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.ld_expenses_min.setFont(font)
        self.ld_expenses_min.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_expenses_min.setObjectName("ld_expenses_min")
        self.horizontalLayout_22.addWidget(self.ld_expenses_min)
        self.ld_expenses_max = QtWidgets.QLineEdit(self.fr_expenses_filter)
        self.ld_expenses_max.setMinimumSize(QtCore.QSize(0, 32))
        self.ld_expenses_max.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.ld_expenses_max.setFont(font)
        self.ld_expenses_max.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_expenses_max.setObjectName("ld_expenses_max")
        self.horizontalLayout_22.addWidget(self.ld_expenses_max)
        self.btn_expenses_filter = QtWidgets.QPushButton(self.fr_expenses_filter)
        self.btn_expenses_filter.setMinimumSize(QtCore.QSize(70, 32))
        self.btn_expenses_filter.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_expenses_filter.setFont(font)
        self.btn_expenses_filter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_expenses_filter.setStyleSheet("QPushButton{\n"
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
        self.btn_expenses_filter.setObjectName("btn_expenses_filter")
        self.horizontalLayout_22.addWidget(self.btn_expenses_filter)
        self.horizontalLayout_21.addWidget(self.fr_expenses_filter)
        self.verticalLayout_7.addWidget(self.fr_expenses_filter_content)
        self.fr_expenses_status = QtWidgets.QFrame(self.tb_expenses)
        self.fr_expenses_status.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_expenses_status.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_expenses_status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_expenses_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_expenses_status.setObjectName("fr_expenses_status")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.fr_expenses_status)
        self.horizontalLayout_15.setContentsMargins(0, 9, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lb_expenses_total = QtWidgets.QLabel(self.fr_expenses_status)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lb_expenses_total.setFont(font)
        self.lb_expenses_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_expenses_total.setObjectName("lb_expenses_total")
        self.horizontalLayout_15.addWidget(self.lb_expenses_total)
        self.verticalLayout_7.addWidget(self.fr_expenses_status)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/money/seta-para-baixo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tb_content_view.addTab(self.tb_expenses, icon4, "")
        self.tb_transactions = QtWidgets.QWidget()
        self.tb_transactions.setObjectName("tb_transactions")
        self.label_5 = QtWidgets.QLabel(self.tb_transactions)
        self.label_5.setGeometry(QtCore.QRect(100, 60, 81, 17))
        self.label_5.setObjectName("label_5")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/calendar/calendario.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tb_content_view.addTab(self.tb_transactions, icon5, "")
        self.tb_profile = QtWidgets.QWidget()
        self.tb_profile.setObjectName("tb_profile")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tb_profile)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.fr_profile_content = QtWidgets.QFrame(self.tb_profile)
        self.fr_profile_content.setMaximumSize(QtCore.QSize(350, 600))
        self.fr_profile_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_profile_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_profile_content.setObjectName("fr_profile_content")
        self.fr_profile_photo = QtWidgets.QFrame(self.fr_profile_content)
        self.fr_profile_photo.setGeometry(QtCore.QRect(111, 20, 128, 128))
        self.fr_profile_photo.setMaximumSize(QtCore.QSize(128, 128))
        self.fr_profile_photo.setStyleSheet("background-image: url(:/user/do-utilizador(copiar).png);\n"
"background-color: rgb(85, 255, 255);\n"
"border-radius: 64px;")
        self.fr_profile_photo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_profile_photo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_profile_photo.setObjectName("fr_profile_photo")
        self.lb_profile_name = QtWidgets.QLabel(self.fr_profile_content)
        self.lb_profile_name.setGeometry(QtCore.QRect(45, 160, 260, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lb_profile_name.setFont(font)
        self.lb_profile_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_profile_name.setObjectName("lb_profile_name")
        self.lb_profile_username = QtWidgets.QLabel(self.fr_profile_content)
        self.lb_profile_username.setGeometry(QtCore.QRect(80, 190, 190, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lb_profile_username.setFont(font)
        self.lb_profile_username.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_profile_username.setObjectName("lb_profile_username")
        self.lb_profile_password = QtWidgets.QLabel(self.fr_profile_content)
        self.lb_profile_password.setGeometry(QtCore.QRect(75, 250, 200, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.lb_profile_password.setFont(font)
        self.lb_profile_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_profile_password.setObjectName("lb_profile_password")
        self.lb_profile_email = QtWidgets.QLabel(self.fr_profile_content)
        self.lb_profile_email.setGeometry(QtCore.QRect(25, 280, 300, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.lb_profile_email.setFont(font)
        self.lb_profile_email.setStyleSheet("")
        self.lb_profile_email.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_profile_email.setObjectName("lb_profile_email")
        self.btn_profile_edit = QtWidgets.QPushButton(self.fr_profile_content)
        self.btn_profile_edit.setGeometry(QtCore.QRect(125, 320, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_profile_edit.setFont(font)
        self.btn_profile_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_profile_edit.setStyleSheet("QPushButton{\n"
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
        self.btn_profile_edit.setObjectName("btn_profile_edit")
        self.horizontalLayout_9.addWidget(self.fr_profile_content)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/user/do-utilizador.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tb_content_view.addTab(self.tb_profile, icon6, "")
        self.tb_settings = QtWidgets.QWidget()
        self.tb_settings.setObjectName("tb_settings")
        self.label_7 = QtWidgets.QLabel(self.tb_settings)
        self.label_7.setGeometry(QtCore.QRect(80, 80, 81, 17))
        self.label_7.setObjectName("label_7")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/settings/019-settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tb_content_view.addTab(self.tb_settings, icon7, "")
        self.tb_search = QtWidgets.QWidget()
        self.tb_search.setObjectName("tb_search")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tb_search)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.fr_search_list = QtWidgets.QFrame(self.tb_search)
        self.fr_search_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_search_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_search_list.setObjectName("fr_search_list")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.fr_search_list)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.tb_search_list = QtWidgets.QTableWidget(self.fr_search_list)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.tb_search_list.setFont(font)
        self.tb_search_list.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"border-radius: 5px;")
        self.tb_search_list.setObjectName("tb_search_list")
        self.tb_search_list.setColumnCount(0)
        self.tb_search_list.setRowCount(0)
        self.horizontalLayout_17.addWidget(self.tb_search_list)
        self.verticalLayout_8.addWidget(self.fr_search_list)
        self.fr_search_result = QtWidgets.QFrame(self.tb_search)
        self.fr_search_result.setMinimumSize(QtCore.QSize(0, 35))
        self.fr_search_result.setMaximumSize(QtCore.QSize(16777215, 35))
        self.fr_search_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_search_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_search_result.setObjectName("fr_search_result")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.fr_search_result)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.lb_search_result = QtWidgets.QLabel(self.fr_search_result)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_search_result.setFont(font)
        self.lb_search_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_search_result.setObjectName("lb_search_result")
        self.horizontalLayout_18.addWidget(self.lb_search_result)
        self.verticalLayout_8.addWidget(self.fr_search_result)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/search/procurar.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tb_content_view.addTab(self.tb_search, icon8, "")
        self.tb_edit = QtWidgets.QWidget()
        self.tb_edit.setObjectName("tb_edit")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tb_edit)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.fr_edit_content = QtWidgets.QFrame(self.tb_edit)
        self.fr_edit_content.setMaximumSize(QtCore.QSize(350, 600))
        self.fr_edit_content.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.fr_edit_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_edit_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_edit_content.setObjectName("fr_edit_content")
        self.ld_edit_name = QtWidgets.QLineEdit(self.fr_edit_content)
        self.ld_edit_name.setGeometry(QtCore.QRect(50, 146, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_edit_name.setFont(font)
        self.ld_edit_name.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_edit_name.setMaxLength(20)
        self.ld_edit_name.setObjectName("ld_edit_name")
        self.ld_edit_username = QtWidgets.QLineEdit(self.fr_edit_content)
        self.ld_edit_username.setGeometry(QtCore.QRect(50, 196, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_edit_username.setFont(font)
        self.ld_edit_username.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_edit_username.setMaxLength(20)
        self.ld_edit_username.setObjectName("ld_edit_username")
        self.ld_edit_password = QtWidgets.QLineEdit(self.fr_edit_content)
        self.ld_edit_password.setGeometry(QtCore.QRect(50, 246, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_edit_password.setFont(font)
        self.ld_edit_password.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_edit_password.setMaxLength(20)
        self.ld_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ld_edit_password.setObjectName("ld_edit_password")
        self.ld_edit_email = QtWidgets.QLineEdit(self.fr_edit_content)
        self.ld_edit_email.setGeometry(QtCore.QRect(50, 296, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ld_edit_email.setFont(font)
        self.ld_edit_email.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: rgb(47, 47, 47);\n"
"    color: rgb(200,200,200);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 122, 209);\n"
"    border: 2px solid rgb(172, 235, 226);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.ld_edit_email.setMaxLength(40)
        self.ld_edit_email.setObjectName("ld_edit_email")
        self.btn_edit_save = QtWidgets.QPushButton(self.fr_edit_content)
        self.btn_edit_save.setGeometry(QtCore.QRect(120, 356, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_edit_save.setFont(font)
        self.btn_edit_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_edit_save.setStyleSheet("QPushButton{\n"
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
        self.btn_edit_save.setObjectName("btn_edit_save")
        self.btn_edit_more = QtWidgets.QPushButton(self.fr_edit_content)
        self.btn_edit_more.setGeometry(QtCore.QRect(310, 98, 24, 24))
        self.btn_edit_more.setMinimumSize(QtCore.QSize(24, 24))
        self.btn_edit_more.setMaximumSize(QtCore.QSize(24, 24))
        self.btn_edit_more.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_edit_more.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-image: url(:/more/more.png);\n"
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
        self.btn_edit_more.setText("")
        self.btn_edit_more.setObjectName("btn_edit_more")
        self.lb_edit_photo = QtWidgets.QLabel(self.fr_edit_content)
        self.lb_edit_photo.setGeometry(QtCore.QRect(50, 94, 250, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_edit_photo.setFont(font)
        self.lb_edit_photo.setStyleSheet("padding: 5px;")
        self.lb_edit_photo.setObjectName("lb_edit_photo")
        self.fr_edit_photo = QtWidgets.QFrame(self.fr_edit_content)
        self.fr_edit_photo.setGeometry(QtCore.QRect(143, 20, 64, 64))
        self.fr_edit_photo.setMaximumSize(QtCore.QSize(64, 64))
        self.fr_edit_photo.setStyleSheet("background-image: url(:/user/do-utilizador_64.png);\n"
"background-color: rgb(85, 255, 255);\n"
"border-radius: 32px;")
        self.fr_edit_photo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_edit_photo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_edit_photo.setObjectName("fr_edit_photo")
        self.horizontalLayout_10.addWidget(self.fr_edit_content)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/pencil/lapis(copiar).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tb_content_view.addTab(self.tb_edit, icon9, "")
        self.verticalLayout_5.addWidget(self.tb_content_view)
        self.horizontalLayout_6.addWidget(self.fr_content_view)
        self.verticalLayout.addWidget(self.fr_content)
        self.fr_button = QtWidgets.QFrame(self.centralwidget)
        self.fr_button.setMaximumSize(QtCore.QSize(16777215, 35))
        self.fr_button.setStyleSheet("")
        self.fr_button.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_button.setObjectName("fr_button")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fr_button)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_credits = QtWidgets.QLabel(self.fr_button)
        self.lb_credits.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-right: 5px;")
        self.lb_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_credits.setObjectName("lb_credits")
        self.horizontalLayout.addWidget(self.lb_credits)
        self.verticalLayout.addWidget(self.fr_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tb_content_view.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_logo.setText(_translate("MainWindow", "My Finances"))
        self.lb_error_msg.setText(_translate("MainWindow", "Error"))
        self.ld_search.setPlaceholderText(_translate("MainWindow", "Search"))
        self.lb_home_filter_month.setText(_translate("MainWindow", "Months"))
        self.lb_home_filter_range.setText(_translate("MainWindow", "~"))
        self.lb_home_filter_year.setText(_translate("MainWindow", "Year"))
        self.ld_home_filter_year.setPlaceholderText(_translate("MainWindow", "2021"))
        self.btn_home_filter.setText(_translate("MainWindow", "Filter"))
        self.lb_home_revenue.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#c8c8c8;\">Revenues: </span><span style=\" color:#ff5580;\">$1000000.00</span></p></body></html>"))
        self.lb_home_expenses.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#c8c8c8;\">Expenses: </span><span style=\" color:#ff5580;\">$1000000.00</span></p></body></html>"))
        self.lb_home_total.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#c8c8c8;\">Total:</span><span style=\" color:#c8c8c8;\"/><span style=\" color:#ff5580;\">$ -1000000.00</span></p></body></html>"))
        self.tb_content_view.setTabText(self.tb_content_view.indexOf(self.tb_home), _translate("MainWindow", "Home"))
        self.ld_add_title.setPlaceholderText(_translate("MainWindow", "Ex: Electricity bill"))
        self.ld_add_creditor.setPlaceholderText(_translate("MainWindow", "Ex: Energy company"))
        self.rb_add_revenues.setText(_translate("MainWindow", "Revenues"))
        self.rb_add_expenses.setText(_translate("MainWindow", "Expenses"))
        self.lb_add_question_rev_exp.setText(_translate("MainWindow", "It\'s a new registry of a revenue or expense?"))
        self.lb_add_question_title.setText(_translate("MainWindow", "What is the title of the new registry? Be it revenue or expense."))
        self.lb_add_question_creditor.setText(_translate("MainWindow", "What is the name of the creditor?"))
        self.ld_add_value.setPlaceholderText(_translate("MainWindow", "Ex: 10000.00"))
        self.lb_add_question_value.setText(_translate("MainWindow", "What is the value of the new registry?"))
        self.lb_add_question_date.setText(_translate("MainWindow", "What is the registry due date?"))
        self.btn_add_register.setText(_translate("MainWindow", "Register"))
        self.tb_content_view.setTabText(self.tb_content_view.indexOf(self.tb_add), _translate("MainWindow", "Add"))
        self.lb_revenue_months.setText(_translate("MainWindow", "Months"))
        self.lb_revenue_filter_range.setText(_translate("MainWindow", "~"))
        self.lb_revenue_year.setText(_translate("MainWindow", "Year"))
        self.ld_revenue_year.setPlaceholderText(_translate("MainWindow", "2021"))
        self.lb_revenues_values.setText(_translate("MainWindow", "Values"))
        self.ld_revenue_min.setPlaceholderText(_translate("MainWindow", "Min"))
        self.ld_revenue_max.setPlaceholderText(_translate("MainWindow", "Max"))
        self.btn_revenue_filter.setText(_translate("MainWindow", "Filter"))
        self.lb_revenue_total.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#c8c8c8;\">Total: </span><span style=\" color:#ff5580;\">$1000.00</span></p></body></html>"))
        self.tb_content_view.setTabText(self.tb_content_view.indexOf(self.tb_revenue), _translate("MainWindow", "Revenue"))
        self.lb_expenses_months.setText(_translate("MainWindow", "Months"))
        self.lb_expenses_filter_range.setText(_translate("MainWindow", "~"))
        self.lb_expenses_year.setText(_translate("MainWindow", "Year"))
        self.ld_expenses_year.setPlaceholderText(_translate("MainWindow", "2021"))
        self.lb_expenses_values.setText(_translate("MainWindow", "Values"))
        self.ld_expenses_min.setPlaceholderText(_translate("MainWindow", "Min"))
        self.ld_expenses_max.setPlaceholderText(_translate("MainWindow", "Max"))
        self.btn_expenses_filter.setText(_translate("MainWindow", "Filter"))
        self.lb_expenses_total.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#c8c8c8;\">Total: </span><span style=\" color:#ff5580;\">$1000.00</span></p></body></html>"))
        self.tb_content_view.setTabText(self.tb_content_view.indexOf(self.tb_expenses), _translate("MainWindow", "Expenses"))
        self.label_5.setText(_translate("MainWindow", "Transactions"))
        self.tb_content_view.setTabText(self.tb_content_view.indexOf(self.tb_transactions), _translate("MainWindow", "Transactions"))
        self.lb_profile_name.setText(_translate("MainWindow", "Naaaameeee Naaaameeee "))
        self.lb_profile_username.setText(_translate("MainWindow", "UsernameeeUsernameee"))
        self.lb_profile_password.setText(_translate("MainWindow", "Password: ********************"))
        self.lb_profile_email.setText(_translate("MainWindow", "Email: email@gmail.comemail@gmail.commmm"))
        self.btn_profile_edit.setText(_translate("MainWindow", "Edit"))
        self.tb_content_view.setTabText(self.tb_content_view.indexOf(self.tb_profile), _translate("MainWindow", "Profile"))
        self.label_7.setText(_translate("MainWindow", "SETTINGS"))
        self.tb_content_view.setTabText(self.tb_content_view.indexOf(self.tb_settings), _translate("MainWindow", "Settings"))
        self.lb_search_result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#c8c8c8;\">10 search results have been found!</span></p></body></html>"))
        self.tb_content_view.setTabText(self.tb_content_view.indexOf(self.tb_search), _translate("MainWindow", "Search"))
        self.ld_edit_name.setPlaceholderText(_translate("MainWindow", "Name"))
        self.ld_edit_username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.ld_edit_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.ld_edit_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.btn_edit_save.setText(_translate("MainWindow", "Save"))
        self.lb_edit_photo.setText(_translate("MainWindow", ":/user/do-utilizador.png"))
        self.tb_content_view.setTabText(self.tb_content_view.indexOf(self.tb_edit), _translate("MainWindow", "Edit"))
        self.lb_credits.setText(_translate("MainWindow", "<html><head/><body><p>Alfa v1.0.0, developer by <span style=\" font-weight:600;\">Bruno Melo.</span></p></body></html>"))
from clicklabel import ClickLabel
from pyqtgraph import PlotWidget
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
