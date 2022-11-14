# Luan Teixeira         R.A: 20.01681-6

from models.usuario import Usuario


class UserController():
    def __init__(self) -> None:
        #Carrega os dados dos usuários
        self.usuarios = [
            Usuario(nome="Zed", password="deathmark", email="zed@mail.com"),
            Usuario(nome="Kayn", password="umbral", email="kayn@mail.com"),
            Usuario(nome="Syndra", password="power", email="syndra@mail.com"),
        ]
    def checkUser(self,usuario):
        return usuario in self.usuarios

    def checkLogin(self, nome, password):
        user_checker = Usuario(nome=nome, password=password, email=None)
        for usuario in self.usuarios:
            if usuario.nome == user_checker.nome and usuario.password == user_checker.password:
                
                return True           
        return False
    
    