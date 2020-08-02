import sys, os
from typing import Any

from Model import CryptoTools
from Model.ZeroKnowledgeAuth import ZeroKnowledgeAuthServer, modexp, ZeroKnowledgeAuthClient

sys.path.insert(0, '../Controllers')
sys.path.insert(1, '../Model')
sys.path.insert(2, '../Views')

from Controllers import BaseController
from Views import BaseView


class AuthController(BaseController.BaseController):

    def __init__(self, view: BaseView = None):
        super(AuthController, self).__init__(view)
        self.view = view


    def getUserName(self):
        self.username = self.view.usernameBox.text()

    def getPassword(self):
        self.password = self.view.passwordBox.text()

    def Authenticate(self):
        logo = ''' ____________ _________________  ___________           .__
        /_   \_____  \\_____  \______  \ \__    ___/___   ____ |  |__
         |   | _(__  <  _(__  <   /    /   |    |_/ __ \_/ ___\|  |  \\
         |   |/       \/       \ /    /    |    |\  ___/\  \___|   Y  \\
         |___/______  /______  //____/     |____| \___  >\___  >___|  /
                    \/       \/                       \/     \/     \/ '''
        print(logo)
        print("\n\n")
        print("Beginning Registration")
        import Crypto.Util.number
        gknot = 3

        p = 4074071952668972172536891376818756322102936787331872501272280898708762599526673412366794779

        #print(pow(gknot, 256))
        self.getUserName()
        self.getPassword()
        server = ZeroKnowledgeAuthServer()
        crypt = CryptoTools.CryptoTools()
        username = self.username
        x = crypt.Sha256(str(self.password).encode())
        Y = modexp(gknot, int.from_bytes(x, byteorder='little'), p)
        #server.registration(username, Y)
        a = server.SendSession()
        print('a: ' + str(a))
        client = ZeroKnowledgeAuthClient(username, crypt.Sha256(str(self.password).encode()),
                                         a)
        didweAuth = server.Authenticate(username, client.c, client.zx)
        print("Did we Authenticate: " + str(didweAuth))

        '''
        testpassword: thisIsNotThePasswordYouAreLookingFor
        '''