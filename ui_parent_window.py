# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_parent_window.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 483)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSave_Progress = QAction(MainWindow)
        self.actionSave_Progress.setObjectName(u"actionSave_Progress")
        self.actionSave_and_Exit = QAction(MainWindow)
        self.actionSave_and_Exit.setObjectName(u"actionSave_and_Exit")
        self.actionSaved_Session = QAction(MainWindow)
        self.actionSaved_Session.setObjectName(u"actionSaved_Session")
        self.actionTraining_Session = QAction(MainWindow)
        self.actionTraining_Session.setObjectName(u"actionTraining_Session")
        self.actionWindow = QAction(MainWindow)
        self.actionWindow.setObjectName(u"actionWindow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.progressBar_main = QProgressBar(self.centralwidget)
        self.progressBar_main.setObjectName(u"progressBar_main")
        self.progressBar_main.setAutoFillBackground(False)
        self.progressBar_main.setValue(1)

        self.gridLayout.addWidget(self.progressBar_main, 7, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 845, 34))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSave = QMenu(self.menuFile)
        self.menuSave.setObjectName(u"menuSave")
        self.menuOpen = QMenu(self.menuFile)
        self.menuOpen.setObjectName(u"menuOpen")
        self.menuNew = QMenu(self.menuFile)
        self.menuNew.setObjectName(u"menuNew")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuSave.addAction(self.actionSave_Progress)
        self.menuSave.addAction(self.actionSave_and_Exit)
        self.menuNew.addAction(self.actionTraining_Session)
        self.menuNew.addAction(self.actionWindow)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSave_Progress.setText(QCoreApplication.translate("MainWindow", u"Save Progress", None))
        self.actionSave_and_Exit.setText(QCoreApplication.translate("MainWindow", u"Save and Exit", None))
        self.actionSaved_Session.setText(QCoreApplication.translate("MainWindow", u"Saved Session", None))
        self.actionTraining_Session.setText(QCoreApplication.translate("MainWindow", u"Training Session", None))
        self.actionWindow.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Click to continue", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuOpen.setTitle(QCoreApplication.translate("MainWindow", u"Open", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"New", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

