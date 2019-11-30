import math


class DiffieHellmanActor:
    name = ''
    __public_key__ = 0
    __secret_key__ = 0
    __modulus__ = 0
    __common_secret__ = 0

    def __init__(self, name, public, secret):
        self.name = name
        self.__public_key__ = public
        self.__secret_key__ = secret

    def __and__(self, other):   # and operator generates common secret key
        self.__modulus__ = (self.__public_key__ ** self.__secret_key__) % other.__public_key__
        other.__modulus__ = (self.__public_key__ ** other.__secret_key__) % other.__public_key__
        self.__generate_common_secret__(other.__modulus__, other.__public_key__)
        other.__generate_common_secret__(self.__modulus__, other.__public_key__)
        return self, other

    def __generate_common_secret__(self, modulus, public_key):
        self.__common_secret__ = (modulus ** self.__secret_key__) % public_key

    def __str__(self):
        return self.name + '{public key: ' + str(self.__public_key__) + '; secret key: ' + str(self.__secret_key__)\
               + "; own modulus: " + str(self.__modulus__) + '; generated common secret key: '\
               + str(self.__common_secret__) + '}'
