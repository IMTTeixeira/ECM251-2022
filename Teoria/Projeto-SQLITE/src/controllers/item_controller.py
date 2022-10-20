from src.models.item import Item
from src.dao.item_dao import ItemDao
class ItemController:
    def __init__(self) -> None:
        pass

    def pegar_item(self, id) -> Item:
        item = ItemDao.get_instance().pegar_item(id)
        return item

    def inserir_item(self, item) -> bool:
        try:
            ItemDao.get_instance().inserir_item(item)
        except:
            return False
        return True

    def pegar_todos_itens(self) -> list[Item]:
        itens = ItemDao.get_instance().get_all()
        return itens

    def atualizar_item(self, item) -> bool:
        return ItemDao.get_instance().atualizar_item(item)

    def deletar_item(self, id) -> bool:
        return ItemDao.get_instance().deletar_item(id)

    def buscar_item_nome(self, nome) -> list[Item]:
        itens = ItemDao.get_instance().buscar_item_nome(nome)
        return itens