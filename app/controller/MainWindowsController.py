from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QMainWindow
from app.ui.Ui_MainWindows import Ui_MainWindow
from app.include.TruetableGenerator import TruetableGenerator


class MainWindowController(QMainWindow):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadSlots_signals()
        self.trueTableData = None

    def loadSlots_signals(self):
        self.ui.addAtom.clicked.connect(self.OnClickAddAtoms)
        self.ui.addPremisa.clicked.connect(self.OnClickAddPremisa)
        self.ui.generateTable.clicked.connect(self.OnClickgenerateTable)


    def OnClickAddAtoms(self):
        self.ui.list_atomos.append(self.ui.atomos_input.text())
        self.ui.atomos_input.setText("")

    def OnClickAddPremisa(self):
        self.ui.list_premisas.append(self.ui.premisas_input.text())
        self.ui.premisas_input.setText("")

    def OnClickgenerateTable(self):
        self.ui.TabPane.setCurrentIndex(1)
        atoms = self.ui.list_atomos.toPlainText().split("\n")
        premisas = self.ui.list_premisas.toPlainText().split("\n")
        self.trueTableData = TruetableGenerator(atoms=atoms, premises=premisas).table
        print(type(self.trueTableData))
        table = self.ui.tableWidget
        table.setRowCount(len(self.trueTableData))
        table.setColumnCount(len(atoms)+len(premisas))
        table.setHorizontalHeaderLabels([x for x in atoms+premisas])