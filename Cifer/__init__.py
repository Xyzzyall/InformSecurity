from Cifer.Caesar import Caesar as Caesar
from Cifer.AntiCaesar import *
from Cifer.DiffieHellmanActor import DiffieHellmanActor as DHActor


def cifer(cif, output_file): # cif should be iterable type's object
    f = open(output_file, 'w+')
    for line in cif:
        f.write(line)
    f.close()



