#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author Frank
# @date 2021/10/13
# @file test.py
from main import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # 设置窗口窗口风格
    QApplication.setStyle(QStyleFactory.create("Fusion"))
    print(QStyleFactory.keys())
    ui = MainWindow()
    ui.show()
    # sys.exit(app.exec_())
    app.exec_()