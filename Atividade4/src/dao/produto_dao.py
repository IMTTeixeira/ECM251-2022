import sqlite3
from src.models.produto import produto
class produtoDao:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = produtoDao()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')
    
    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Itens;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(produto(id = resultado[0], nome = resultado[1], preco = resultado[2], imagem = resultado[3]))
        self.cursor.close()
        return resultados

    def cadastrar_produto(self, produto):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Itens (id, nome, preco, imagem) VALUES (?, ?, ?, ?);
        """, (produto.id, produto.nome, produto.preco, produto.imagem))
        self.conn.commit()
        self.cursor.close()

    def selecionar_produto(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE id = '{id}';
        """)
        produto = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            produto = (produto(id = resultado[0], nome = resultado[1], preco = resultado[2], imagem = resultado[3]))
        self.cursor.close()
        return produto

    def atualizar_produto(self, produto):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Itens SET
                nome = '{produto.nome}',
                preco = '{produto.preco}'
                imagem = '{produto.imagem}'
                WHERE id = '{produto.id}';
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def deletar_produto(self, id):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Itens
                WHERE id = '{id}';
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def buscar_produto_nome(self, nome):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE nome LIKE '{nome}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(produto(id = resultado[0], nome = resultado[1], preco = resultado[2], imagem = resultado[3]))
        self.cursor.close()
        return resultados