from dao.carrinho_dao import carrinhoDao
from models.carrinho import Carrinho
class CarrinhoController():
    def __init__(self):
        pass 

    def adicionar_carrinho(self, produto, quantidade) -> bool:
        try:
            carrinhoDao.get_instance().adicionar_carrinho(produto, quantidade)
        except:
            return False 
        return True
    
    def get_all_carrinho(self) -> list[Carrinho]:
        try: 
            return carrinhoDao.get_instance().get_all()
        except:
            print("Erro ao pegar todos produtos")
            
    def limpar_carrinho(self) -> bool:
        try:
            return carrinhoDao.get_instance().limpar_carrinho()
        except:
            raise Exception(" Erro ao limpar carrinho ")