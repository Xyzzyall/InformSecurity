from Cifer.SPR.Client import Client as Client
from Cifer.SPR.LoginTransfer import LoginTransfer as Login
from Cifer.SPR.SPR import *


class Server:
    name = ''
    __accounts__ = {}
    __safe_prime__ = 0

    def __init__(self, name):
        self.name = name
        self.__safe_prime__ = generate_safe_prime(SAFE_PRIME_DIAP)

    def registration(self, client, password):
        username = client.send_username()
        salt = client.send_salt()
        private_key = my_hash((salt, password))
        self.__accounts__[username] = Account(username, salt, password_verifier)

    def login(self, client: Client, login: Login, M, K):
        u = my_hash((login.public_key_A, login.public_key_B))
        if login.public_key_A == 0:
            client.login_failed(self, 'A == 0')
            return
        session_key = (login.public_key_A*self.__accounts__[login.username].pass_verifier**u)**self.__private_key__
        server_K = my_hash((session_key))
        if server_K == K:
            client.login_successful(self)
        else:
            client.login_failed(self, 'your key is ' + str(K) + ', but mine is ' + str(server_K))

    def __str__(self):
        res = self.name + ': safe_prime=' + str(self.__safe_prime__) + '\nAccounts:\n'
        for acc in self.__accounts__.values():
            res += str(acc) + '\n'
        return res

    __private_key__ = 0

    def __generate_private_key__(self):
        self.__private_key__ = generate_safe_prime(SAFE_PRIME_DIAP)

    def send_public_key(self):
        self.__generate_private_key__()
        return modulo_n(self.__safe_prime__)**self.__private_key__ % self.__safe_prime__

    def send_user_salt(self, username):
        return self.__accounts__[username].salt


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
