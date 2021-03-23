from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from random import randint


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


class CoffreNum(QMainWindow):
    def __init__(self):
        super().__init__()
        self.code = []
        temp = 0
        for i in range(4):
            num = randint(temp, 6 + i)
            self.code.append(num)
            temp = num

        self.input = []
        self.msg = "salut à tous les amis, vos grands mères les tricératops !"
        self.setWindowTitle("Coffre Numérique")
        self.codevalide = False

        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.clavier = []
        nums = [i for i in range(10)]
        for i in range(10):
            num = nums.pop(randint(0, len(nums) - 1))
            button = QPushButton(str(num))
            self.clavier.append(button)
            button.clicked.connect(self.numkeydown)
            self.layout.addWidget(button, 1 if i >= 5 else 0, i - (5 * (1 if i >= 5 else 0)))

        self.ouvrir = QPushButton('Ouvrir !')
        self.ouvrir.clicked.connect(self.openmsg)
        p = self.ouvrir.palette()
        p.setColor(self.ouvrir.backgroundRole(), Qt.green)
        self.ouvrir.setPalette(p)
        self.layout.addWidget(self.ouvrir, 2, 0, 2, 5)

        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(self.layout)

        print(self.code)

    def numkeydown(self):
        button = self.sender()
        self.input.append(int(button.text()))

        if len(self.input) >= 4:
            if len(self.input) > 4: del self.input[0]

            # vérification du code, algo avec une complexité exponentielle mais la dimension est fixe donc c'est négligeable
            # remarque : cela aurait été plus optimisé et propre de le faire dans une fonction dédié mais on a préferer centraliser
            temp = []
            for i in range(4):
                trouver = False
                for j in range(4):
                    if j not in temp:
                        if self.input[i] == self.code[j]:
                            temp.append(j)
                            trouver = True
                            break
                if not trouver:
                    break

            if len(temp) == 4:
                self.codevalide = True
                self.ouvrir.setAutoFillBackground(True)
            else:
                self.codevalide = False
                self.ouvrir.setAutoFillBackground(False)

    def openmsg(self):
        if self.codevalide:
            Message(self, self.msg)
