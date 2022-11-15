import sqlite3
from models.carrinho import Carrinho

class carrinhoDao:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = carrinhoDao()
        return cls._instance

    def _connect(self):
        try:
            self.conn = sqlite3.connect('./database/sqlite.db', check_same_thread=False)
        except:
            print('Erro ao conectar ao banco de dados')
    
    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Carrinho;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Carrinho(id = resultado[0], nome = resultado[1], preco = resultado[2], imagem = resultado[3], quantidade = resultado[4]))
        self.cursor.close()
        return resultados

    def adicionar_carrinho(self, produto, quantidade):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Carrinho (nome, preco, imagem, quantidade) VALUES (?, ?, ?, ?);
        """, (produto.nome, produto.preco, produto.imagem, quantidade))
        self.conn.commit()
        self.cursor.close()

    def limpar_carrinho(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            DELETE FROM Carrinho;
        """)
        self.conn.commit()
        self.cursor.close()
