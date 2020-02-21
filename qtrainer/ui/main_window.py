from PySide2.QtWidgets import QMainWindow, QAction, QLabel, QToolBar, \
     QStatusBar, QVBoxLayout, QWidget
from PySide2.QtCore import Signal, Slot

class MainWindow(QMainWindow):
    session_started = Signal(str)
    close_requested = Signal()
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Spiral Training")
        layout = QVBoxLayout()
        emptyWidget = QWidget()
        layout.addWidget(emptyWidget)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setGeometry(200, 200, 800, 800)
        self.button_action = QAction("Open Wizard")
        self.button_action.setStatusTip("Open the wizarddddd")
        self.button_action.triggered.connect(self.on_button_clicked)

        self.exit_action = QAction("Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(self.close_request)
        self._createMenu()
        self._createToolbar()
        self._createStatusbar()


        # Exit QAction
        # self.file_menu.addAction(exit_action)

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")

        self.menu.addAction('&Exit', self.close)

    def _createToolbar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction(self.button_action)

    def _createStatusbar(self):
        status = QStatusBar()
        status.showMessage("I'm the status bar")
        self.setStatusBar(status)

    @Slot()
    def on_button_clicked(self):
        """
        on_button_clicked [summary]
        """
        self.session_started.emit("Session Started")
        print("Session started")

    @Slot()
    def close_request(self):
        self.close_requested.emit()
