from controllers.usuario_controller import UsuarioController
from models.usuario import Usuario

controller = UsuarioController()

novo_usuario = Usuario("Luan", "luan@email.com", "3456")
print(controller.cadastrar_usuario(novo_usuario))
print("*****************************************************************************************")

usuarios = controller.get_all_usuarios()
for usuario in usuarios:
    print(f'Nome: {usuario.nome} | Email: {usuario.email} | Senha: {usuario.senha}')