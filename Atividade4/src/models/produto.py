# Luan Teixeira         R.A: 20.01681-6

class Produto():
    def __init__(self, id, nome, preco, imagem) -> None:
        self.id = id
        self.nome = nome
        self.preco = preco
        self.imagem = imagem
    def __str__(self) -> str:
        return f'Produto: (id = {self.id}, nome={self.nome}, preco={self.preco}, imagem={self.imagem})'
    def __eq__(self, __o: object) -> bool:
        if type(__o) != Produto:
            return False
        return self.nome == __o.nome