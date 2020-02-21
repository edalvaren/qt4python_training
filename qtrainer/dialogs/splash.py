# """
# Splash Screen for application

# Erick Alvarenga (erick@alfignetworking.com)
# License: Licensed under the GPLv3
# """
from PySide2.QtWidgets import QSplashScreen
from PySide2.QtGui import QPixmap



class Splash(QSplashScreen):
    def __init__(self, splash_pix: QPixmap):
        super(Splash, self).__init__(pixmap=splash_pix)
        self.setEnabled(False)
