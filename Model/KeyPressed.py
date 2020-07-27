'''
Turns a non clickable object such as a label into a clickable object
'''
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def KeyPressed(widget):

    class Filter(QObject):
        keyPressed = pyqtSignal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QEvent.KeyRelease:
                    print("KeyReleased")
                    self.keyPressed.emit()
                    return True


            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.keyPressed
