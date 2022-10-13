# Luan Teixeira         R.A: 20.01681-6

from controllers.product_controller import ProductController
import streamlit as st
class Carrinho():
    def __init__(self):
        self.products = []
        self.quantidade = 0

    def addProduct(self, product):
        if product not in st.session_state["carrinho"].getList():
            self.products.append(product)
        else:
            st.error("Produto já adicionado ao carrinho!")
    
    def getQuantidade(self):
        for i in range(len(self.products)):
            self.quantidade = st.session_state["quantidade"]
            return self.quantidade

    def getList(self):
        return self.products
