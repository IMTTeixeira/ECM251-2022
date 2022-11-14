# Luan Teixeira         R.A: 20.01681-6

from models.user import User


class UserController():
    def __init__(self) -> None:
        #Carrega os dados dos usuários
        self.users = [
            User(nome="Zed", password="deathmark", email="zed@mail.com"),
            User(nome="Kayn", password="umbral", email="kayn@mail.com"),
            User(nome="Syndra", password="power", email="syndra@mail.com"),
        ]
    def checkUser(self,user):
        return user in self.users

    def checkLogin(self, nome, password):
        user_checker = User(nome=nome, password=password, email=None)
        for user in self.users:
            if user.nome == user_checker.nome and user.password == user_checker.password:
                
                return True           
        return False
    
    