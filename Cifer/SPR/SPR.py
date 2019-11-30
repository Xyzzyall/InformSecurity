import random
import Cifer

K = 3
SAFE_PRIME_DIAP = (1, 10)


def my_hash(objs):
    s = ''
    for obj in objs:
        s += str(obj)
    return abs(hash(s)) % 100


def modulo_n(n):
    return random.randint(2, n - 2)


def generate_safe_prime(diap: tuple):
    index = random.randint(diap[0], diap[1]-1)
    i = 0
    for prime in Cifer.SafePrimes(diap[1]):
        if i == index:
            return prime
        i += 1