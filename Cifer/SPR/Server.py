import Cifer.SPR as SPR
import Cifer


class Server:
    name = ''
    __accounts__ = {}
    __safe_prime__ = 0

    def __init__(self, name):
        self.name = name
        self.__safe_prime__ = SPR.generate_safe_prime(SPR.SAFE_PRIME_DIAP)

    def registration(self, client, password):
        username = client.send_username()
        salt = client.send_salt()
        private_key = SPR.my_hash((salt, password))
        password_verifier = SPR.modulo_n(self.__safe_prime__)**private_key
        self.__accounts__[username] = Account(username, salt, password_verifier)

    def login(self, client):
        pass

    def __str__(self):
        res = self.name + ': safe_prime=' + str(self.__safe_prime__) + '\nAccounts:\n'
        for acc in self.__accounts__.values():
            res += str(acc) + '\n'
        return res

    __private_key__ = 0

    def __generate_private_key__(self):
        self.__private_key__ = SPR.generate_safe_prime(SPR.SAFE_PRIME_DIAP)

    def send_public_key(self):
        return SPR.modulo_n(self.__safe_prime__)**self.__private_key__


class Account:
    username = ''
    salt = 0
    pass_verifier = 0

    def __init__(self, username, salt, pass_verifier):
        self.username = username
        self.salt = salt
        self.pass_verifier = pass_verifier

    def __str__(self):
        return self.username + ': salt=' + str(self.salt) + '; password_verifier=' + str(self.pass_verifier)
