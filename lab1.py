import Cifer

KEY = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

Cifer.cifer(Cifer.Caesar('test.txt', 1), 'out_test.txt')

orig_chr_fr = Cifer.char_frequency('test.txt')
coded_chr_fr = Cifer.char_frequency('out_test.txt')
key = Cifer.find_a_caesar_key(orig_chr_fr, coded_chr_fr)
print(key)

Cifer.decifer('out_test.txt', 'out_decoded_test.txt', key)


orig_chr_fr = Cifer.char_frequency('test.txt', bigramm=True)
coded_chr_fr = Cifer.char_frequency('out_test.txt', bigramm=True)
key = Cifer.find_a_caesar_key(orig_chr_fr, coded_chr_fr)
print(key)

Cifer.decifer('out_test.txt', 'out_decoded_bigram_test.txt', key)
