from Cifer.Caesar import Caesar as Caesar
from Cifer.AntiCaesar import *
from Cifer.DiffieHellmanActor import DiffieHellmanActor as DHActor
from Cifer.PrimeNumbers import Primes
from Cifer.SafePrimes import SafePrimes
#from Cifer.SPR.Client import Client as SPR_Client
#from Cifer.SPR.Server import Server as SPR_Server
import Cifer.SPR


def cifer(cif, output_file): # cif should be iterable type's object
    f = open(output_file, 'w+')
    for line in cif:
        f.write(line)
    f.close()



