import sys

import sqlite3

from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtGui

from PyQt5_Yandex_Project import Ui_MainWindow
from About import Ui_Form
from PyQt5.QtWidgets import QDockWidget, QApplication, QMainWindow, QErrorMessage, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel, QTimeEdit, QListWidget, QMessageBox
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

from PyQt5.QtGui import QPixmap

import datetime as dt
from datetime import date
import time


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # uic.loadUi('C:\\Users\\Mr_GoldSky_\\Desktop\\Python\\Yandex projects\\PyQt5_Yandex_Project.ui', self) 
        self.setupUi(self)     
        self.setWindowTitle('Калькулятор времени')
        
        self.first_Date.setDate(QDate.currentDate())
        self.second_Date.setDate(QDate.currentDate())
        self.first_Time.setTime(QTime.currentTime())
        self.second_Time.setTime(QTime.currentTime())
        self.buttonDt2_minus_Dt1.clicked.connect(self.Dt2_minus_Dt1)
        self.buttonDt1_minus_Dt2.clicked.connect(self.Dt1_minus_Dt2)
        self.buttonD1_minus_DeltaDateDay.clicked.connect(self.D1_minus_DeltaDateDay)
        self.buttonD1_plus_DeltaDateDay.clicked.connect(self.D1_plus_DeltaDateDay)
        self.buttonT1_minus_T2.clicked.connect(self.T1_minus_T2)
        self.buttonT2_minus_T1.clicked.connect(self.T2_minus_T1)
        self.buttonT1_minus_DeltaTime.clicked.connect(self.T1_minus_DeltaTime)
        self.buttonT2_minus_DeltaTime.clicked.connect(self.T2_minus_DeltaTime)
        self.action_about.triggered.connect(self.open_about_window)
        
        f = open("logs/logs.txt", mode="a")
        f.write(f"Open {dt.datetime.now()}\n")
        f.close()
        
        con = sqlite3.connect("database/project_db.sqlite")
        cur = con.cursor()
        cur.execute('''
                    UPDATE counts
                    SET count_opens = count_opens + 1
                    WHERE id = 1
                    ''')
        con.commit()
        con.close()

    def select_open(self):
        con = sqlite3.connect("database/project_db.sqlite")
        cur = con.cursor()
        result = cur.execute('''
                    SELECT count_opens FROM counts
                    WHERE id = 1
                    ''').fetchall()[0]
        con.close()
        return result[0]

    def save_result(self, result_f, type_f):
        con = sqlite3.connect("database/project_db.sqlite")
        cur = con.cursor()
        cur.execute(f'''
                    INSERT INTO results(open, result, type)
                    VALUES ({self.select_open()}, '{result_f}', '{type_f}')
                    ''')
        con.commit()
        con.close()

    def Dt1_minus_Dt2(self):
        first_Date = self.first_Date.date().toPyDate()
        second_Date = self.second_Date.date().toPyDate()
        
        if first_Date == second_Date:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Date1 должна отличаться от Date2")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        
        result = str(first_Date - second_Date).replace("0:00:00", "").replace(",", "")
        self.output_Date.setText(result)
        
        self.save_result(result, "Dt1_minus_Dt2")

    def Dt2_minus_Dt1(self):
        first_Date = self.first_Date.date().toPyDate()
        second_Date = self.second_Date.date().toPyDate()
        
        if first_Date == second_Date:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Date1 должна отличаться от Date2")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        
        result = str(second_Date - first_Date).replace("0:00:00", "").replace(",", "")
        self.output_Date.setText(result)
        
        self.save_result(result, "Dt2_minus_Dt1")

    def D1_minus_DeltaDateDay(self):
        first_Date = self.first_Date.date().toPyDate()
        DeltaDateDay = dt.timedelta(days=self.delta_Date_Day.value())
        
        if str(DeltaDateDay) == "0:00:00":
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("DeltaDateDay должна отличаться от 0")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        
        result = str(first_Date - DeltaDateDay)
        self.output_Date.setText(result)
        
        self.save_result(result, "D1_minus_DeltaDateDay")

    def D1_plus_DeltaDateDay(self):
        first_Date = self.first_Date.date().toPyDate()
        DeltaDateDay = dt.timedelta(days=self.delta_Date_Day.value())
        
        if str(DeltaDateDay) == "0:00:00":
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("DeltaDateDay должна отличаться от 0")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        
        result = str(first_Date + DeltaDateDay)
        self.output_Date.setText(result)
        
        self.save_result(result, "D1_plus_DeltaDateDay")

    def T1_minus_T2(self):
        first_Time = self.first_Time.time().toPyTime()
        second_Time = self.second_Time.time().toPyTime()
        
        if first_Time == second_Time:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Time1 должна отличаться от Time2")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        
        rs = dt.datetime.combine(date.today(), first_Time) - dt.datetime.combine(date.today(), second_Time)
        rs = time.gmtime(abs(rs.total_seconds()))
        hours = rs.tm_hour
        minutes = rs.tm_min
        
        result = f"{'{:02}'.format(hours)}:{'{:02}'.format(minutes)}"
        self.output_Time.setText(result)
        
        self.save_result(result, "T1_minus_T2")

    def T2_minus_T1(self):
        first_Time = self.first_Time.time().toPyTime()
        second_Time = self.second_Time.time().toPyTime()
        
        if first_Time == second_Time:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Time1 должна отличаться от Time2")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        
        rs = dt.datetime.combine(date.today(), second_Time) - dt.datetime.combine(date.today(), first_Time)
        rs = time.gmtime(abs(rs.total_seconds()))
        hours = rs.tm_hour
        minutes = rs.tm_min
        
        result = f"{'{:02}'.format(hours)}:{'{:02}'.format(minutes)}"
        self.output_Time.setText(result)
        
        self.save_result(result, "T2_minus_T1")

    def T1_minus_DeltaTime(self):
        first_Time = self.first_Time.time().toPyTime()
        delta_Time = self.delta_Time.time().toPyTime()
        
        if str(delta_Time) == "00:00:00":
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("DeltaTime должна отличаться от 0")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        
        rs = dt.datetime.combine(date.today(), first_Time) - dt.datetime.combine(date.today(), delta_Time)
        rs = time.gmtime(abs(rs.total_seconds()))
        hours = rs.tm_hour
        minutes = rs.tm_min
        
        result = f"{'{:02}'.format(hours)}:{'{:02}'.format(minutes)}"
        self.output_Time.setText(result)
        
        self.save_result(result, "T1_minus_DeltaTime")

    def T2_minus_DeltaTime(self):
        second_Time = self.second_Time.time().toPyTime()
        delta_Time = self.delta_Time.time().toPyTime()
        
        if str(delta_Time) == "00:00:00":
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("DeltaTime должна отличаться от 0")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            return
        
        rs = dt.datetime.combine(date.today(), second_Time) - dt.datetime.combine(date.today(), delta_Time)
        rs = time.gmtime(abs(rs.total_seconds()))
        hours = rs.tm_hour
        minutes = rs.tm_min
        
        result = f"{'{:02}'.format(hours)}:{'{:02}'.format(minutes)}"
        self.output_Time.setText(result)
        
        self.save_result(result, "T2_minus_DeltaTime")

    def open_about_window(self):
        self.second_form = AboutForm()
        self.second_form.show()

    def closeEvent(self, event):
        f = open("logs/logs.txt", mode="a")
        f.write(f"Close {dt.datetime.now()}\n")
        f.close()
        
        con = sqlite3.connect("database/project_db.sqlite")
        cur = con.cursor()
        cur.execute('''
                    UPDATE counts
                    SET count_closes = count_closes + 1
                    WHERE id = 1
                    ''')
        con.commit()
        con.close()


class AboutForm(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        # uic.loadUi('C:\\Users\\Mr_GoldSky_\\Desktop\\Python\\Yandex projects\\About.ui', self)        
        self.setWindowTitle('О программе')
        self.pixmap = QPixmap("img/clock.png")
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec_())