import Cifer.SPR as SPR
import random


SALT_DIAP = (-10000000, 10000000)


class Client:
    __username__ = ''
    __salt__ = 0
    __safe_prime__ = 0

    def __init__(self, username):
        self.__username__ = username
        self.__salt__ = random.randint(SALT_DIAP[0], SALT_DIAP[1])
        self.__safe_prime__ = SPR.generate_safe_prime(SPR.SAFE_PRIME_DIAP)

    def login(self, server, password):
        server.login(self)

    def register(self, server: SPR.Server, password):
        server.registration(self, password)

    def send_salt(self):
        return self.__salt__

    def send_username(self):
        return self.__username__

    def send_public_key(self):
        return SPR.modulo_n(self.__safe_prime__)**self.__private_key__

    __private_key__ = 0

    def __generate_private_key__(self):
        self.__private_key__ = SPR.generate_safe_prime(SPR.SAFE_PRIME_DIAP)

