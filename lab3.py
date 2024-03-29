import Cifer
import random


primes = [prime for prime in Cifer.SafePrimes(10)]
q_prime = random.choice(primes)
n_prime = 2 * q_prime + 1

g_list = [i for i in range(2, n_prime - 2)]
g_modulus = random.choice(g_list)

k = 3

#Клиент
password = int(input('Пароль при регистрации = '))
salt = random.choice(range(1,10000))
x = hash(salt + password)
verifier = g_modulus ** x % n_prime

print('Пароль пользователя:', password)
print('Соль пользователя:', salt)
print('Хэш от соли и пароля:', x)

X = g_modulus ** x % n_prime
if isinstance(X, int):
    valid_X = X

user = 'username'
a = random.choice(range(1,10000))
full_A = g_modulus ** a % n_prime

if full_A != 0:
    print('A != 0. Проверка на сервере прошла успешно.')
    b = random.choice(range(1,100))
    full_B = (k * verifier + g_modulus ** b % n_prime) % n_prime
    server_answer = [salt, full_B]
else:
    print('Проверка на стороне сервера не прошла! А = 0 :(')

if server_answer[1] != 0:
    client_answer = True

server_scrambler = hash(full_A + server_answer[1])
client_scrambler = hash(full_A + server_answer[1])

if server_scrambler != client_scrambler and client_answer:
    print('Соединение с сервером прервано!')
else:
    print('Соединение с сервером прошло успешно!')

new_x = hash(salt + int(input("Введите пароль=")))

session_key_client = ((full_B - k * (g_modulus ** new_x % n_prime)) ** (a + client_scrambler * new_x)) % n_prime
session_key_server = ((full_A * (verifier ** server_scrambler % n_prime)) ** b) % n_prime

session_key_hash_client = hash(session_key_client)
session_key_hash_server = hash(session_key_server)

if session_key_hash_client == session_key_hash_server:
    print('Первая проверка прошла успешно!')
else:
    print('Первая проверка провалилась!')

hash_for_m = bool(hash(n_prime)) != (hash(g_modulus))

match_client = hash(hash_for_m + hash(user) + salt + full_A + full_B + session_key_hash_client)
match_server = hash(hash_for_m + hash(user) + salt + full_A + full_B + session_key_hash_server)

if match_client == match_server:
    print('Вторая проверка прошла успешно!')
    return_server = hash(full_A + match_server + session_key_hash_server)
    answer_client = hash(full_A + match_client + session_key_hash_client)
    if return_server == answer_client:
        print('Авторизация прошла успешно!')
    else:
        print('Авторизация не удалась!')
else:
    print('Вторая попытка проверки провалилась!')



"""import Cifer


site = Cifer.SPR.Server('shmail.ru')

evgeniy = Cifer.SPR.Client('onejka228')
tatyana = Cifer.SPR.Client('larina2000')

evgeniy.register(site, 'ilovetatyana')
tatyana.register(site, 'onegindebil')

print(str(site))

evgeniy.login(site, 'ilovetatyana')
"""