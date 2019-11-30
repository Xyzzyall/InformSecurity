import Cifer.SPR as SPR


class LoginTransfer:
    username = ''
    public_key_A = 0
    public_key_B = 0
    user_salt = 0

    def __init__(self, server: SPR.Server, client: SPR.Client):
        self.username = client.send_username()
        self.public_key_A = client.send_public_key()
        self.public_key_B = server.send_public_key()

