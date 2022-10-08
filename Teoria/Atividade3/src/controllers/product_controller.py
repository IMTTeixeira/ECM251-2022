from models.product import Product
class ProductController():
    def __init__(self):
        #Carrega os dados dos produtos
        self.product = [
            Product("The Beginning After the End",99.99,"https://mangazim.com/wp-content/uploads/2022/09/the-beginning-after-the-end-todos-os-capitulos-mangazim.jpg"),
            Product("One Piece",69.99,"https://m.media-amazon.com/images/I/81rEhhwbubL.jpg"),
            Product("Solo Leveling",49.99,"https://m.media-amazon.com/images/I/71amUl0481L.jpg"),
        ]
    def getProducts(self):
        for i in range(len(self.product)):
            return self.product