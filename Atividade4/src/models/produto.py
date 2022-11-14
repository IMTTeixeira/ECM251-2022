# Luan Teixeira         R.A: 20.01681-6

class produto():
    def __init__(self,nome, preco, url):
        self.nome = nome
        self.preco = preco
        self.url = url
    def __str__(self) -> str:
        return f'produto(nome:{self.nome}, preco:{self.preco}, url:{self.url})'
    def __eq__(self, __o: object) -> bool:
        if type(__o) != produto:
            return False
        return self.nome == __o.nome