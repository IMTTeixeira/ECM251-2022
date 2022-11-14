# Luan Teixeira         R.A: 20.01681-6

from models.produto import produto
class produtoController():
    def __init__(self):
        #Carrega os dados dos produtos
        self.produto = [
            produto("The Beginning After the End",99.99,"https://mangazim.com/wp-content/uploads/2022/09/the-beginning-after-the-end-todos-os-capitulos-mangazim.jpg"),
            produto("One Piece",69.99,"https://m.media-amazon.com/images/I/81rEhhwbubL.jpg"),
            produto("Solo Leveling",49.99,"https://m.media-amazon.com/images/I/71amUl0481L.jpg"),
            produto("The God of High School",39.99,"https://www.intoxianime.com/wp-content/uploads/2020/06/EapWDo4WoAEKfx9.jpg"),
            produto("Martial Peak",59.99,"https://i.pinimg.com/736x/d7/dc/93/d7dc93b6331e3d40256e5053b5a04e14.jpg"),
        ]
    def getprodutos(self):
        for i in range(len(self.produto)):
            return self.produto