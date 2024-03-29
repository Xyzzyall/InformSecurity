import random
from typing import Any, Union

import Cifer

K = 3
SAFE_PRIME_DIAP = (5, 10)
mod_n = 7

'''def my_hash(objs):
    s = ''
    for obj in objs:
        s += str(obj)
    return abs(hash(s)) % 100'''


def my_hash(objs):
    res = 0
    for obj in objs:
        res += hash(obj) % 100
    return res


def modulo_n(n):
    #mod_n = random.randint(2, n - 2)
    return mod_n


def generate_safe_prime(diap: tuple):
    index = random.randint(diap[0], diap[1]-1)
    i = 0
    for prime in Cifer.SafePrimes(diap[1]):
        if i == index:
            return prime
        i += 1
