import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.show()  # IMPORTANT! Les fenêtres sont invisibles sinon
app.exec_()
