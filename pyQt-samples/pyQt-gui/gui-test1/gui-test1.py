# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets

from guitest_ui import Ui_MainWindow

class MainWindowClass(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

if (__name__ == "__main__"):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
