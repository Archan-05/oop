import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *
from PySide6.QtGui import *

app = QApplication(sys.argv)
loader = QUiLoader()

dig = loader.load("student.ui", None)

def MenuOpenClicked():
    print("Clicked")

def MenuExit():
    c = QMessageBox()
    c.setText("แน่ใจว่าจะออกไหม?")
    c.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
    c = c.exec()
    if c == QMessageBox.Yes:
        app.quit()

def mainFrom(w):
    w.setWindowTitle("My Student")
    icon = QIcon("icon.png")
    w.setWindowIcon(icon)

dig .actionOpen.triggered.connect(MenuOpenClicked)
dig .actionExit.triggered.connect(MenuExit)
mainFrom(dig)
dig.show()
sys.exit(app.exec())