import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from classes import ClavierNum

if __name__ == '__main__':
    app = QCoreApplication.instance()
    app = QApplication(sys.argv)
    window = ClavierNum()
    window.show()
    app.exec_()
