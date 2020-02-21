from PySide2.QtWidgets import QToolBar, QAction
class Toolbar(QToolBar):

    def __init__(self, toolbar_name: str, parent=None):
        super(Toolbar, self).__init__()
        self.setParent(parent)
        self.setObjectName(toolbar_name)
        self.button_action = QAction("FirstButton")
        self.button_action.setStatusTip("This is your first button")
        self.button_action.triggered.connect(self.onToolbarButtonClick)
        self.button_action.setCheckable(True)
        self.addAction(self.button_action)

    @classmethod
    def onToolbarButtonClick(cls, s):
        """Toolbar Click event

        Arguments:
            s {[type]} -- [description]
        """
        print("click", s)
