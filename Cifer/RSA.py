from Cifer.SafePrimes import SafePrimes
import random


class RSA:
    __public_key__ = 0
    __private_key__ = 0

    def __init__(self):
        primes = [prime for prime in SafePrimes(20)]
        n_prime = random.choice(primes)
        m_prime = random.choice(primes)

        modulus = n_prime * m_prime

        eiler_function = (n_prime - 1) * (m_prime - 1)

        open_exponent_vars = [i for i in primes if (i < eiler_function) and RSA.rev_prime_check(eiler_function, i)]
        open_exponent = random.choice(open_exponent_vars)

        self.__public_key__ = [open_exponent, modulus]

        d_list = []
        for i in range(1, 10000000):
            if (i * open_exponent) % eiler_function == 1:
                d_list.append(i)

        d_num = random.choice(d_list)
        self.__private_key__ = [d_num, modulus]

    def code(self, num):
        return (num ** self.__public_key__[0]) % self.__public_key__[1]

    def decode(self, num):
        return (num ** self.__private_key__[0]) % self.__private_key__[1]

    def __str__(self):
        return 'Public key=' + str(self.__public_key__) + '\nPrivate key=' + str(self.__private_key__)

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
        badnum_set1 = RSA.reverse_prime(prime_one)
        badnum_set2 = RSA.reverse_prime(prime_two)
        if len(badnum_set1.union(badnum_set2)) == len(badnum_set2) + len(badnum_set1):
            return True
        else:
            return False