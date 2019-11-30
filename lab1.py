import Cifer

KEY = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
reference = 'Refs/test.txt'
result_dir = 'lab1_out/'

Cifer.cifer(Cifer.Caesar(reference, 1), result_dir+'out_test.txt')

orig_chr_fr = Cifer.char_frequency(reference)
coded_chr_fr = Cifer.char_frequency(result_dir+'out_test.txt')
key = Cifer.find_a_caesar_key(orig_chr_fr, coded_chr_fr)
print(key)

Cifer.caesar_decifer(result_dir + 'out_test.txt', result_dir + 'out_decoded_test.txt', key)


orig_chr_fr = Cifer.char_frequency(reference, bigramm=True)
coded_chr_fr = Cifer.char_frequency(result_dir+'out_test.txt', bigramm=True)
key = Cifer.find_a_caesar_key(orig_chr_fr, coded_chr_fr)
print(key)

Cifer.caesar_decifer(result_dir + 'out_test.txt', result_dir + 'out_decoded_bigram_test.txt', key)
