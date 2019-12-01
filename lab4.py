import Cifer


rsa = Cifer.RSA()

print(rsa)

message = int(input('Type a message: '))

crypted = rsa.code(message)
print('Coded message=' + str(crypted))

decrypted = rsa.decode(crypted)
print('Decoded message=' + str(decrypted))
