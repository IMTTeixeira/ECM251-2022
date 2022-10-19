from src.dao.item_dao import ItemDao

items = ItemDao().get_instance().get_all()

for item in items:
    print(item)