from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLineEdit


class SecretTextBox(QLineEdit):
    clicked = pyqtSignal()

    def __init__(self, parent=None, **kwargs):
        super(SecretTextBox, self).__init__(parent, **kwargs)
        s = self.size()
        print(self.size())
        print(parent.size())
        print(self.geometry())
        self.setGeometry(parent.width() / 2 - s.width() / 2,
                         parent.height() / 2 - s.height() / 2,
                         s.width(),
                         s.height()
                         )

    def mousePressEvent(self, ev):
        self.clicked.emit()
