class Carrinho:
    #Método construtor
    def __init__(self): # __init__ é um método construtor do Python
        self._itens = []
    #Demais métodos
    def get_valor_total(self):
        total= 0
        for item in self.itens:
            total += item.get_preço()
    def get_quantidade_itens(self):
        return len(self._itens)
    def adicionar_item(self, item):
        self._itens.append(item)
    def remover(self,item):
        self._itens.remove(item)
        pass
