#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author Frank
# @date 2021/10/12
# @file index.py
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys

ui, _ = loadUiType('main.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


def main():
    app = QApplication([])
    # 设置窗口窗口风格
    QApplication.setStyle(QStyleFactory.create("Fusion"))
    print(QStyleFactory.keys())
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
