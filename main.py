"""
First created a QT file of type UI
Make changes using the designer tool (WYSIWYG)
Use the pyside2-uic tool to convert to a python class
Syntax: pyside2-uic mainwindow.ui > ui_mainwindow.py
NOTE: Must run pyside2-uic every time there are changes on the pyside2-uic file
"""
from PySide2 import QtWidgets as qw

#from PySide2.QtWidgets import QApplication, QMainWindow
from login import Login

from ui_parent_window import Ui_MainWindow

class MainWindow(qw.QMainWindow):
    """[summary]

    Arguments:
        qw {[type]} -- [description]
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_window = Ui_MainWindow()
        self.ui_window.setupUi(self)


if __name__ == "__main__":
    import sys
    APP = qw.QApplication(sys.argv)
    LOGIN = Login()
    
    if LOGIN.exec_() == qw.QDialog.Accepted:
        WINDOW = MainWindow()
        WINDOW.show()
        sys.exit(APP.exec_())
