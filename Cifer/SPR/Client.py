from Cifer.SPR.LoginTransfer import LoginTransfer as Login
from Cifer.SPR.SPR import *
import random


SALT_DIAP = (-10000000, 10000000)


class Client:
    __username__ = ''
    __salt__ = 0
    __safe_prime__ = 0

    def __init__(self, username):
        self.__username__ = username
        self.__salt__ = random.randint(SALT_DIAP[0], SALT_DIAP[1])
        self.__safe_prime__ = generate_safe_prime(SAFE_PRIME_DIAP)

    def login(self, server, password):
        login = Login(server, self)
        u = my_hash((login.public_key_A, login.public_key_B))
        if login.public_key_B == 0 or u == 0:
            print('From ' + self.__username__ + ': Logging failed! B == 0 or u == 0.')
            return
        x = my_hash((login.user_salt, password))
        session_key = (login.public_key_B - K*modulo_n(self.__safe_prime__)**x) ** (self.__private_key__ + u*x)
        myK = my_hash((session_key))

    def login_successful(self, server):
        print('From ' + server.name + ': ' + self.__username__ + ' logged successful!')

    def login_failed(self, server, desc):
        print('From ' + server.name + ': ' + self.__username__ + "'s logging failed!\nDescription: " + desc)

    def register(self, server, password):
        server.registration(self, password)

    def send_salt(self):
        return self.__salt__

    def send_username(self):
        return self.__username__

    __private_key__ = 0

    def __generate_private_key__(self):
        self.__private_key__ = generate_safe_prime(SAFE_PRIME_DIAP)

    def send_public_key(self):
        self.__generate_private_key__()
        return modulo_n(self.__safe_prime__)**self.__private_key__ % self.__safe_prime__


