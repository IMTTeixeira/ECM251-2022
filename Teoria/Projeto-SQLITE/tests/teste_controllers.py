from src.controllers.item_controller import ItemController
from src.models.item import Item

controller = ItemController()
items = controller.pegar_todos_itens()

for item in items:
    print(item)

novo_item = Item("OLA1", "Cooler REDRAGON Vermelho", 19.90)
print(controller.inserir_item(novo_item))

items = controller.pegar_todos_itens()

print("*******************************************************************************")
for item in items:
    print(item)

print("*******************************************************************************")
item = controller.pegar_item("CAF")
print(item)

# print("*******************************************************************************")
# item = controller.pegar_item("OLA")
# item.nome = "RTX 4090"
# item.preco = 14990.90
# print(controller.atualizar_item(item))

# print("*******************************************************************************")
# print(controller.deletar_item(item.id))

print("*******************************************************************************")
items = controller.buscar_item_nome("Au")
for item in items:
    print(item)