# Luan Teixeira         R.A: 20.01681-6

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