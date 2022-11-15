# Luan Teixeira         R.A: 20.01681-6

from controllers.produto_controller import ProdutoController
from models.produto import Produto

controller = ProdutoController()

novo_produto1 = Produto(1,"The Beginning After the End",100,"https://mangazim.com/wp-content/uploads/2022/09/the-beginning-after-the-end-todos-os-capitulos-mangazim.jpg")
print(controller.cadastrar_produto(novo_produto1))
print("*****************************************************************************************")
produtos = controller.get_all_produtos()
for produto in produtos:
    print(f'ID: {produto.id} | Nome: {produto.nome} | Preço: {produto.preco} | Imagem: {produto.imagem}')

print("*****************************************************************************************")
print(controller.selecionar_produto(1))
print("*****************************************************************************************")
print(controller.cadastrar_produto(novo_produto1))