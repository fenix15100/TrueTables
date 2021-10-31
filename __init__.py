import sys

from PySide6.QtWidgets import QApplication

from app.include.TruetableGenerator import TruetableGenerator
from app.controller.MainWindowsController import MainWindowController
TruetableGenerator(atoms=['a', 'b'], premises=['not a']).__str__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowController()
    window.show()
    sys.exit(app.exec())
