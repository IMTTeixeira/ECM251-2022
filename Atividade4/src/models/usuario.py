# Luan Teixeira         R.A: 20.01681-6

class Usuario():
    def __init__(self,nome ,email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha
    def __str__(self) -> str:
        return f'User(nome:{self.nome}, email:{self.email}, password:{self.senha})'

    def getnome(self):
        return self.nome