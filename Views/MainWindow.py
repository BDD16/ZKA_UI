"""
DBA 1337_TECH, AUSTIN TEXAS © July 2021
Proof of Concept code, No liabilities or warranties expressed or implied.
"""

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QMainWindow, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

from Model.Overlay import Overlay

sys.path.insert(0, '../Controllers')
sys.path.insert(1, '../Model')
sys.path.insert(2, '../Views')

import BaseView
import ButtonController
import LandingPage
import AuthenticateView


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ctrl = None
        self.components = []
        self.view = None
        self.initUI()

    def paintEvent(self, event=None):
        painter = QPainter(self)

        painter.setOpacity(0.01)
        painter.setBrush(Qt.white)
        painter.setPen(QPen(Qt.white))
        painter.drawRect(self.childrenRect())

    def initUI(self):
        self.view = LandingPage.LandingPage(window=self)
        self.view.initUI()
        # self.statusBar().showMessage('StatusBar:')
        self.setCentralWidget(self.view)

        self.setGeometry(0, 0, 250, 250)

        self.setWindowTitle('Complexity Calculator')

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        # self.setWindowOpacity(0.35)

        op = QGraphicsOpacityEffect(self.view)
        op.setOpacity(1.0)
        self.setGraphicsEffect(op)
        self.paintEvent()
        self.setStyleSheet("background-color: yellow;")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
