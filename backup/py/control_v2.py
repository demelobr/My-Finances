from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QAbstractItemView
from click import confirm
from login import Ui_MainWindow
from library_v2 import *
from pathlib import Path
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import re
import time
import datetime
import locale
import sqlite3
import resources_rc
import register
import main

"""
    Classes:
        Class MainWindow: The main window class
        Class RegisterWindow: The register window class
        Class LoginWindow: The login window class
"""

class MainWindow(QtWidgets.QMainWindow, main.Ui_MainWindow):

    '''
        > "main" class initialization function
    '''
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

class RegisterWindow(QtWidgets.QMainWindow, register.Ui_MainWindow):
    
    '''
        > "register" class initialization function
    '''    
    def __init__(self, parent = None):
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)

        '''
            >> "register" window visual settings
        '''
        self.fr_error_msg.hide()
        
        '''
            >> register window button click events
        '''
        self.btn_close.clicked.connect(lambda: self.fr_error_msg.hide())
        self.btn_register.clicked.connect(lambda: create_account(self))

class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    '''
        > "login" class initialization function
    '''
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        '''
            >> Create database if it doesn't exist
        '''
        file_name = r"db_control.db"
        file_object = Path(file_name)

        if(not file_object.is_file()):
            create_data_base(self)

        '''
            >> "login" window visual settings
        '''
        self.fr_error_msg.hide()

        '''
            >> "login" window button click events
        '''
        self.btn_close.clicked.connect(lambda: self.fr_error_msg.hide())
        self.btn_click_here.clicked.connect(lambda: self.show_register_window())
        self.btn_login.clicked.connect(lambda: verify_login(self))

    '''
        >> "login" class methods
    '''
    
    def show_register_window(self):
        register_obj.show()  
    
    def show_main_window(self, username):
        data_user = get_data_user(username)
        setting_main_window(main_obj, data_user)
        main_obj.show()    


'''
    App
'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_obj = LoginWindow()
    register_obj = RegisterWindow()
    main_obj = MainWindow()
    login_obj.show()
    sys.exit(app.exec_())