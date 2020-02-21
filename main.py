from qtrainer.app import App
from PySide2.QtCore import QFile, QTextStream
from qtrainer.themes import breeze_resources


if __name__ == '__main__':
    import sys
    APP = App()

    file = QFile(":/dark.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    APP.setStyleSheet(stream.readAll())
    sys.exit(APP.exec_())
