from modelos.item import Item
from modelos.carrinho import Carrinho
item1 = Item(
    preço = 350,
    nome = 'Dark Souls 3')

item2 = Item(
    preço = 100,
    nome = 'Elden Ring',
    descrição = 'Jogo de RPG Mundo aberto')

item3 = Item(
    preço = 100,
    nome = 'Elden Ring',
    descrição = 'Jogo de RPG Mundo aberto')

carrinho1 = Carrinho()
carrinho1.adicionar_item(item1)
carrinho1.adicionar_item(item2)
print(item1 == item2)
print(item2 == item3)
print(item2 == 'Jogo de RPG Mund Aberto')