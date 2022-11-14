# Luan Teixeira         R.A: 20.01681-6

from models.usuario import Usuario
from dao.usuario_dao import usuarioDao


class UsuarioController():
    def __init__(self) -> None:
        #Carrega os dados dos usuários
        # self.usuarios = [
        #     Usuario(nome="Zed", password="deathmark", email="zed@mail.com"),
        #     Usuario(nome="Kayn", password="umbral", email="kayn@mail.com"),
        #     Usuario(nome="Syndra", password="power", email="syndra@mail.com"),
        # ]
        pass

    # def checkUser(self,usuario):
    #     return usuario in self.usuarios

    def selecionar_usuario(self, nome):
        usuario = usuarioDao.get_instance().selecionar_usuario(nome)
        return usuario

    
    def cadastrar_usuario(self, nome, email, senha) -> bool:
        try:
            usuarioDao.get_instance().cadastrar_usuario(nome, email, senha)
        except:
            return False 
        return True
    
    def get_all_usuarios(self) -> list[Usuario]:
        try: 
            return usuarioDao.get_instance().get_all()
        except:
            print("Erro ao pegar todos usuarios")
            
    def deletar_usuario(self, id) -> bool:
        try:
            return usuarioDao.get_instance().deletar_usuario(id)
        except:
            raise Exception(" Erro ao deletar usuario ")
    
    
    def buscar_usuario_nome(self, nome) -> list[Usuario]:
        usuarios = usuarioDao.get_instance().buscar_usuario_nome(nome)
        return usuarios

    def checar_login(self, nome, senha):
        usuario = usuarioDao.get_instance().checar_login(nome, senha)
        return usuario

    def atualizar_usuario(self, nome, email, senha):
        try:
            usuarioDao.get_instance().atualizar_usuario(nome, email, senha)
            return True
        except:
            print(" Erro ao atualizar usuario ")
       
    
    