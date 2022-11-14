# Luan Teixeira         R.A: 20.01681-6

class Usuario():
    def __init__(self,nome ,email, password) -> None:
        self.nome = nome
        self.email = email
        self.password = password
    def __str__(self) -> str:
        return f'User(nome:{self.nome}, email:{self.email}, password:{self.password})'

    def getnome(self):
        return self.nome