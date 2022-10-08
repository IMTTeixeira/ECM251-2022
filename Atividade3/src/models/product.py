class Product():
    def __init__(self,name, price, url):
        self.name = name
        self.price = price
        self.url = url
    def __str__(self) -> str:
        return f'Product(name:{self.name}, price:{self.price}, url:{self.url})'
    def __eq__(self, __o: object) -> bool:
        if type(__o) != Product:
            return False
        return self.name == __o.name