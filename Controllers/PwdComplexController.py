"""
DBA 1337_TECH, AUSTIN TEXAS © July 2021
Proof of Concept code, No liabilities or warranties expressed or implied.
"""

import sys, os
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

sys.path.insert(0, '../Controllers')
sys.path.insert(1, '../Model')
sys.path.insert(2, '../Views')

from PyQt5.QtCore import *
import BaseController
import ProgressBarCustom
import ComplexityEngine


class PwdComplexController(BaseController.BaseController):

    def __init__(self, view):
        super(PwdComplexController,self).__init__(view)
        self.progressBar = ProgressBarCustom.ProgressBarCustom(view)
        self.pwdText = QTextEdit("EnterPassword", view)
        self.pwdText.setGeometry(200,80,250,20)
        self.view = view
        self.clicks = 0
        self.progress = 0
        self.engine = ComplexityEngine.ComplexityEngine()
        self.init()

    def init(self):
        KeyPressed(self.pwdText, self.calc)

    def calc(self):
        self.progressBar.setProgress(self.engine.CalculatePwdCompelxity())
        self.engine.L = len(self.pwdText.toPlainText())
        self.progressBar.show()
        return


def KeyPressed(widget, function):

    class Filter(QObject):
        keyPressed = pyqtSignal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QEvent.KeyRelease:
                    print("KeyReleased")
                    function()
                    self.keyPressed.emit()
                    return True


            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.keyPressed
