import Cifer.SPR as SPR
import Cifer
import random


SALT_DIAP = (-10000000, 10000000)


class Client:
    __username__ = ''
    __salt__ = 0

    def __init__(self, username):
        self.__username__ = username
        self.__salt__ = random.randint(SALT_DIAP[0], SALT_DIAP[1])

    def login(self, server, password):
        pass

    def register(self, server, password):
        pass
