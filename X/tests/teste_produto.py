from src.controllers.produto_controller import *
from src.models.produto import *
from src.dao.produto_dao import *

produto1 = ProdutoController.cadastrar_produto(produto(id=1, nome="The Beginning After the End", preco=99.99, imagem="https://mangazim.com/wp-content/uploads/2022/09/the-beginning-after-the-end-todos-os-capitulos-mangazim.jpg"))
