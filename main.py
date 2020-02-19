"""
First created a QT file of type UI
Make changes using the designer tool (WYSIWYG)
Use the pyside2-uic tool to convert to a python class
Syntax: pyside2-uic mainwindow.ui > ui_mainwindow.py
NOTE: Must run pyside2-uic every time there are changes on the pyside2-uic file
"""
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
