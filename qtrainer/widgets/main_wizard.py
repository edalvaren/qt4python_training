from PySide2.QtWidgets import QWizard, QWizardPage, QVBoxLayout, QLabel
from PySide2.QtGui import QPixmap


class MainWizard(QWizard):

    def __init__(self, parent=None):
        super(MainWizard, self).__init__(parent)


        self.addPage(IntroPage())
        self.addPage(Page2())
        self.banner_pixmap = QPixmap("resources/img/technology.jpg")
        self.setPixmap(self.BannerPixmap, self.banner_pixmap)


class IntroPage(QWizardPage):
    def __init__(self, parent=None):
        super(IntroPage, self).__init__(parent)

        self.setTitle("Introduction")
        self.setPixmap(QWizard.WatermarkPixmap, QPixmap('resources/img/ilox.png'))
        label = QLabel("This wizard will guide you through a spiral commissioning process")
        label.setWordWrap(True)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


class Page2(QWizardPage):
    def __init__(self, parent=None):
        super(Page2, self).__init__(parent)
        self.label1 = QLabel()
        self.label2 = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)

    def initializePage(self):
        self.label1.setText("This is my label")
        self.label2.setText("My second label")
