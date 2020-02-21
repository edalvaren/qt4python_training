"""
First created a QT file of type UI
Make changes using the designer tool (WYSIWYG)
Use the pyside2-uic tool to convert to a python class
Syntax: pyside2-uic mainwindow.ui > ui_mainwindow.py
NOTE: Must run pyside2-uic every time there are changes on the pyside2-uic file
"""
import time
from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtGui import QPixmap, Qt
from PySide2.QtCore import Signal, Slot
from .dialogs import Login, Splash
from .ui import MainWindow
from .widgets import PbWidget, MainWizard




class App(QApplication):

    def __init__(self):
        super(App, self).__init__()
        self.splash_pix = QPixmap('resources/img/ilox_brochure.jpg')
        self.splash = Splash(self.splash_pix)
        self.login = Login()
        self.main_window = MainWindow()
        self.pb = PbWidget(self.splash_pix, 20, self.splash)
#        self.toolbar = Toolbar("This is your toolbar", self.main_window)
        self.main_wizard = MainWizard(self.main_window)
        self.init_UI()

    def init_UI(self):
        """starts the application User Interface
        """
        self.splash.show()
        self.splash.showMessage("<h1><font color='green'>Welcome BeeMan!</font></h1>",
                                Qt.AlignTop | Qt.AlignCenter, Qt.black)
        self.pb.show()
        self.pb.update_bar(self)
        time.sleep(1)

        if self.login.exec_() == QDialog.Accepted:
            self.main_window.show()
            self.main_window.close_requested.connect(self.close_request)
            self.main_window.session_started.connect(self.session_start)
            self.splash.finish(self.main_window)

    @Slot()
    def close_request(self):
        print("Request for closure of app")

    @Slot()
    def session_start(self):
        self.main_wizard.show()
        print("Session start")






# class MainWindow(qw.QMainWindow):
#     """[summary]

#     Arguments:
#         qw {[type]} -- [description]
#     """

#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.ui_window = Ui_MainWindow()
#         self.ui_window.setupUi(self)



# if __name__ == "__main__":
#     import sys
#     import time

#     APP = qw.QApplication(sys.argv)

#     if LOGIN.exec_() == qw.QDialog.Accepted:
#         WINDOW = MainWindow()
#         WINDOW.show()
#         splash.finish(WINDOW)
#         sys.exit(APP.exec_())
