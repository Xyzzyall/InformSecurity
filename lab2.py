import Cifer
import random


safe_primes = [i for i in Cifer.SafePrimes(100)]

evgeniy = Cifer.DHActor('Evgeniy Onegin', safe_primes[10], random.choice(safe_primes))
tatyana = Cifer.DHActor('Tatyana Larina', safe_primes[11], random.choice(safe_primes))

print(evgeniy)
print(tatyana)
print()

evgeniy, tatyana = evgeniy & tatyana

print(evgeniy)
print(tatyana)
