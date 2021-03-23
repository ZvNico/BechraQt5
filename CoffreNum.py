from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton
from PyQt5.QtCore import Qt

class CoffreNum(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coffre numérique")
        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.buttons = []
        for i in range(10):
            self.buttons.append(QPushButton(str(i)))
            self.layout.addWidget(self.buttons[i], 1 if i >= 5 else 0, i - (5 * (1 if i >= 5 else 0)),Qt.AlignmentFlag.AlignCenter)
        self.buttons.append(QPushButton('Ouvrir !'))
        self.layout.addWidget(self.buttons[-1],2,0,2,5)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)