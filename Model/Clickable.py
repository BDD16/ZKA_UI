"""
DBA 1337_TECH, AUSTIN TEXAS © July 2021
Proof of Concept code, No liabilities or warranties expressed or implied.
"""

'''
Turns a non clickable object such as a label into a clickable object
'''
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
sys.path.insert(0, '../Controllers')
sys.path.insert(1, '../Model')
sys.path.insert(2, '../Views')

def clickable(widget):

    class Filter(QObject):
        keyPressed = pyqtSignal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QEvent.MouseButtonReleased:
                    print("KeyReleased")
                    self.keyPressed.emit()
                    return True


            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.keyPressed
