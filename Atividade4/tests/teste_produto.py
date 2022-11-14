from src.controllers.produto_controller import ProdutoController
from src.models.produto import Produto

controller = ProdutoController()
# produtos = controller.get_all_produtos()
# for produto in produtos:
#     print(produto.nome)


novo_produto = Produto(1,"The Beginning After the End",100,"https://mangazim.com/wp-content/uploads/2022/09/the-beginning-after-the-end-todos-os-capitulos-mangazim.jpg")
print(controller.cadastrar_produto(novo_produto))
print("*****************************************************************************************")
produtos = controller.get_all_produtos()
for produto in produtos:
    print(f'ID: {produto.id} | Nome: {produto.nome} | Preço: {produto.preco} | Imagem: {produto.imagem}')