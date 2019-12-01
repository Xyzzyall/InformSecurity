import random
import Cifer.SafePrimes


class RSAActor:
    name = ''

    def __init__(self, name):
        self.name = name

    def __iter__(self):
        pass

    def __and__(self, other):
        pass

    @staticmethod
    def reverse_prime(n):  # check for exponent
        fact_set = set()
        for i in range(2, n + 1):
            if (n % i == 0):
                n //= i
                fact_set.add(i)
        return fact_set

    @staticmethod
    def rev_prime_check(prime_one, prime_two):
        badnum_set1 = RSAActor.reverse_prime(prime_one)
        badnum_set2 = RSAActor.reverse_prime(prime_two)
        if len(badnum_set1.union(badnum_set2)) == len(badnum_set2) + len(badnum_set1):
            return True
        else:
            return False
