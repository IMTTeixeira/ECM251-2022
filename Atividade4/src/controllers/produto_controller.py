# Luan Teixeira         R.A: 20.01681-6
#             produto("The Beginning After the End",99.99,"https://mangazim.com/wp-content/uploads/2022/09/the-beginning-after-the-end-todos-os-capitulos-mangazim.jpg"),
#             produto("One Piece",69.99,"https://m.media-amazon.com/images/I/81rEhhwbubL.jpg"),
#             produto("Solo Leveling",49.99,"https://m.media-amazon.com/images/I/71amUl0481L.jpg"),
#             produto("The God of High School",39.99,"https://www.intoxianime.com/wp-content/uploads/2020/06/EapWDo4WoAEKfx9.jpg"),
#             produto("Martial Peak",59.99,"https://i.pinimg.com/736x/d7/dc/93/d7dc93b6331e3d40256e5053b5a04e14.jpg"),

from models.produto import Produto
from dao.produto_dao import produtoDao
class ProdutoController():
    def __init__(self):
        pass 

    def selecionar_produto(self, id):
        produto = produtoDao.get_instance().selecionar_produto(id)
        return produto

    
    def cadastrar_produto(self, produto) -> bool:
        try:
            produtoDao.get_instance().cadastrar_produto(produto)
        except:
            return False 
        return True
    
    def get_all_produtos(self) -> list[Produto]:
        try: 
            return produtoDao.get_instance().get_all()
        except:
            print("Erro ao pegar todos produtos")
            
    def deletar_produto(self, id) -> bool:
        try:
            return produtoDao.get_instance().deletar_produto(id)
        except:
            raise Exception(" Erro ao deletar produto ")
    
    
    def buscar_produto_nome(self, nome) -> list[Produto]:
        itens = produtoDao.get_instance().buscar_produto_nome(nome)
        return itens