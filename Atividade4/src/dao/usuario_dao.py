# Luan Teixeira         R.A: 20.01681-6

import sqlite3
from models.usuario import Usuario
import streamlit as st
class usuarioDao:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = usuarioDao()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./database/sqlite.db', check_same_thread=False)
    
    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Usuario;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Usuario(nome = resultado[0], email = resultado[1], senha = resultado[2]))
        self.cursor.close()
        return resultados

    def cadastrar_usuario(self, nome, email, senha):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO Usuario (nome, email, senha) VALUES (?, ?, ?);
            """, (nome, email, senha))
            self.conn.commit()
            self.cursor.close()
        except:
            print("Esse nome já está sendo usado por outro usuário. Tente outro.")

    def selecionar_usuario(self, nome):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Usuario
            WHERE nome = '{nome}';
        """)
        usuario = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            usuario = (Usuario(nome = resultado[0], email = resultado[1], senha = resultado[2]))
        self.cursor.close()
        return usuario

    def atualizar_usuario(self, nome, email, senha):
        try:
            if st.session_state['login']:
                nome_atual = st.session_state['nome_usuario']
                self.cursor = self.conn.cursor()
                self.cursor.execute(f"""
                    UPDATE Usuario SET 
                    nome = ?,
                    email = ?,
                    senha = ?
                    WHERE nome = ?;
                """,(nome, email, senha, nome_atual))
                self.conn.commit()
                self.cursor.close()
        except:
            print("Esse nome já está sendo usado por outro usuário. Tente outro.")
            return False
        print ("Usuário atualizado com sucesso!")
        return True

    def deletar_usuario(self, nome):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Usuario
                WHERE nome = '{nome}';
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def buscar_usuario_nome(self, nome):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                SELECT * FROM Usuario
                WHERE nome LIKE '{nome}%';
            """)
            resultados = []
            for resultado in self.cursor.fetchall():
                resultados.append(Usuario(nome = resultado[0], email = resultado[1], senha = resultado[2]))
            self.cursor.close()
            return resultados
        except:
            print("Não foi possível encontrar nenhum usuário com esse nome.")

    def checar_login(self, nome, senha):
        #try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                SELECT * FROM Usuario
                WHERE nome = '{nome}' AND senha = '{senha}';
            """)
            usuario = None
            resultado = self.cursor.fetchone()
            if resultado != None:
                usuario = (Usuario(nome = resultado[0], email = resultado[1], senha = resultado[2]))
            self.cursor.close()
            return usuario
        #except:
           # print("Não foi possível realizar o login. Tente novamente.")