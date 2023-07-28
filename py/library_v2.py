from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QAbstractItemView
from login import Ui_MainWindow
from pathlib import Path
from control_v2 import *
import sys
import re
import time
import datetime
import locale
import sqlite3
import resources_rc
import register
import main

'''
    Utility functions
'''
def is_number(number):
    """
        FUNCTIONALITY: function that tests whether the received data is number or not.
        :param  - number: parameter with the data received.
        :return - flag: Returns true if it is a number and false if it is not.
    """   
    flag = True

    if("," in number):
        number = number.replace(',','.')
    
    try:
        float(number)
    except:
        flag = False
    
    return flag
    
def list_to_dict(data):
    #BM OBS: Depois preciso indicar que a tipagem
    #        de "data" é "list".
    """
        FUNCTIONALITY: function that converts a list of data into a dictionary.
        :param  - data: parameter with the data in the form of a list.
        :return - dict: returns a dictionary with the data passed.
    """
    dict = {"id": None, "name": None, "username": None, "password": None, "email": None}

    if (len(data) == 0):
        dict = {}
    else:
        dict["id"] = data[0][0]
        dict["name"] = data[0][1]
        dict["username"] = data[0][2]
        dict["password"] = data[0][3]
        dict["email"] = data[0][4]

    return dict

def format_data_for_graph(data):
    #BM OBS: Depois preciso indicar a tipagem
    #      de "data" é "list".
    """
        FUNCTIONALITY: function that converts a list of data into a dictionary.
        :param  - data: parameter with the data in the form of a list.
        :return - values_graph: list with all values for each month.
                - value_total: total sum of months.
    """
    values_graph = [0,0,0,0,0,0,0,0,0,0,0,0]
    value_total = 0

    for fields in data:
        for month in range(0,12):
            if(fields[7] - 1 == month):
                values_graph[month] += fields[9]
    
    for values in values_graph:
        value_total += values
    
    return values_graph, value_total


'''
    Database functions
'''
def create_data_base(self):
    """
        FUNCTIONALITY: function that creates the application database.
        :param - self: window context where the function is being called.
        :return: nothing.
    """
    try:
        conn = sqlite3.connect('db_control.db')
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE tb_users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name VARCHAR(20),
                       username VARCHAR(20), password VARCHAR(20), email VARCHAR(40))""")
        cursor.execute("""CREATE TABLE tb_registry (rg_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, rg_proprietary VARCHAR(20),
                       rg_type VARCHAR(8), rg_title VARCHAR(40), rg_creditor VARCHAR(40), rg_date VARCHAR(10), rg_date_day INTEGER(2),
                       rg_date_month INTEGER(2), rg_date_year INTEGER(4), rg_value DECIMAL)""")
        conn.close()
        print("Data base created!")
    except:
        self.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
        self.fr_error_msg.show()
        self.lb_error_msg.setText("Could not open the database!")

def search_user(username: str, password: str = None):
    """
        FUNCTIONALITY: function that searches by user in the database.
        :param  - username: parameter with the username passed by the user.
                - password: parameter with the password passed by the user.
        :return - flag: true if the user exists in the database and false if not.
    """    
    flag = False

    conn = sqlite3.connect("db_control.db")
    cursor = conn.cursor()

    cursor.execute(""" SELECT * FROM tb_users WHERE username = ? AND password = ?""", (username, password))
    data = cursor.fetchall()
    conn.close()

    if(len(data) > 0):
        flag = True
    
    return flag

def get_data_user(username: str):
    """
        FUNCTIONALITY: function that get all data by user in the database.
        :param  - username: parameter with the username passed by the user.
        :return - data: a dictionary, empty if there are no records or with user data.
    """    
    conn = sqlite3.connect("db_control.db")
    cursor = conn.cursor()

    cursor.execute(""" SELECT * FROM tb_users WHERE username = ?""", (username,))
    data = cursor.fetchall()
    data = list_to_dict(data)
    conn.close()

    return data

def get_data(username: str, register_type: str, month_min: int, month_max: int, year: int,
            value_min: float = -1.0, value_max: float = -1.0):
    """
        FUNCTIONALITY: function that returns a list with all records of a user according to the applied filter.
        :param  - username: parameter with the username passed by the user.
                - register_type: parameter that indicates the type of record.
                - month_min: integer parameter that indicates the minimum month considered in the search.
                - month-max: integer parameter that indicates the maximum month considered in the search.
                - year: integer parameter that indicates the year considered in the survey.
                - value_min: float parameter that indicates the minimum value considered in the search
                - value_max: float parameter that indicates the maximum value considered in the search
        :return - data: list of all searched data.
    """ 

    data_list = [register_type, username,year]
    cmd_str = " SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_year = ? "

    if(month_min != 0):
        data_list.append(month_min)
        cmd_str = cmd_str + "AND rg_date_month >= ? "
    if(month_max != 0):
        data_list.append(month_max)
        cmd_str = cmd_str + "AND rg_date_month <= ? "
    if(value_min != float(-1)):
        data_list.append(value_min)
        cmd_str = cmd_str + "AND rg_value >= ? "
    if(value_max != float(-1)):
        data_list.append(value_max)
        cmd_str = cmd_str + "AND rg_value <= ? "

    conn = sqlite3.connect("db_control.db")
    cursor = conn.cursor()
    cursor.execute(f"""{cmd_str}""", data_list)
    data = cursor.fetchall()
    conn.close()

    return data

def new_register(main, username: str):
    """
        FUNCTIONALITY: function that makes a new record in the database.
        :param  - main: main window context. 
                - username: parameter with the username passed by the user.
        :return: nothing.
    """ 
    conn = sqlite3.connect('db_control.db')
    cursor = conn.cursor()

    title = main.ld_add_title.text()
    creditor = main.ld_add_creditor.text()
    value = main.ld_add_value.text()

    if("," in value):
        value = value.replace(',','.')

    if(title == "" or creditor == "" or value == ""):
        main.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
        main.fr_error_msg.show()
        main.lb_error_msg.setText(f"All fields are required!")
    else:
        if(not is_number(value)):
            main.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
            main.fr_error_msg.show()
            main.lb_error_msg.setText(f"The value field requires a float number!")
        else:
            if main.rb_add_revenues.isChecked():
                type_registry = "REVENUE"
            elif main.rb_add_expenses.isChecked():
                type_registry = "EXPENSES"

            date = main.de_add_date.date().toString("dd/MM/yyyy")
            date_split = date.split("/")

            db = []
            db.append(username)
            db.append(type_registry)
            db.append(title.upper())
            db.append(creditor.upper())
            db.append(date)
            db.append(int(date_split[0]))
            db.append(int(date_split[1]))
            db.append(int(date_split[2]))
            db.append(float(value))

            cursor.execute(""" INSERT INTO tb_registry (rg_proprietary, rg_type, rg_title, rg_creditor, rg_date, rg_date_day, rg_date_month, rg_date_year, rg_value) VALUES (?,?,?,?,?,?,?,?,?)""", db)
            conn.commit()
            conn.close()

            print(f"{username} added a new registry!")
            main.fr_error_msg.setStyleSheet("background-color: rgb(85, 255, 127); border-radius: 5px;")
            main.fr_error_msg.show()
            main.lb_error_msg.setText("Registry successfully added!")
            
            main.btn_error_msg.clicked.connect( lambda: main.fr_error_msg.hide())
            QtCore.QTimer.singleShot(5000, lambda: main.fr_error_msg.hide())
            
            main.ld_add_title.clear()
            main.ld_add_creditor.clear()
            main.ld_add_value.clear()
            main.rb_add_revenues.setChecked(True)
            today = QtCore.QDate.currentDate()
            main.de_add_date.setDate(today)            


"""
    System functions
"""

def plot(main, months, values, title: str, axis_x_name: str, axis_y_name: str, legend: str, color: str):
    #BM OBS: Falta descrever o retorno "data_line"
    """
        FUNCTIONALITY: function that forms and draws the graph from the data.
        :param - main: main window context.
               - months: list of values indicating the months.
               - values: list with the values of each month.
               - title: graph title
               - x: axis x name
               - y: axis y name
               - legend: legend for graph
               - color: color of line
        :return: - data_line: PENDENTE.
    """
    pen = pg.mkPen(color=color)
    main.graphWidget.setBackground((31,35,38))
    main.graphWidget.setTitle(f"<span style=\"color: rgb(255,255,255);font-size:18px;font-weight:600;\">{title}</span>")
    main.graphWidget.setLabel("left", f"<span style=\"color:rgb(255,255,255);font-size:13px;font-weight:600;\">{axis_x_name} ($)</span>")
    main.graphWidget.setLabel("bottom", f"<span style=\"color: rgb(255,255,255);font-size:13px;font-weight:600;\">{axis_y_name} (months)</span>")
    main.graphWidget.addLegend()
    main.graphWidget.showGrid(x=True, y=True)
    data_line = main.graphWidget.plot(months, values, name=legend, pen=pen)

    return data_line

def set_graph(main, username: str):
    """
        FUNCTIONALITY: function that defines elements and data to be displayed in the graph.
        :param - main: main window context.
               - username: parameter with the username passed by the user.
        :return: nothing.
    """
    _translate = QtCore.QCoreApplication.translate

    month_min = main.cb_home_filter_min.currentText()
    month_max = main.cb_home_filter_max.currentText()

    index_min = main.cb_home_filter_min.findText(main.cb_home_filter_min.currentText(), QtCore.Qt.MatchFixedString)
    index_max = main.cb_home_filter_max.findText(main.cb_home_filter_max.currentText(), QtCore.Qt.MatchFixedString)

    year = main.ld_home_filter_year.text()

    if(not is_number(year)):
        year = int(datetime.date.today().strftime("%Y"))
        main.ld_home_filter_year.setText("")
        main.ld_home_filter_year.setPlaceholderText(str(year))

    if(index_min == 0 and index_max == 0):
        month_min = "January"
        month_max = "December"
        index_min = 1
        index_max = 12

    data_expenses = get_data(username, "EXPENSES", index_min, index_max, year)
    data_revenue = get_data(username, "REVENUE", index_min, index_max, year)

    data_revenue, total_revenue = format_data_for_graph(data_revenue)
    data_expenses, total_expenses = format_data_for_graph(data_expenses)
    total = total_revenue - total_expenses
    # months = {0:'Jan',1:'Feb',2:'Mar',3:'Apr',4:'May',5:'June',6:'Jul',7:'Aug',8:'Sept',9:'Oct',10:'Nov',11:'Dec'}
    # months = ['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sept','Oct','Nov','Dec']
    # months = dict(enumerate(months))

    main.graphWidget.clear()
    plot(main, [1,2,3,4,5,6,7,8,9,10,11,12], data_revenue, f"Financial statement for the period {month_min} ~ {month_max} {year}", "Values", "Time", "Revenue", [85,255,127])
    plot(main, [1,2,3,4,5,6,7,8,9,10,11,12], data_expenses, f"Financial statement for the period {month_min} ~ {month_max} {year}", "Values", "Time", "Expenses", [255,85,128])
    # plot(main, months, data_revenue, f"Financial statement for the period {month_min} ~ {month_max} {year}", "Values", "Time", "Revenue", [85,255,127])
    # plot(main, months, data_expenses, f"Financial statement for the period {month_min} ~ {month_max} {year}", "Values", "Time", "Expenses", [255,85,128])
    main.lb_home_revenue.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#c8c8c8;\">Revenue: </span><span style=\" color:#55ff7f;\">${total_revenue:.2f}</span></p></body></html>"))
    main.lb_home_expenses.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#c8c8c8;\">Expenses: </span><span style=\" color:#ff5580;\">${total_expenses:.2f}</span></p></body></html>"))
    
    if(total > 0):
        color = "#55ff7f"
    elif(total == 0):
        color = "#c8c8c8"
    else:
        color = "#ff5580"
    
    main.lb_home_total.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#c8c8c8;\">Total: </span><span style=\" color:{color};\">${total:.2f}</span></p></body></html>"))

def search_list(main, username: str):
    #BM PENDÊNCIA: MELHORAR A EURÍSTICA DE PESQUISA, CONSIDERANDO TAMBÉM SUBSTRINGS
    """
        FUNCTIONALITY: function that puts the user's income information in the "search" tab.
        :param - main: main window context.
               - username: parameter with the username passed by the user.
        :return: nothing.
    """
    conn = sqlite3.connect('db_control.db')
    cursor = conn.cursor()

    search = main.ld_search.text().upper()

    cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? OR rg_title = ? OR rg_creditor = ? OR rg_date = ? OR rg_value = ? AND rg_proprietary = ? """, (search, search, search, search, search, username))
    data = cursor.fetchall()
    conn.close()

    _translate = QtCore.QCoreApplication.translate
    headers = ["TYPE", "TITLE","CREDITOR","DUE DATE","VALUE"]
    width_tb_search_list = main.tb_search_list.frameGeometry().width()

    if main.tb_search_list.rowCount() > 0:
        for i in range(main.tb_search_list.rowCount()):
            main.tb_search_list.removeRow(main.tb_search_list.rowCount() - 1)

    main.tb_search_list.setColumnCount(5)

    for i in range(len(data)):
        main.tb_search_list.insertRow(i)
        main.tb_search_list.setItem(i, 0, QTableWidgetItem(str(data[i][2])))
        main.tb_search_list.setItem(i, 1, QTableWidgetItem(str(data[i][3])))
        main.tb_search_list.setItem(i, 2, QTableWidgetItem(str(data[i][4])))
        main.tb_search_list.setItem(i, 3, QTableWidgetItem(str(data[i][5])))
        value = float(data[i][9])
        main.tb_search_list.setItem(i, 4, QTableWidgetItem(str(f"{value:.2f}")))
        main.tb_search_list.setRowHeight(i, 20)

    main.tb_search_list.setColumnWidth(0,width_tb_search_list/5)
    main.tb_search_list.setColumnWidth(1,width_tb_search_list/5)
    main.tb_search_list.setColumnWidth(2,width_tb_search_list/5)
    main.tb_search_list.setColumnWidth(3,width_tb_search_list/5)
    main.tb_search_list.setColumnWidth(4,width_tb_search_list/5)
    main.tb_search_list.setHorizontalHeaderLabels(headers)
    main.tb_search_list.verticalHeader().setVisible(False)
    main.tb_search_list.setStyleSheet("QTableView {background-color: rgb(47, 47, 47); selection-background-color: rgb(0, 139, 209);font-weight: bold;}")
    main.tb_search_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
    main.tb_search_list.setSelectionBehavior(QAbstractItemView.SelectRows)

    if len(data) > 0:
        main.fr_error_msg.setStyleSheet("background-color: rgb(85, 255, 127); border-radius: 5px;")
        main.lb_error_msg.setText(f"{len(data)} search result(s) have been found!")
        main.fr_error_msg.show()
        main.btn_error_msg.clicked.connect( lambda: main.fr_error_msg.hide())
        QtCore.QTimer.singleShot(5000, lambda: main.fr_error_msg.hide())
        main.lb_search_result.setText(f"{len(data)} search result(s) have been found!")
    else:
        main.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
        main.lb_error_msg.setText(f"No results found!")
        main.fr_error_msg.show()
        main.btn_error_msg.clicked.connect( lambda: main.fr_error_msg.hide())
        QtCore.QTimer.singleShot(5000, lambda: main.fr_error_msg.hide())
        main.lb_search_result.setText("No results found!")

def revenue_list(main, username: str, tab: str):
    """
        FUNCTIONALITY: function that puts the user's income information in the "revenues" tab.
        :param - main: main window context.
               - username: parameter with the username passed by the user.
               - tab: parameter that indicates which tab the click action came from.
        :return: nothing.
    """
    register_type = "REVENUE"


    if(tab == "home"):
        index_min = main.cb_home_filter_min.findText(main.cb_home_filter_min.currentText(), QtCore.Qt.MatchFixedString)
        index_max = main.cb_home_filter_max.findText(main.cb_home_filter_max.currentText(), QtCore.Qt.MatchFixedString)

        if index_min >= 0 and index_max >= 0:
            main.cb_revenue_months_min.setCurrentIndex(index_min)
            main.cb_revenue_months_max.setCurrentIndex(index_max)

        year = main.ld_home_filter_year.text()
        main.ld_revenue_year.setText(year)
        
        if(not is_number(year)):
            year = int(datetime.date.today().strftime("%Y"))
        
        data = get_data(username, register_type, index_min, index_max,year)

    else:
        index_min = main.cb_revenue_months_min.findText(main.cb_revenue_months_min.currentText(), QtCore.Qt.MatchFixedString)
        index_max = main.cb_revenue_months_max.findText(main.cb_revenue_months_max.currentText(), QtCore.Qt.MatchFixedString)

        value_min = main.ld_revenue_min.text()
        value_max = main.ld_revenue_max.text()

        if("," in value_min):
            value_min = value_min.replace(',','.')
        if("," in value_max):
            value_max = value_max.replace(',','.')

        year = main.ld_revenue_year.text()
        
        if(not is_number(year)):
            year = int(datetime.date.today().strftime("%Y"))
        
        if(not is_number(value_min)):
            value_min = float(-1)
        else:
            value_min = float(value_min)
        
        if(not is_number(value_max)):
            value_max = float(-1)
        else:
            value_max = float(value_max)

        data = get_data(username, register_type, index_min, index_max, year, value_min, value_max)

    _translate = QtCore.QCoreApplication.translate
    total_revenue = 0.00
    headers = ["TITLE","CREDITOR","DUE DATE","VALUE"]
    width_tb_revenue_list = main.tb_revenue_list.frameGeometry().width()

    main.tb_revenue_list.setColumnCount(4)

    if main.tb_revenue_list.rowCount() > 0:
        for i in range(main.tb_revenue_list.rowCount()):
            main.tb_revenue_list.removeRow(main.tb_revenue_list.rowCount() - 1)

    for i in range(len(data)):
        main.tb_revenue_list.insertRow(i)
        main.tb_revenue_list.setItem(i, 0, QTableWidgetItem(str(data[i][3])))
        main.tb_revenue_list.setItem(i, 1, QTableWidgetItem(str(data[i][4])))
        main.tb_revenue_list.setItem(i, 2, QTableWidgetItem(str(data[i][5])))
        value = float(data[i][9])
        main.tb_revenue_list.setItem(i, 3, QTableWidgetItem(str(f"{value:.2f}")))
        main.tb_revenue_list.setRowHeight(i, 20)
        total_revenue = total_revenue + data[i][9]
    
    main.tb_revenue_list.setColumnWidth(0,width_tb_revenue_list/4)
    main.tb_revenue_list.setColumnWidth(1,width_tb_revenue_list/4)
    main.tb_revenue_list.setColumnWidth(2,width_tb_revenue_list/4)
    main.tb_revenue_list.setColumnWidth(3,width_tb_revenue_list/4)
    main.tb_revenue_list.setHorizontalHeaderLabels(headers)
    main.tb_revenue_list.verticalHeader().setVisible(False)
    main.tb_revenue_list.setStyleSheet("QTableView {background-color: rgb(47, 47, 47); selection-background-color: rgb(0, 139, 209);font-weight: bold;}")
    main.tb_revenue_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
    main.tb_revenue_list.setSelectionBehavior(QAbstractItemView.SelectRows)
    main.lb_revenue_total.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#c8c8c8;\">Total: </span><span style=\" color:#55ff7f;\">${total_revenue:.2f}</span></p></body></html>"))

def expenses_list(main, username: str, tab: str):
    """
        FUNCTIONALITY: function that puts the user's income information in the "expenses" tab.
        :param - main: main window context.
               - username: parameter with the username passed by the user.
               - tab: parameter that indicates which tab the click action came from.
        :return: nothing.
    """
    register_type = "EXPENSES"


    if(tab == "home"):
        index_min = main.cb_home_filter_min.findText(main.cb_home_filter_min.currentText(), QtCore.Qt.MatchFixedString)
        index_max = main.cb_home_filter_max.findText(main.cb_home_filter_max.currentText(), QtCore.Qt.MatchFixedString)

        if index_min >= 0 and index_max >= 0:
            main.cb_expenses_months_min.setCurrentIndex(index_min)
            main.cb_expenses_months_max.setCurrentIndex(index_max)

        year = main.ld_home_filter_year.text()
        main.ld_expenses_year.setText(year)
        
        if(not is_number(year)):
            year = int(datetime.date.today().strftime("%Y"))
        
        data = get_data(username, register_type, index_min, index_max,year)
    
    else:
        index_min = main.cb_expenses_months_min.findText(main.cb_expenses_months_min.currentText(), QtCore.Qt.MatchFixedString)
        index_max = main.cb_expenses_months_max.findText(main.cb_expenses_months_max.currentText(), QtCore.Qt.MatchFixedString)

        value_min = main.ld_expenses_min.text()
        value_max = main.ld_expenses_max.text()

        if("," in value_min):
            value_min = value_min.replace(',','.')
        if("," in value_max):
            value_max = value_max.replace(',','.')
        
        year = main.ld_expenses_year.text()

        if(not is_number(year)):
            year = int(datetime.date.today().strftime("%Y"))
        
        if(not is_number(value_min)):
            value_min = float(-1)
        else:
            value_min = float(value_min)
        
        if(not is_number(value_max)):
            value_max = float(-1)
        else:
            value_max = float(value_max)

        data = get_data(username, register_type, index_min, index_max, year, value_min, value_max)

    _translate = QtCore.QCoreApplication.translate
    total_expenses = 0.00
    headers = ["TITLE","CREDITOR","DUE DATE","VALUE"]
    width_tb_expenses_list = main.tb_expenses_list.frameGeometry().width()

    main.tb_expenses_list.setColumnCount(4)

    if main.tb_expenses_list.rowCount() > 0:
        for i in range(main.tb_expenses_list.rowCount()):
            main.tb_expenses_list.removeRow(main.tb_expenses_list.rowCount() - 1)

    for i in range(len(data)):
        main.tb_expenses_list.insertRow(i)
        main.tb_expenses_list.setItem(i, 0, QTableWidgetItem(str(data[i][3])))
        main.tb_expenses_list.setItem(i, 1, QTableWidgetItem(str(data[i][4])))
        main.tb_expenses_list.setItem(i, 2, QTableWidgetItem(str(data[i][5])))
        value = float(data[i][9])
        main.tb_expenses_list.setItem(i, 3, QTableWidgetItem(str(f"{value:.2f}")))
        main.tb_expenses_list.setRowHeight(i, 20)
        total_expenses = total_expenses + float(data[i][9])

    main.tb_expenses_list.setColumnWidth(0,width_tb_expenses_list/4)
    main.tb_expenses_list.setColumnWidth(1,width_tb_expenses_list/4)
    main.tb_expenses_list.setColumnWidth(2,width_tb_expenses_list/4)
    main.tb_expenses_list.setColumnWidth(3,width_tb_expenses_list/4)
    main.tb_expenses_list.setHorizontalHeaderLabels(headers)
    main.tb_expenses_list.verticalHeader().setVisible(False)
    main.tb_expenses_list.setStyleSheet("QTableView {background-color: rgb(47, 47, 47); selection-background-color: rgb(0, 139, 209);font-weight: bold;}")
    main.tb_expenses_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
    main.tb_expenses_list.setSelectionBehavior(QAbstractItemView.SelectRows)    
    main.lb_expenses_total.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#c8c8c8;\">Total: </span><span style=\" color:#ff5580;\">${total_expenses:.2f}</span></p></body></html>"))

def setting_main_window(main, data_user):
    """
        FUNCTIONALITY: function that setting elements of the main window.
        :param - main: main window context.
        :return: nothing.
    """
    '''
        >> "main" window visual settings
    '''
    _translate = QtCore.QCoreApplication.translate

    ''' ! set title window ! '''
    main.setWindowTitle(_translate("MainWindow", f"My Finances - {data_user['name']}"))

    ''' ! set welcome msg ! '''
    main.fr_error_msg.setStyleSheet("background-color: rgb(85, 255, 127); border-radius: 5px;")
    main.lb_error_msg.setText(f"Welcome {data_user['username']}!")
    main.fr_error_msg.show()
    main.show()
    main.btn_error_msg.clicked.connect( lambda: main.fr_error_msg.hide())
    QtCore.QTimer.singleShot(5000, lambda: main.fr_error_msg.hide())

    ''' ! set date and time ! '''
    timer = QTimer(main)
    timer.timeout.connect(lambda: update_time(main))
    timer.start(1000)
    current_year = int(datetime.date.today().strftime("%Y"))

    ''' ! set icon's tabs ! '''
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(":/home/graph-home-white-32x32.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)

    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(":/add/add-white-32x32.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)

    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap(":/money/stat-up-white-32x32.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    
    icon4 = QtGui.QIcon()
    icon4.addPixmap(QtGui.QPixmap(":/money/stat-down-white-32x32.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    
    icon5 = QtGui.QIcon()
    icon5.addPixmap(QtGui.QPixmap(":/money/graph-total-white-32x32.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    
    icon6 = QtGui.QIcon()
    icon6.addPixmap(QtGui.QPixmap(":/user/user-white-32x32.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    
    icon7 = QtGui.QIcon()
    icon7.addPixmap(QtGui.QPixmap(":/settings/settings-white-32x32.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    
    icon8 = QtGui.QIcon()
    icon8.addPixmap(QtGui.QPixmap(":/search/search-white-32x32.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    
    icon9 = QtGui.QIcon()
    icon9.addPixmap(QtGui.QPixmap(":/pencil/lapis(copiar).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)        

    ''' ! remove tabs ! '''
    main.tb_content_view.removeTab(8)
    main.tb_content_view.removeTab(7)
    main.tb_content_view.removeTab(6)
    main.tb_content_view.removeTab(5)
    main.tb_content_view.removeTab(4)
    main.tb_content_view.removeTab(3)
    main.tb_content_view.removeTab(2)
    main.tb_content_view.removeTab(1)

    ''' ! set layout add ! '''
    main.rb_add_revenues.setChecked(True)
    today = QtCore.QDate.currentDate()
    main.de_add_date.setDate(today)

    ''' ! set layout home ! '''
    main.tb_content_view.addTab(main.tb_home, icon1,"Home")

    main.cb_home_filter_min.addItems(["Select month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    main.cb_home_filter_max.addItems(["Select month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    
    main.ld_home_filter_year.setPlaceholderText(_translate("MainWindow", f"{current_year}"))
    
    main.lb_home_revenue.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.lb_home_revenue.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_revenue, icon3,"Revenue"))              
    main.lb_home_revenue.clicked.connect(lambda: revenue_list(main, data_user['username'], "home"))

    main.lb_home_expenses.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.lb_home_expenses.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_expenses, icon4,"Expenses"))
    main.lb_home_expenses.clicked.connect(lambda: expenses_list(main, data_user['username'], "home"))
    
    main.btn_home_filter.clicked.connect(lambda: set_graph(main, data_user['username']))

    ''' ! set layout revenue ! '''
    main.cb_revenue_months_min.addItems(["Select month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    main.cb_revenue_months_max.addItems(["Select month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    main.ld_revenue_year.setPlaceholderText(_translate("MainWindow", f"{current_year}"))

    ''' ! set layout expenses ! '''
    main.cb_expenses_months_min.addItems(["Select month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    main.cb_expenses_months_max.addItems(["Select month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    main.ld_expenses_year.setPlaceholderText(_translate("MainWindow", f"{current_year}"))

    ''' ! set layout profile ! '''
    main.lb_profile_name.setText(f"{data_user['name']}")
    main.lb_profile_username.setText(f"{data_user['username']}")
    main.lb_profile_email.setText(f"Email: {data_user['email']}")
    i = len(data_user['password'])
    main.lb_profile_password.setText("Password: " + "*"*i)

    ''' ! set layout edit ! '''
    main.ld_edit_name.setPlaceholderText(_translate("MainWindow", f"{data_user['name']}"))
    main.ld_edit_username.setPlaceholderText(_translate("MainWindow", f"{data_user['username']}"))
    main.ld_edit_password.setPlaceholderText(_translate("MainWindow", "*"*i))
    main.ld_edit_email.setPlaceholderText(_translate("MainWindow", f"{data_user['email']}"))

    ''' ! set graph ! '''
    set_graph(main, data_user['username'])

    '''
        >> "main" window button click events
    '''
    
    ''' ! abas click events ! '''
    main.btn_add.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.btn_add.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_add, icon2,"Add"))        
    main.btn_add_register.clicked.connect(lambda: new_register(main, data_user['username']))    
    
    main.btn_home.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.btn_home.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_home, icon1,"Home"))
    main.btn_home.clicked.connect(lambda: set_graph(main, data_user['username']))
    
    main.btn_revenue.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.btn_revenue.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_revenue, icon3,"Revenue"))
    main.btn_revenue.clicked.connect(lambda: revenue_list(main, data_user['username'], "revenue"))    
    main.btn_revenue_filter.clicked.connect(lambda:revenue_list(main, data_user['username'], "revenue"))

    main.btn_expenses.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.btn_expenses.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_expenses, icon4,"Expenses"))
    main.btn_expenses.clicked.connect(lambda: expenses_list(main, data_user['username'], "expenses"))
    main.btn_expenses_filter.clicked.connect(lambda:expenses_list(main, data_user['username'], "expenses"))

    main.btn_transactions.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.btn_transactions.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_transactions, icon5,"Transactions"))
    
    main.btn_user.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.btn_user.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_profile, icon6,f"{data_user['name']}"))
    
    main.btn_settings.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.btn_settings.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_settings, icon7,"Settings"))
    
    main.btn_search.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.btn_search.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_search, icon8,"Search"))
    main.btn_search.clicked.connect(lambda: search_list(main, data_user['username']))
    
    main.btn_profile_edit.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.btn_profile_edit.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_edit, icon9,"Edit"))

def create_account(self):
    """
        FUNCTIONALITY: function that creates a new user account in the database.
        :param - self: window context where the function is being called.
        :return: nothing.
    """
    email_regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    ''' ! database initialization ! '''
    conn = sqlite3.connect('db_control.db')
    cursor = conn.cursor()

    ''' ! data collected by inputs ! '''
    dict = {}
    dict['name'] = self.ld_name.text()
    dict['username'] = self.ld_username.text()
    dict['password'] = self.ld_password.text()
    dict['confirm_password'] = self.ld_confirm_password.text()
    dict['email'] = self.ld_email.text()

    ''' ! data validation ! '''
    if(dict['name'] == "" or dict['username'] == "" or
    dict['password'] == "" or dict['confirm_password'] == "" or
    dict['email'] == ""):
        self.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
        self.lb_error_msg.setText(f"All fields are required!")
        self.fr_error_msg.show()
    else:
        if(len(dict['password']) < 8):
            self.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
            self.fr_error_msg.show()
            self.lb_error_msg.setText("The password needs at least 8 digits!")
        else:
            if(dict['password'] != dict['confirm_password']):
                self.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
                self.fr_error_msg.show()
                self.lb_error_msg.setText("Password and confirm password are different!")
            else:
                if(re.search(email_regex, dict['email'])):
                    cursor.execute(""" SELECT * FROM tb_users WHERE username = ?""",(dict['username'],))
                    data = cursor.fetchall()
                    conn.close()

                    if(data != []):
                        print(f"The new user tried to register with an existing username {dict['username']}")
                        self.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
                        self.fr_error_msg.show()
                        self.lb_error_msg.setText(f"The username {dict['username']} exist!")
                    else:
                        conn = sqlite3.connect('db_control.db')
                        cursor = conn.cursor()
                        cursor.execute(""" INSERT INTO tb_users (name, username, password, email) VALUES (?,?,?,?)""",
                        (dict['name'],dict['username'],dict['password'],dict['email'],))
                        conn.commit()
                        conn.close()

                        print(f"The new user {dict['name']} was registered!")
                
                        self.fr_error_msg.setStyleSheet("background-color: rgb(85, 255, 127); border-radius: 5px;")
                        self.fr_error_msg.show()
                        self.lb_error_msg.setText("Account successfully created!")
                        QtCore.QTimer.singleShot(3000, lambda: self.hide())                                                          
                else:
                    self.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
                    self.fr_error_msg.show()
                    self.lb_error_msg.setText("The email is not valid!")                           

def verify_login(self):
    """
        FUNCTIONALITY: function that checks user login.
        :param - self: window context where the function is being called.
        :return: nothing.
    """
    username = self.ld_username.text()
    password = self.ld_password.text()

    ''' ! decision making ! '''
    if(username == "" or password == ""):
        self.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
        self.fr_error_msg.show()
        self.lb_error_msg.setText("Enter Username and Password fields!")
    else:
        if(search_user(username, password)):
            self.fr_error_msg.setStyleSheet("background-color: rgb(85, 255, 127); border-radius: 5px;")
            self.lb_error_msg.setText("Successfully login! Loadin your account...")
            self.fr_error_msg.show()
            QtCore.QTimer.singleShot(1500, lambda: self.show_main_window(username))
            QtCore.QTimer.singleShot(1500, lambda: self.hide())
        else:
            self.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
            self.lb_error_msg.setText("Username or password is wrong!")
            self.fr_error_msg.show()

def update_time(self):
    """
        FUNCTIONALITY: function that puts date and time in main window.
        :param - self: window context where the function is being called.
        :return: nothing.
    """
    locale.setlocale(locale.LC_TIME, "en_US.utf8")
    current_time = QTime.currentTime().toString("hh:mm")
    current_date = datetime.date.today().strftime("%A, %d/%m/%Y")
    date_time = current_date + "  " + current_time
    self.lb_date_time.setText(date_time)