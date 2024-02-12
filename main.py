import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_main_window import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())