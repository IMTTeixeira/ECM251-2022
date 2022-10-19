from src.models.item import Item
from src.dao.item_dao import ItemDao
class ItemController:
    def __init__(self) -> None:
        pass

    def pegar_item(self, id) -> Item:
        item = ItemDao.get_instance().pegar_item(id)
        return item

    def inserir_item(self, item) -> None:
        try:
            ItemDao.get_instance().inserir_item(item)
        except:
            return False
        return True

    def pegar_todos_itens(self) -> list[Item]:
        itens = ItemDao.get_instance().get_all()
        return itens