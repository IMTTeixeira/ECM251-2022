# Luan Teixeira         R.A: 20.01681-6

from controllers.produto_controller import produtoController
import streamlit as st
class Carrinho():
    def __init__(self):
        self.produtos = []
        self.quantidade = 0

    def addproduto(self, produto):
        if produto not in st.session_state["carrinho"].getList():
            self.produtos.append(produto)
        else:
            st.error("Produto já adicionado ao carrinho!")
    
    def getQuantidade(self):
        for i in range(len(self.produtos)):
            self.quantidade = st.session_state["quantidade"][i]
            return self.quantidade

    def getList(self):
        return self.produtos
