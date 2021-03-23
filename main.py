import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from classes import CoffreNum

if __name__ == '__main__':
    app = QCoreApplication.instance()
    app = QApplication(sys.argv)
    window = CoffreNum()
    window.show()
    app.exec_()
