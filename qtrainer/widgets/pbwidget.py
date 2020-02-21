import time
from PySide2.QtWidgets import QProgressBar, QApplication
from PySide2.QtGui import QPixmap


class PbWidget(QProgressBar):

    def __init__(self, reference_image: QPixmap, total=20, parent=None):
        super(PbWidget, self).__init__()
        self.setMinimum(1)
        self.setMaximum(total)
        self._active = False
        self.setGeometry(0, reference_image.height() - 50, reference_image.height(), 20)
        self.setParent(parent)

    def update_bar(self, application: QApplication):
        """Updates Progress Bar
        Arguments:
            application {PySide2.QtWidgets.QApplication} --
            manages the GUI application's control flow and main settings
        """
        for i in range(1, 21):
            self.setValue(i)
            t = time.time()
            while time.time() < t + 0.1:
                application.processEvents()
