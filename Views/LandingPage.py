'''
Although it is titled the Landing page it is being treated more like the initial
Setup.  Luckily this is just a view so it is subject to change, the Developer can
always make a view called GameBoard (as an example) which inherits the BaseView
'''

import sys, os
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

sys.path.insert(0, '../Controllers')
sys.path.insert(1, '../Model')
sys.path.insert(2, '../Views')

import BaseView
import ButtonController
from CustomLabel import *
import PwdComplexController


class LandingPage(BaseView.BaseView):

    def __init__(self):
        super(LandingPage, self).__init__()
        self.ctrl = None
        self.components = []
        self.p = None
        self.p2 = None
        self.initUI()


    def initUI(self):

        self.p = QPixmap(os.getcwd() + '/images/DarkKnight_logo.png')

        # self.setGeometry(300, 300, 250, 150)
        # self.setWindowTitle('Password Complexity UI')
        # self.folderitems = QDockWidget("Enter Password", self)
        # self.fileitems = QDockWidget("Password Complexity", self)
        # self.pwdController = PwdComplexController.PwdComplexController(self)
        #
        # self.dockWidget1 = self.pwdController.progressBar
        # self.dockWidget2 = self.pwdController.pwdText
        #
        # self.fileitems.setWidget(self.dockWidget1)
        # self.fileitems.setFloating(False)
        #
        # self.folderitems.setWidget(self.dockWidget2)
        # self.folderitems.setFloating(False)
        #
        hbox = QHBoxLayout(self)
        #
        # splitter1 = QSplitter(self)
        # splitter1.setOrientation(Qt.Horizontal)
        #
        #
        # splitter2 = QSplitter(splitter1)
        # sizePolicy = splitter2.sizePolicy()
        # sizePolicy.setHorizontalStretch(1)
        #
        # splitter2.setSizePolicy(sizePolicy)
        # splitter2.setOrientation(Qt.Vertical)
        #
        # top_right = QFrame(splitter2)
        # top_right.setFrameShape(QFrame.StyledPanel)
        # splitter2.addWidget(self.fileitems)
        # #splitter2.addWidget(logo)
        # bottom_right = QFrame(splitter2)
        # bottom_right.setFrameShape(QFrame.StyledPanel)
        # splitter2.addWidget(self.folderitems)
        # splitter2.setGeometry(0,0,20,700)
        # #hbox.addWidget(splitter1)
        # #hbox.addWidget(top_right)
        self.m_label = QLabel(alignment=Qt.AlignCenter)
        self.m_label.setPixmap(self.p)
        self.m_label.setAttribute(Qt.WA_TranslucentBackground, True)
        hbox.addWidget(self.m_label)
        self.setGeometry(300, 300, 450, 450)
        #
        pallete = QPalette()
        pallete.setColor(QPalette.Background, Qt.gray)
        #  #pallete.setColor(QPalette.Background, Qt.green)
        self.setAutoFillBackground(True)
        self.setPalette(pallete)


        #self.show()
