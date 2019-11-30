from Cifer.PrimeNumbers import Primes as Primes


MAX_PRIMES = 100000000


class SafePrimes:
    __size__ = 0
    __target_size__ = 0
    __primes__ = Primes(MAX_PRIMES)

    def __init__(self, size):
        self.__target_size__ = size

    def __iter__(self):
        for prime in self.__primes__:
            num = 2*prime + 1
            if self.__primes__.is_prime(num):
                self.__size__ += 1
                yield num

            if self.__size__ == self.__target_size__:
                break

