# Luan Teixeira         R.A: 20.01681-6

class Carrinho():
    def __init__(self, id, nome, preco, imagem, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.imagem = imagem
        self.quantidade = quantidade

    def __str__ (self):
        return f'ID: {self.id} | Nome: {self.nome} | Preço: {self.preco} | Imagem: {self.imagem} | Quantidade: {self.quantidade}'