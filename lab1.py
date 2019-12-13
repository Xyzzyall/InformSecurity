import Cifer

KEY = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
reference = 'Refs/test1.txt'
result_dir = 'lab1_out/'
key_reference = 'Refs/VoinaAndPeace_.txt'
key_filter = KEY + KEY.upper()

Cifer.cifer(Cifer.Caesar(reference, 13), result_dir+'out_test.txt')

orig_chr_fr = Cifer.char_frequency(reference, filt=key_filter)
coded_chr_fr = Cifer.char_frequency(result_dir+'out_test.txt', filt=key_filter)
key = Cifer.find_a_caesar_key(orig_chr_fr, coded_chr_fr)
print(key)

Cifer.caesar_decifer(result_dir + 'out_test.txt', result_dir + 'out_decoded_test.txt', key)


orig_chr_fr = Cifer.char_frequency(reference, bigramm=True)
coded_chr_fr = Cifer.char_frequency(result_dir+'out_test.txt', bigramm=True)
key = Cifer.find_a_caesar_key(orig_chr_fr, coded_chr_fr)
print(key)

Cifer.caesar_decifer(result_dir + 'out_test.txt', result_dir + 'out_decoded_bigram_test.txt', key)
