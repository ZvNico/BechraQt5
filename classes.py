from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt


class Message(QMessageBox):
    def __init__(self, controller, text):
        self.controller = controller
        super().__init__()
        self.setText(text)
        self.setStandardButtons(QMessageBox.Ok)
        self.buttonClicked.connect(self.close)
        self.exec()

    def close(self):
        self.controller.close()

    def closeEvent(self, event):
        """
        override closeEvent from QMessageBox from Qwidget
        """
        self.close()


class ClavierNum(QMainWindow):
    def __init__(self):
        super().__init__()
        self.code = [1, 2, 4, 5]
        self.input = []
        self.msg = "salut à tous les amis, vos grands mères les tricératops !"
        self.setWindowTitle("Coffre numérique")
        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.buttons = []
        for i in range(10):
            self.buttons.append(QPushButton(str(i)))
            self.buttons[i].connect(lambda x: self.numkeydown(i))
            self.layout.addWidget(self.buttons[i], 1 if i >= 5 else 0, i - (5 * (1 if i >= 5 else 0)), Qt.AlignmentFlag.AlignCenter)
        self.buttons.append(QPushButton('Ouvrir !'))
        self.buttons[-1].clicked.connect(self.openmsg)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.layout.addWidget(self.buttons[-1], 2, 0, 2, 5)

    def numkeydown(self, i):
        print(i)

    def openmsg(self):
        Message(self, self.msg)
