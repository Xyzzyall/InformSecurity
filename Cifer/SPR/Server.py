import Cifer.SPR as SPR
import Cifer


class Server(Cifer.DHActor):
    __passwords__ = []

    def registration(self, client, ):
        pass

class Account:
    username = ''
    salt = ''
    pass_verifier = ''

    def __init__(self, username, salt, pass_verifier):
        self.username = username
        self.salt = salt
        self.pass_verifier = pass_verifier

