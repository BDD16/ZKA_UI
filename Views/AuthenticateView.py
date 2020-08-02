'''
Although it is titled the Landing page it is being treated more like the initial
Setup.  Luckily this is just a view so it is subject to change, the Developer can
always make a view called GameBoard (as an example) which inherits the BaseView
'''

import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Controllers import AuthController
from Model.CustomLabel import LoadingLabel
from Model.TextBoxes import SecretTextBox

sys.path.insert(0, '../Controllers')
sys.path.insert(1, '../Model')
sys.path.insert(2, '../Views')

from Views import BaseView
from CustomLabel import *


class AuthenticateView(BaseView.BaseView):

    def __init__(self):
        super(AuthenticateView, self).__init__()
        self.ctrl = None
        self.components = []
        self.p = None
        self.p2 = None

        self.initUI()

    def initUI(self):
        self.p = QPixmap(os.getcwd() + '/images/DarkKnight_logo.png')
        self.logo = QPixmap(os.getcwd() + '/images/1337_TECH_NEW_LOGO.png')
        hbox = QHBoxLayout(self)

        self.main_label = LoadingLabel(alignment=Qt.AlignCenter)
        self.main_label.setPixmap(self.p)
        self.main_label.setAttribute(Qt.WA_TranslucentBackground, True)

        self.passwordBox = SecretTextBox(self.main_label, text='password')
        self.usernameBox = SecretTextBox(self.main_label, text='username')
        self.usernameBox.move(self.main_label.size().width() + 50, 200)
        self.usernameBox.setStyleSheet('background-color: rgb(244,40,40); border-radius: 10;')

        self.passwordBox.setEchoMode(QLineEdit.Password)
        self.passwordBox.setStyleSheet('background-color: rgb(244,40,40); border-radius: 10;')
        self.passwordBox.move(self.main_label.size().width() + 50, 300)

        self.usernameBox.setFont(QFont("Helvetica", 14, QFont.ExtraBold))

        hbox.addWidget(self.main_label)

        self.controller = AuthController.AuthController(self)

        self.passwordBox.clicked.connect(self.controller.Authenticate)

        # self.show()
