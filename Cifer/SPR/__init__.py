import random


K = 3


def my_hash(objs):
    s = ''
    for obj in objs:
        s += str(obj)
    return hash(s)


def modulo_n(n):
    return random.choice([i for i in range(2, n - 2)])
