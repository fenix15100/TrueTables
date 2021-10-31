import sys

from PySide6 import QtGui
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication,QPushButton,QLineEdit,QTextBrowser
from PySide6.QtCore import QFile, QIODevice


class QtUiLoader():

    def __init__(self):
        self.app = None
        self.windows = None
        self.loadUi()
        self.addAtom = self.windows.findChild(QPushButton, 'addAtom')
        self.atomos_input = self.windows.findChild(QLineEdit, 'atomos_input')
        self.list_atomos = self.windows.findChild(QTextBrowser, 'list_atomos')
        self.loadSlots_signals()


    def loadUi(self):
        self.app = QApplication(sys.argv)

        ui_file_name = "./app/ui/main.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        window = loader.load(ui_file)
        ui_file.close()
        if not window:
            print(loader.errorString())
            sys.exit(-1)
        self.windows = window

    def loadSlots_signals(self):
        self.addAtom.clicked.connect(self.OnClickAddAtoms)


    def OnClickAddAtoms(self):
        print("TUS MUERTOS")

        self.list_atomos.append(self.atomos_input.text())

