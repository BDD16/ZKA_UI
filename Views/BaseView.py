"""
DBA 1337_TECH, AUSTIN TEXAS © July 2021
Proof of Concept code, No liabilities or warranties expressed or implied.
"""

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt

me = '[BaseView]'
class BaseView(QWidget):

    def __init__(self):
        super(BaseView, self).__init__()
        self.components = []


    def initUI(self):

        print (me + 'this is in the Baseview initUI')
