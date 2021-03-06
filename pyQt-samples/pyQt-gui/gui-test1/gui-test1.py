# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

import os, sys
from guitest_ui import Ui_MainWindow

class MainWindowClass(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon(os.path.abspath('./logo.png')))
        self.pushButton_start.clicked.connect(lambda:self.clicked_pushbutton(self.pushButton_start))
        
        image_path = os.path.abspath('./company_ icon.png')
        scene = QtWidgets.QGraphicsScene(MainWindow)
        pixmap = QPixmap(image_path)
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.graphicsView.setScene(scene)        
        
    def clicked_pushbutton(self, btn):
        msg = 'Button clicked --> "%s".\n' % (btn.text())
        self.textBrowser_status.setText(self.textBrowser_status.toPlainText() + msg)

if (__name__ == "__main__"):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
