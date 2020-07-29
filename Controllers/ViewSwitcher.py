import sys, os
from typing import Any

sys.path.insert(0, '../Controllers')
sys.path.insert(1, '../Model')
sys.path.insert(2, '../Views')

from Controllers import BaseController
from Views import BaseView
from Views.AuthenticateView import AuthenticateView


class ViewSwitcher(BaseController.BaseController):

    def __init__(self, view: BaseView = None):
        super(ViewSwitcher, self).__init__(view)
        self.view = view
        #self.view.m_label.clicked.connect(self.SwitchOnclick)

    def SwitchOnClick(self):
        newView = AuthenticateView()
        self.view.mw.setCentralWidget(newView)

        print("MADE IT TO SWITCHONECLICK, END")
        self.view.mw.show()
