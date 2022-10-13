# Luan Teixeira         R.A: 20.01681-6

from models.user import User


class UserController():
    def __init__(self) -> None:
        #Carrega os dados dos usuários
        self.users = [
            User(name="Zed", password="deathmark", email="zed@mail.com"),
            User(name="Kayn", password="umbral", email="kayn@mail.com"),
            User(name="Syndra", password="power", email="syndra@mail.com"),
        ]
    def checkUser(self,user):
        return user in self.users

    def checkLogin(self, name, password):
        user_checker = User(name=name, password=password, email=None)
        for user in self.users:
            if user.name == user_checker.name and user.password == user_checker.password:
                
                return True           
        return False
    
    