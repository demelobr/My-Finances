from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QAbstractItemView
from login import Ui_MainWindow
from library import *
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

id_global = ""
username_global = ""
name_global = ""
email_global = ""
password_global = ""
email_regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
Default = True

'''
	Classes
'''

class MainWindow(QtWidgets.QMainWindow, main.Ui_MainWindow):
    
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    def plot(self, values, time, title, x, y, legend, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.setBackground((31,35,38))
        self.graphWidget.setTitle(f"<span style=\"color: rgb(255,255,255);font-size:18px;font-weight:600;\">{title}</span>")
        self.graphWidget.setLabel("left", f"<span style=\"color:rgb(255,255,255);font-size:13px;font-weight:600;\">{x} ($)</span>")
        self.graphWidget.setLabel("bottom", f"<span style=\"color: rgb(255,255,255);font-size:13px;font-weight:600;\">{y} (months)</span>")
        self.graphWidget.addLegend()
        self.graphWidget.showGrid(x=True, y=True)
        data_line = self.graphWidget.plot(values, time, name =legend, pen=pen)
        return data_line

class RegisterWindow(QtWidgets.QMainWindow, register.Ui_MainWindow):
    
    def __init__(self, parent = None):
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)

class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        register = RegisterWindow(self)
        main = MainWindow(self)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/home/casa.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)

        def Show_register_window():
        	register.btn_register.clicked.connect(lambda: Create_account(register))
        	register.btn_close.clicked.connect(lambda: register.fr_error_msg.hide())
        	register.fr_error_msg.hide()
        	register.show()
        
        def Show_main_window():
            global Default
            #SET TITLE WINDOW
            _translate = QtCore.QCoreApplication.translate
            main.setWindowTitle(_translate("MainWindow", f"My Finances - {name_global}"))
            #SET DATA AND TIME
            timer = QTimer(self)
            timer.timeout.connect(lambda: Update_time(self, main))
            timer.start(1000)
            current_year = int(datetime.date.today().strftime("%Y"))
            #SET ICONS'S TABS
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/home/casa.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/add/mais.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap(":/money/dinheiro(copiar).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap(":/money/seta-para-baixo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap(":/calendar/calendario.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap(":/user/do-utilizador.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap(":/settings/019-settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap(":/search/procurar.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap(":/pencil/lapis(copiar).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            #REMOVE TABS
            main.tb_content_view.removeTab(8)
            main.tb_content_view.removeTab(7)
            main.tb_content_view.removeTab(6)
            main.tb_content_view.removeTab(5)
            main.tb_content_view.removeTab(4)
            main.tb_content_view.removeTab(3)
            main.tb_content_view.removeTab(2)
            main.tb_content_view.removeTab(1)
            #ADD/REMOVE TABS AND SET BUTTONS IN ALL TABS
            main.btn_add.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
            main.btn_add.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_add, icon2,"Add"))
            main.btn_home.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
            main.btn_home.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_home, icon1,"Home"))
            
            '''Linha faltante'''
            main.btn_home.clicked.connect(lambda: Home_graph(main, username_global, Default))
            
            main.btn_revenue.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
            main.btn_revenue.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_revenue, icon3,"Revenue"))
            main.btn_revenue.clicked.connect(lambda: Revenue_list(main, username_global))
            
            main.btn_expenses.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
            main.btn_expenses.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_expenses, icon4,"Expenses"))
            main.btn_expenses.clicked.connect(lambda: Expenses_list(main, username_global))
            
            main.btn_calendar.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
            main.btn_calendar.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_calendar, icon5,"Calendar"))
            main.btn_user.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
            main.btn_user.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_profile, icon6,f"{name_global}"))
            main.btn_settings.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
            main.btn_settings.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_settings, icon7,"Settings"))
            main.btn_search.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
            main.btn_search.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_search, icon8,"Search"))
            main.btn_search.clicked.connect(lambda: Search_list(main, username_global))
            
            main.btn_profile_edit.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
            main.btn_profile_edit.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_edit, icon9,"Edit"))
            
            '''Linhas faltantes'''
            main.btn_edit_save.clicked.connect(lambda: Edit_account(main, icon6))
            main.btn_add_register.clicked.connect(lambda: New_register(main, username_global))
            
            #SET LAYOUT ADD
            main.rb_add_revenues.setChecked(True)
            today = QtCore.QDate.currentDate()
            main.de_add_date.setDate(today)
            #SET LAYOUT HOME
            main.cb_home_filter_min.addItems(["Select month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            main.cb_home_filter_max.addItems(["Select month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            main.ld_home_filter_year.setPlaceholderText(_translate("MainWindow", f"{current_year}"))
            
            month_min = main.cb_home_filter_min.currentText()
            month_max = main.cb_home_filter_max.currentText()
            year = main.ld_home_filter_year.text()
            
            if month_min == "Select month" and month_max == "Select month" and year == "" and Default == True:
                data_revenue = Search_filter(username_global, "REVENUE", month_min, month_max, year, "", "")
                data_expenses = Search_filter(username_global, "EXPENSES", month_min, month_max, year, "", "")
        
                data_revenue, total_revenue = Data_graph(data_revenue)
                data_expenses, total_expenses = Data_graph(data_expenses)
                total = total_revenue - total_expenses
                
                main.graphWidget.clear()
                main.plot([1,2,3,4,5,6,7,8,9,10,11,12], data_revenue, f"Financial statement for the period January ~ December {current_year}", "Values", "Time", "Revenue", [85,255,127])
                main.plot([1,2,3,4,5,6,7,8,9,10,11,12], data_expenses, f"Financial statement for the period January ~ December {current_year}", "Values", "Time", "Expenses", [255,85,128])

                main.lb_home_revenue.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#c8c8c8;\">Revenue: </span><span style=\" color:#55ff7f;\">${total_revenue:.2f}</span></p></body></html>"))
                main.lb_home_expenses.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#c8c8c8;\">Expenses: </span><span style=\" color:#ff5580;\">${total_expenses:.2f}</span></p></body></html>"))
                if total > 0:
                    color = "#55ff7f"
                elif total == 0:
                    color = "#c8c8c8"
                else:
                    color = "#ff5580"
                main.lb_home_total.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#c8c8c8;\">Total: </span><span style=\" color:{color};\">${total:.2f}</span></p></body></html>"))
                Default = False
            
            main.lb_home_revenue.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
            main.lb_home_revenue.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_revenue, icon3,"Revenue"))
            main.lb_home_revenue.clicked.connect(lambda: Revenue_list(main, username_global, month_min, month_max, year))

            main.lb_home_expenses.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
            main.lb_home_expenses.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_expenses, icon4,"Expenses"))
            main.lb_home_expenses.clicked.connect(lambda: Expenses_list(main, username_global, month_min, month_max, year))   
            main.lb_home_total.clicked.connect(lambda: print("Clicando Total"))
            main.btn_home_filter.clicked.connect(lambda: Home_graph(main, username_global, Default))
            #SET LAYOUT REVENUE
            main.cb_revenue_months_min.addItems(["Select month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            main.cb_revenue_months_max.addItems(["Select month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            main.ld_revenue_year.setPlaceholderText(_translate("MainWindow", f"{current_year}"))
            #SET LAYOUT EXPENSES
            main.cb_expenses_months_min.addItems(["Select month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            main.cb_expenses_months_max.addItems(["Select month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            main.ld_expenses_year.setPlaceholderText(_translate("MainWindow", f"{current_year}"))
            #SET LAYOUT PROFILE
            main.lb_profile_name.setText(f"{name_global}")
            main.lb_profile_username.setText(f"{username_global}")
            main.lb_profile_email.setText(f"Email: {email_global}")
            i = len(password_global)
            main.lb_profile_password.setText("Password: " + "*"*i)
            #SET LAYOUT EDIT
            main.ld_edit_name.setPlaceholderText(_translate("MainWindow", f"{name_global}"))
            main.ld_edit_username.setPlaceholderText(_translate("MainWindow", f"{username_global}"))
            main.ld_edit_password.setPlaceholderText(_translate("MainWindow", "*"*i))
            main.ld_edit_email.setPlaceholderText(_translate("MainWindow", f"{email_global}"))
            #SET MSG WELCOME
            main.fr_error_msg.setStyleSheet("background-color: rgb(85, 255, 127); border-radius: 5px;")
            main.lb_error_msg.setText(f"Welcome {username_global}!")
            main.fr_error_msg.show()
            main.show()
            main.btn_error_msg.clicked.connect( lambda: main.fr_error_msg.hide())
            QtCore.QTimer.singleShot(5000, lambda: main.fr_error_msg.hide())

        def Verify_login():
            username = login.ld_username.text()
            password = login.ld_password.text()
            global id_global
            global username_global
            global name_global 
            global password_global
            global email_global

            if username == "" and password == "":
                login.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
                login.fr_error_msg.show()
                login.lb_error_msg.setText("Enter Username and Password fields!")
            elif username == "":
                login.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
                login.fr_error_msg.show()
                login.lb_error_msg.setText("Enter Username field!")
            elif password == "":
                login.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
                login.fr_error_msg.show()
                login.lb_error_msg.setText("Enter Password field!")
            else:
                file_name = r"db_control.db"
                file_object = Path(file_name)

                if not file_object.is_file():
                    conn = sqlite3.connect('db_control.db')
                    cursor = conn.cursor()
                    cursor.execute("""CREATE TABLE tb_users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name VARCHAR(20), username VARCHAR(20), password VARCHAR(20), email VARCHAR(40))""")
                    cursor.execute("""CREATE TABLE tb_registry (rg_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, rg_proprietary VARCHAR(20), rg_type VARCHAR(8), rg_title VARCHAR(40), rg_creditor VARCHAR(40), rg_date VARCHAR(10), rg_date_day VARCHAR(2), rg_date_month VARCHAR(2), rg_date_year VARCHAR(4), rg_value VARCHAR)""")
                    conn.close()
                try:
                    conn = sqlite3.connect('db_control.db')
                    cursor = conn.cursor()

                    cursor.execute(""" SELECT * FROM tb_users WHERE username = ? AND password = ?""", (username, password))
                    data = cursor.fetchall()
                    conn.close()
                    if data == []:
                        j = len(password)
                        print('============================================================')
                        print(f'Username: {username} Password: '+ '*'*j +' not found!')
                        print('============================================================')
                        login.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
                        login.fr_error_msg.show()
                        login.lb_error_msg.setText("Username or password is wrong!")
                    else:
                        login.fr_error_msg.setStyleSheet("background-color: rgb(85, 255, 127); border-radius: 5px;")
                        login.fr_error_msg.show()
                        login.lb_error_msg.setText("Successfully login! Loadin your account...")
                        QtCore.QTimer.singleShot(1500, lambda: Show_main_window())
                        QtCore.QTimer.singleShot(1500, lambda: login.hide())
                        for i in range(len(data)):
                            print('============================================================')
                            print(f'id: {data[i][0]}')
                            print(f'name: {data[i][1]}')
                            print(f'username: {data[i][2]}')
                            j = len(data[i][3])
                            print(f'password: ' + '*'*j)
                            print(f'email: {data[i][4]}')
                            print('============================================================')
                        id_global = data[0][0]
                        name_global = data[0][1]
                        username_global = data[0][2]
                        password_global = data[0][3]
                        email_global = data[0][4]
                except:
                    login.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
                    login.fr_error_msg.show()
                    login.lb_error_msg.setText("Could not open the database!")

        self.btn_login.clicked.connect(Verify_login)
        self.btn_click_here.clicked.connect(Show_register_window)

'''
	Functions
'''

def month_number(month: str):
    """
        FUNCTIONALITY: function that returns the number corresponding to the given month.
        :param  - month: parameter with month name.
        :return: returns the month number.
    """   
    dict = {"January" : 1, "February" : 2, "March" : 3,
            "April" : 4, "May" : 5, "June" : 6,
            "July" : 7, "August" : 8, "September" : 9,
            "October" : 10, "November" : 11, "December" : 12,
            "Select month" : -1}
    
    return dict[f'{month}']

def Edit_account(main, icon):
    conn = sqlite3.connect('db_control.db')
    cursor = conn.cursor()

    _translate = QtCore.QCoreApplication.translate

    global id_global
    global username_global
    global name_global 
    global password_global
    global email_global
    global email_regex

    name = main.ld_edit_name.text()
    username = main.ld_edit_username.text()
    password = main.ld_edit_password.text()
    email = main.ld_edit_email.text()

    cursor.execute(""" SELECT * FROM tb_users WHERE username = ?""",(username,))
    data = cursor.fetchall()

    if name == "" and username == "" and password == "" and email == "":
        main.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
        main.fr_error_msg.show()
        main.lb_error_msg.setText("No editing was done!")
        return
    if data != []:
        print(f"The {username_global} user tried edit your register with an existing username {username}")
        main.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
        main.fr_error_msg.show()
        main.lb_error_msg.setText(f"The username {username} exist!")
    else:
        if len(password) < 8 and password != "":
            print(f"The {username_global} user tried edit your password with an smaller password!")
            main.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
            main.fr_error_msg.show()
            main.lb_error_msg.setText("The password needs at least 8 digits!")
        elif password == password_global:
            main.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
            main.fr_error_msg.show()
            main.lb_error_msg.setText("The new password is the same as the old one!")
        elif email != "" and not re.search(email_regex, email):
            main.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
            main.fr_error_msg.show()
            main.lb_error_msg.setText("The email is not valid!")
        else:
            db = []
            if name == "" or username == "" or email == "" or password == "":
                if name != "":
                    db.append(name)
                else:
                    db.append(name_global)
                if username != "":
                    db.append(username)
                else:
                    db.append(username_global)
                if password != "":
                    db.append(password)
                else:
                    db.append(password_global)
                if email != "":
                    db.append(email)
                else:
                    db.append(email_global)

                #db.append(id_global)
                
                cursor.execute(""" UPDATE tb_users SET name = ?, username = ?, password = ?, email = ? WHERE id = ?""", (db[0], db[1], db[2], db[3], id_global,))
                conn.commit()
                conn.close()
                main.fr_error_msg.setStyleSheet("background-color: rgb(85, 255, 127); border-radius: 5px;")
                main.lb_error_msg.setText(f"Successfully edit!")
                main.fr_error_msg.show()
                QtCore.QTimer.singleShot(5000, lambda: main.fr_error_msg.hide())
                name_global = db[0]
                username_global = db[1]
                password_global = db[2]
                email_global = db[3]
                i = len(password_global)
                main.lb_profile_name.setText(f"{name_global}")
                main.lb_profile_username.setText(f"{username_global}")
                main.lb_profile_email.setText(f"Email: {email_global}")
                main.lb_profile_password.setText("Password: " + "*"*i)
                main.ld_edit_name.setPlaceholderText(_translate("MainWindow", f"{name_global}"))
                main.ld_edit_username.setPlaceholderText(_translate("MainWindow", f"{username_global}"))
                main.ld_edit_password.setPlaceholderText(_translate("MainWindow", "*"*i))
                main.ld_edit_email.setPlaceholderText(_translate("MainWindow", f"{email_global}"))
                main.tb_content_view.removeTab(main.tb_content_view.currentIndex())
                main.tb_content_view.addTab(main.tb_profile, icon,f"{name_global}")
            else:
                db.append(name)
                db.append(username)
                db.append(password)
                db.append(email)
                cursor.execute(""" UPDATE tb_users SET name = ?, username = ?, password = ?, email = ? WHERE id = ?""", (db[0], db[1], db[2], db[3], id_global,))
                conn.commit()
                conn.close()
                main.fr_error_msg.setStyleSheet("background-color: rgb(85, 255, 127); border-radius: 5px;")
                main.lb_error_msg.setText(f"Successfully edit!")
                main.fr_error_msg.show()
                QtCore.QTimer.singleShot(5000, lambda: main.fr_error_msg.hide())
                name_global = db[0]
                username_global = db[1]
                password_global = db[2]
                email_global = db[3]
                i = len(password_global)
                main.lb_profile_name.setText(f"{name_global}")
                main.lb_profile_username.setText(f"{username_global}")
                main.lb_profile_email.setText(f"Email: {email_global}")
                main.lb_profile_password.setText("Password: " + "*"*i)
                main.ld_edit_name.setPlaceholderText(_translate("MainWindow", f"{name_global}"))
                main.ld_edit_username.setPlaceholderText(_translate("MainWindow", f"{username_global}"))
                main.ld_edit_password.setPlaceholderText(_translate("MainWindow", "*"*i))
                main.ld_edit_email.setPlaceholderText(_translate("MainWindow", f"{email_global}"))
                main.tb_content_view.removeTab(main.tb_content_view.currentIndex())
                main.tb_content_view.addTab(main.tb_profile, icon,f"{name_global}")
    main.ld_edit_name.clear()
    main.ld_edit_username.clear()
    main.ld_edit_password.clear()
    main.ld_edit_email.clear()

def Create_account(register):
    conn = sqlite3.connect('db_control.db')
    cursor = conn.cursor()

    global email_regex

    name = register.ld_name.text()
    username = register.ld_username.text()
    password = register.ld_password.text()
    confirm_password = register.ld_confirm_password.text()
    email = register.ld_email.text()

    db = []
    db.append(name)
    db.append(username)
    db.append(password)
    db.append(email)

    if name == "" or username == "" or password == "" or confirm_password == "" or email == "":
	    register.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
	    register.fr_error_msg.show()
	    register.lb_error_msg.setText(f"All fields are required!")
    else:
        if len(password) < 8:
                register.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
                register.fr_error_msg.show()
                register.lb_error_msg.setText("The password needs at least 8 digits!")
        else:
            if password != confirm_password:
                register.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
                register.fr_error_msg.show()
                register.lb_error_msg.setText("Password and confirm password are different!")
            else:
                if re.search(email_regex, email):
                    cursor.execute(""" SELECT * FROM tb_users WHERE username = ?""",(username,))
                    data = cursor.fetchall()
                    conn.close()

                    if data != []:
                        print(f"The new user tried to register with an existing username {username}")
                        register.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
                        register.fr_error_msg.show()
                        register.lb_error_msg.setText(f"The username {username} exist!")
                    else:
                        conn = sqlite3.connect('db_control.db')
                        cursor = conn.cursor()
                        cursor.execute(""" INSERT INTO tb_users (name, username, password, email) VALUES (?,?,?,?)""", db)
                        conn.commit()
                        conn.close()
                        print(f"The new user {name} was registered!")
                        register.fr_error_msg.setStyleSheet("background-color: rgb(85, 255, 127); border-radius: 5px;")
                        register.fr_error_msg.show()
                        register.lb_error_msg.setText("Account successfully created!")
                else:
                    register.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
                    register.fr_error_msg.show()
                    register.lb_error_msg.setText("The email is not valid!")

'''
	Application
'''

if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)    
    login = LoginWindow()
    login.btn_close.clicked.connect(lambda: login.fr_error_msg.hide())
    login.fr_error_msg.hide()
    login.show()
    sys.exit(app.exec_())