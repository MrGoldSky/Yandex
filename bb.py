import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QDockWidget, QApplication, QMainWindow, QPushButton, QLabel, QTimeEdit, QListWidget
from PyQt5.QtWidgets import QCalendarWidget, QMainWindow
import difflib


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('solution.ui', self)
        self.pushButton.clicked.connect(self.result)


    def result(self):
        self.porog = self.doubleSpinBox.value()
        self.text_1 = self.textEdit.toPlainText().split("\n")
        self.text_2 = self.textEdit_2.toPlainText().split("\n")

        same = difflib.SequenceMatcher(None, self.text_1, self.text_2).ratio()

        if self.porog > same * 100:
            self.statusBar().setStyleSheet("background-color: green")
            self.statusBar().showMessage(f"Код похож на {same * 100}%")
        else:
            self.statusBar().setStyleSheet("background-color: red")
            self.statusBar().showMessage(f"Код похож на {same * 100}%")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())