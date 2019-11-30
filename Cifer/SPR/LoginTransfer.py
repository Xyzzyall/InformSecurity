class LoginTransfer:
    username = ''
    public_key_A = 0
    public_key_B = 0
    user_salt = 0

    def __init__(self, server, client):
        self.username = client.send_username()
        self.public_key_A = client.send_public_key()
        self.public_key_B = server.send_public_key()
        self.user_salt = server.send_user_salt(self.username)
        print(server.name + ': Logging ' + self.username + ' in process...')
        print('keys:\nA= ' + str(self.public_key_A) + '\nB= ' + str(self.public_key_B))
