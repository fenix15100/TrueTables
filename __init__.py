import sys
from app.include.TruetableGenerator import TruetableGenerator
from app.controller.QtUiLoader import QtUiLoader
TruetableGenerator(atoms=['a', 'b'], premises=['not a']).__str__()

if __name__ == "__main__":
    application = QtUiLoader()
    application.windows.show()
    sys.exit(application.app.exec())
