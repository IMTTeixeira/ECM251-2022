class Products():
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url
    
    def __str__(self):
        return f'Products(Name:{self.name}, Price:{self.price}, URL:{self.url})'