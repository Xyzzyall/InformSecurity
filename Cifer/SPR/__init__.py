import random
import Cifer
from Cifer.SPR.Server import Server as Server
from Cifer.SPR.Client import Client as Client


K = 3
SAFE_PRIME_DIAP = (100, 200)


def my_hash(objs):
    s = ''
    for obj in objs:
        s += str(obj)
    return hash(s)


def modulo_n(n):
    return random.choice([i for i in range(2, n - 2)])


def generate_safe_prime(diap: tuple):
    index = random.randint(diap[0], diap[1])
    i = 0
    for prime in Cifer.SafePrimes(diap[1]):
        if i == index:
            return prime
        i += 1
