from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QAbstractItemView
from login import Ui_MainWindow
import sys
import re
import time
import datetime
import locale
import sqlite3
import resources_rc
import register
import main

def Update_time(self, main):
    locale.setlocale(locale.LC_TIME, "en_US.utf8")
    current_time = QTime.currentTime().toString("hh:mm")
    current_date = datetime.date.today().strftime("%A, %d/%m/%Y")
    date_time = current_date + "  " + current_time
    main.lb_date_time.setText(date_time)

def Is_number(number):
    try:
        float(number)
    except ValueError:
        return False
    return True

def Which_month(month):
    if month == "January":
        month_num = 1
    elif month == "February":
        month_num = 2
    elif month == "March":
        month_num = 3
    elif month == "April":
        month_num = 4
    elif month == "May":
        month_num = 5
    elif month == "June":
        month_num = 6
    elif month == "July":
        month_num = 7
    elif month == "August":
        month_num = 8
    elif month == "September":
        month_num = 9
    elif month == "October":
        month_num = 10
    elif month == "November":
        month_num = 11
    elif month == "December":
        month_num = 12
    else:
        month_num = "Select month"
    return month_num

def Data_graph(data):
    values_graph = [0,0,0,0,0,0,0,0,0,0,0,0]
    value_total = 0

    for fields in data:
        if fields[7] == "1":
            values_graph[0] += int(fields[9])
        elif fields[7] == "2":
            values_graph[1] += int(fields[9])
        elif fields[7] == "3":
            values_graph[2] += int(fields[9])
        elif fields[7] == "4":
            values_graph[3] += int(fields[9])
        elif fields[7] == "5":
            values_graph[4] += int(fields[9])
        elif fields[7] == "6":
            values_graph[5] += int(fields[9])
        elif fields[7] == "7":
            values_graph[6] += int(fields[9])
        elif fields[7] == "8":
            values_graph[7] += int(fields[9])
        elif fields[7] == "9":
            values_graph[8] += int(fields[9])
        elif fields[7] == "10":
            values_graph[9] += int(fields[9])
        elif fields[7] == "11":
            values_graph[10] += int(fields[9])
        elif fields[7] == "12":
            values_graph[11] += int(fields[9])
    
    for values in values_graph:
        value_total+=values

    return values_graph, value_total

def Home_graph(main, username_global, Default):
    _translate = QtCore.QCoreApplication.translate
    month_min = main.cb_home_filter_min.currentText()
    month_max = main.cb_home_filter_max.currentText()
    year = main.ld_home_filter_year.text()

    if month_min != "Select month" and month_max != "Select month" and year != "" and Default == False:
        month_min_num = Which_month(month_min)
        month_max_num = Which_month(month_max)
        if not Is_number(year):
            main.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
            main.fr_error_msg.show()
            main.lb_error_msg.setText("Please enter a valid year!")

        data_revenue = Search_filter(username_global, "REVENUE", month_min_num, month_max_num, year, "", "")
        data_expenses = Search_filter(username_global, "EXPENSES", month_min_num, month_max_num, year, "", "")

        data_revenue, total_revenue = Data_graph(data_revenue)
        data_expenses, total_expenses = Data_graph(data_expenses)
        total = total_revenue - total_expenses
    else:
        data_revenue = Search_filter(username_global, "REVENUE", month_min, month_max, year, "", "")
        data_expenses = Search_filter(username_global, "EXPENSES", month_min, month_max, year, "", "")
        
        data_revenue, total_revenue = Data_graph(data_revenue)
        data_expenses, total_expenses = Data_graph(data_expenses)
        total = total_revenue - total_expenses
        
    main.graphWidget.clear()
    main.plot([1,2,3,4,5,6,7,8,9,10,11,12], data_revenue, f"Financial statement for the period {month_min} ~ {month_max} {year}", "Values", "Time", "Revenue", [85,255,127])
    main.plot([1,2,3,4,5,6,7,8,9,10,11,12], data_expenses, f"Financial statement for the period {month_min} ~ {month_max} {year}", "Values", "Time", "Expenses", [255,85,128])
    main.lb_home_revenue.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#c8c8c8;\">Revenue: </span><span style=\" color:#55ff7f;\">${total_revenue:.2f}</span></p></body></html>"))
    main.lb_home_expenses.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#c8c8c8;\">Expenses: </span><span style=\" color:#ff5580;\">${total_expenses:.2f}</span></p></body></html>"))
    if total > 0:
        color = "#55ff7f"
    elif total == 0:
        color = "#c8c8c8"
    else:
        color = "#ff5580"
    main.lb_home_total.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#c8c8c8;\">Total: </span><span style=\" color:{color};\">${total:.2f}</span></p></body></html>"))

    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap(":/money/dinheiro(copiar).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    icon4 = QtGui.QIcon()
    icon4.addPixmap(QtGui.QPixmap(":/money/seta-para-baixo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    
    main.lb_home_revenue.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.lb_home_revenue.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_revenue, icon3,"Revenue"))
    main.lb_home_revenue.clicked.connect(lambda: Revenue_list(main, username_global, month_min, month_max, year))

    main.lb_home_expenses.clicked.connect(lambda: main.tb_content_view.removeTab(main.tb_content_view.currentIndex()))
    main.lb_home_expenses.clicked.connect(lambda: main.tb_content_view.addTab(main.tb_expenses, icon4,"Expenses"))
    main.lb_home_expenses.clicked.connect(lambda: Expenses_list(main, username_global, month_min, month_max, year))

def Search_filter(username_global, type_rg, month_min, month_max, year, minimum, maximum):
    conn = sqlite3.connect('db_control.db')
    cursor = conn.cursor()
    current_year = int(datetime.date.today().strftime("%Y"))


    #Defaults filter
    if month_min == "Select month" and month_max == "Select month" and year == "" and minimum == "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_year = ? """, (type_rg, username_global, current_year))
    #Individual filter fields
    elif month_min != "Select month" and month_max == "Select month" and year == "" and minimum == "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? """, (type_rg, username_global, month_min))
    elif month_min == "Select month" and month_max != "Select month" and year == "" and minimum == "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month <= ? """, (type_rg, username_global, month_max))
    elif month_min == "Select month" and month_max == "Select month" and year != "" and minimum == "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_year = ? """, (type_rg, username_global, int(year)))
    elif month_min == "Select month" and month_max == "Select month" and year == "" and minimum != "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_value >= ? """, (type_rg, username_global, minimum))
    elif month_min == "Select month" and month_max == "Select month" and year == "" and minimum == "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_value <= ? """, (type_rg, username_global, maximum)) 
    #Combinations 2 to 2 with the field "months_min"
    elif month_min != "Select month" and month_max != "Select month" and year == "" and minimum == "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_date_month <= ? """, (type_rg, username_global, month_min, month_max))
    elif month_min != "Select month" and month_max == "Select month" and year != "" and minimum == "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_date_year = ? """, (type_rg, username_global, month_min, int(year)))
    elif month_min != "Select month" and month_max == "Select month" and year == "" and minimum != "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_value >= ? """, (type_rg, username_global, month_min, minimum))
    elif month_min != "Select month" and month_max == "Select month" and year == "" and minimum == "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_value <= ? """, (type_rg, username_global, month_min, maximum))
    #Combinations 2 to 2 with the field "months_max"
    elif month_min == "Select month" and month_max != "Select month" and year != "" and minimum == "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month <= ? AND rg_date_year = ? """, (type_rg, username_global, month_max, int(year)))
    elif month_min == "Select month" and month_max != "Select month" and year == "" and minimum != "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month <= ? AND rg_value >= ? """, (type_rg, username_global, month_max, minimum))
    elif month_min == "Select month" and month_max != "Select month" and year == "" and minimum == "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month <= ? AND rg_value <= ? """, (type_rg, username_global, month_max, maximum))
    #Combinations 2 to 2 with the field "year"
    elif month_min == "Select month" and month_max == "Select month" and year != "" and minimum != "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_year = ? AND rg_value >= ? """, (type_rg, username_global, int(year), minimum))
    elif month_min == "Select month" and month_max == "Select month" and year != "" and minimum == "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_year = ? AND rg_value <= ? """, (type_rg, username_global, int(year), maximum))
    #Combinations 2 to 2 with the field "value_min"
    elif month_min == "Select month" and month_max == "Select month" and year == "" and minimum != "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_value >= ? AND rg_value <= ? """, (type_rg, username_global, minimum, maximum))
    #Combinatios 3 to 3 with the field "month_min"
    elif month_min != "Select month" and month_max != "Select month" and year != "" and minimum == "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_date_month <= ? AND rg_date_year = ? """, (type_rg, username_global, month_min, month_max, int(year)))
    elif month_min != "Select month" and month_max != "Select month" and year == "" and minimum != "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_date_month <= ? AND rg_value >= ? """, (type_rg, username_global, month_min, month_max, minimum))
    elif month_min != "Select month" and month_max != "Select month" and year == "" and minimum == "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_date_month <= ? AND rg_value <= ? """, (type_rg, username_global, month_min, month_max, maximum))
    elif month_min != "Select month" and month_max == "Select month" and year != "" and minimum != "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_date_year = ? AND rg_value >= ? """, (type_rg, username_global, month_min, int(year), minimum))
    elif month_min != "Select month" and month_max == "Select month" and year != "" and minimum == "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_date_year = ? AND rg_value <= ? """, (type_rg, username_global, month_min, int(year), maximum))
    elif month_min != "Select month" and month_max == "Select month" and year == "" and minimum != "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_value >= ? AND rg_value <= ? """, (type_rg, username_global, month_min, minimum, maximum))
    #Combinations 3 to 3 with the field "month_max"
    elif month_min == "Select month" and month_max != "Select month" and year != "" and minimum != "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month <= ? AND rg_date_year = ? AND rg_value >= ? """, (type_rg, username_global, month_min, int(year), minimum))
    elif month_min == "Select month" and month_max != "Select month" and year != "" and minimum == "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month <= ? AND rg_date_year = ? AND rg_value <= ? """, (type_rg, username_global, month_min, int(year), maximum))
    elif month_min == "Select month" and month_max != "Select month" and year == "" and minimum != "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month <= ? AND rg_value >= ? AND rg_value <= ? """, (type_rg, username_global, month_min, minimum, maximum))
    #Combinatios 3 to 3 with the field "year"
    elif month_min == "Select month" and month_max == "Select month" and year != "" and minimum != "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_year = ? AND rg_value >= ? AND rg_value <= ? """, (type_rg, username_global, int(year), minimum, maximum))
    #Combinations 4 to 4 with the field "months_min"
    elif month_min != "Select month" and month_max != "Select month" and year != "" and minimum != "" and maximum == "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_date_month <= ? AND rg_date_year = ? AND rg_value >= ? """, (type_rg, username_global, month_min, month_max, int(year), minimum))
    elif month_min != "Select month" and month_max != "Select month" and year != "" and minimum == "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_date_month <= ? AND rg_date_year = ? AND rg_value <= ? """, (type_rg, username_global, month_min, month_max, int(year), maximum))
    elif month_min != "Select month" and month_max != "Select month" and year == "" and minimum != "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_date_month <= ? AND rg_value >= ? AND rg_value <= ? """, (type_rg, username_global, month_min, month_max, minimum, maximum))
    elif month_min != "Select month" and month_max == "Select month" and year != "" and minimum != "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_date_year = ? AND rg_value >= ? AND rg_value <= ? """, (type_rg, username_global, month_min, int(year), minimum, maximum))
    #Combinations 4 to 4 with the field "months_max"
    elif month_min == "Select month" and month_max != "Select month" and year != "" and minimum != "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month <= ? AND rg_date_year = ? AND rg_value >= ? AND rg_value <= ? """, (type_rg, username_global, month_max, int(year), minimum, maximum))
    #Combination with all fields
    elif month_min != "Select month" and month_max != "Select month" and year != "" and minimum != "" and maximum != "":
        cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? AND rg_proprietary = ? AND rg_date_month >= ? AND rg_date_month <= ? AND rg_date_year = ? AND rg_value >= ? AND rg_value <= ? """, (type_rg, username_global, month_min, month_max, int(year), minimum, maximum))

    data_filter = cursor.fetchall()
    conn.close()

    return data_filter

def Search_list(main, username_global):
    conn = sqlite3.connect('db_control.db')
    cursor = conn.cursor()

    search = main.ld_search.text().upper()


    cursor.execute(""" SELECT * FROM tb_registry WHERE rg_type = ? OR rg_title = ? OR rg_creditor = ? OR rg_date = ? OR rg_value = ? AND rg_proprietary = ? """, (search, search, search, search, search, username_global))
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
        main.tb_search_list.setItem(i, 4, QTableWidgetItem(str(data[i][9])))
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

def Revenue_list(main, username_global, month_min = "Select month", month_max = "Select month", year = ""):
    main.btn_revenue_filter.clicked.connect(lambda:Revenue_list(main, username_global))
    
    if month_min == "Select month" and month_max == "Select month" and year == "":
        month_min = main.cb_revenue_months_min.currentText()
        month_max = main.cb_revenue_months_max.currentText()
        year = main.ld_revenue_year.text()
    else:
        month_min = main.cb_home_filter_min.currentText()
        month_max = main.cb_home_filter_max.currentText()
        year = main.ld_home_filter_year.text()

    minimum = main.ld_revenue_min.text()
    maximum = main.ld_revenue_max.text()

    if month_min != "Select month" or month_max != "Select month":
        month_min = Which_month(month_min)
        month_max = Which_month(month_max)
    if not Is_number(year):
        year = ""
    if not Is_number(minimum):
        minimum = ""
    else:
        minimum = float(minimum)
    if not Is_number(maximum):
        maximum = ""
    else:
        maximum = float(maximum)

    data = Search_filter(username_global, "REVENUE", month_min, month_max, year, minimum, maximum)

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
        main.tb_revenue_list.setItem(i, 3, QTableWidgetItem(str(data[i][9])))
        main.tb_revenue_list.setRowHeight(i, 20)
        total_revenue = total_revenue + float(data[i][9])
    
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

def Expenses_list(main, username_global, month_min = "Select month", month_max = "Select month", year = ""):
    main.btn_expenses_filter.clicked.connect(lambda:Expenses_list(main, username_global, month_min, month_max))
    
    if month_min == "Select month" and month_max == "Select month" and year == "":
        month_min = main.cb_expenses_months_min.currentText()
        month_max = main.cb_expenses_months_max.currentText()
        year = main.ld_expenses_year.text()
    else:
        month_min = main.cb_home_filter_min.currentText()
        month_max = main.cb_home_filter_max.currentText()
        year = main.ld_home_filter_year.text()
    
    minimum = main.ld_expenses_min.text()
    maximum = main.ld_expenses_max.text()

    if month_min != "Select month" or month_max != "Select month":
        month_min = Which_month(month_min)
        month_max = Which_month(month_max)
    if not Is_number(year):
        year = ""
    if not Is_number(minimum):
        minimum = ""
    else:
        minimum = float(minimum)
    if not Is_number(maximum):
        maximum = ""
    else:
        maximum = float(maximum)

    data = Search_filter(username_global, "EXPENSES", month_min, month_max, year, minimum, maximum)

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
        main.tb_expenses_list.setItem(i, 3, QTableWidgetItem(str(data[i][9])))
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

def New_register(main, username_global):
    conn = sqlite3.connect('db_control.db')
    cursor = conn.cursor()

    title = main.ld_add_title.text()
    creditor = main.ld_add_creditor.text()
    value = main.ld_add_value.text()

    if title == "" or creditor == "" or value == "":
        main.fr_error_msg.setStyleSheet("background-color: rgb(255, 85, 128); border-radius: 5px;")
        main.fr_error_msg.show()
        main.lb_error_msg.setText(f"All fields are required!")
    else:
        if not Is_number(value):
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
            db.append(username_global)
            db.append(type_registry)
            db.append(title.upper())
            db.append(creditor.upper())
            db.append(date)
            db.append(date_split[0])
            db.append(date_split[1])
            db.append(date_split[2])
            db.append(value)

            cursor.execute(""" INSERT INTO tb_registry (rg_proprietary, rg_type, rg_title, rg_creditor, rg_date, rg_date_day, rg_date_month, rg_date_year, rg_value) VALUES (?,?,?,?,?,?,?,?,?)""", db)
            conn.commit()
            conn.close()

            print(f"{username_global} added a new registry!")
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