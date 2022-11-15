import sqlite3
from models.produto import Produto
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
        try:
            self.conn = sqlite3.connect('./database/sqlite.db', check_same_thread=False)
        except:
            print('Erro ao conectar ao banco de dados')
    
    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Produtos;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Produto(id = resultado[0], nome = resultado[1], preco = resultado[2], imagem = resultado[3]))
        self.cursor.close()
        return resultados

    def cadastrar_produto(self, produto):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO Produtos (id, nome, preco, imagem) VALUES (?, ?, ?, ?);
            """, (produto.id, produto.nome, produto.preco, produto.imagem))
            self.conn.commit()
            self.cursor.close()
        except:
            print('Esse produto já foi cadastrado')
            return False

    def selecionar_produto(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Produtos WHERE id = ?;
        """, (id,))
        resultado = self.cursor.fetchone()
        self.cursor.close()
        return Produto(id = resultado[0], nome = resultado[1], preco = resultado[2], imagem = resultado[3])
                
    def atualizar_produto(self, produto):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Produtos SET
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
                DELETE FROM Produtos
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
            SELECT * FROM Produtos
            WHERE nome LIKE '{nome}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Produto(id = resultado[0], nome = resultado[1], preco = resultado[2], imagem = resultado[3]))
        self.cursor.close()
        return resultados