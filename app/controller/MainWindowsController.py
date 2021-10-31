from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QMainWindow
from app.ui.Ui_MainWindow import Ui_MainWindow


class MainWindowController(QMainWindow):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadSlots_signals()

    def loadSlots_signals(self):
        self.ui.addAtom.clicked.connect(self.OnClickAddAtoms)

    def OnClickAddAtoms(self):
        self.ui.list_atomos.append(self.ui.atomos_input.text())
