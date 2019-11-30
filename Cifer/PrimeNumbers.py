class Primes:
    size = 0

    def __init__(self, size):
        self.size = size

    __primes__ = []
    __num__ = 2

    def __iter__(self):
        while len(self.__primes__) < self.size:
            if self.is_prime(self.__num__):
                self.__primes__.append(self.__num__)
                yield self.__num__
            self.__num__ += 1

    def is_prime(self, num):
        for prime in self.__primes__:
            if num != prime and num % prime == 0:
                return False
        return True

    def __str__(self):
        return str(self.__primes__)