class Item():
    #Construtor
    def __init__(self, preço, nome, descrição = None):
        self._nome = nome
        self._preço = preço
        self._descrição = descrição
    def get_nome(self):
        return self._nome
    def get_preço(self):
        return self._preço
    def get_descrição(self):
        return self._descrição
    def __str__(self):
        return f'Nome : {self._nome}, Preço: {self._preço}, Descrição: {self._descrição}'