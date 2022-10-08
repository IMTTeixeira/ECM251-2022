from operator import truediv
from turtle import onclick
from models.carrinho import Carrinho
import streamlit as st
from controllers.user_controller import UserController
from controllers.product_controller import ProductController
if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = Carrinho()
    
if "quantidade" not in st.session_state:
    st.session_state["quantidade"] = 0
if "quantidade2" not in st.session_state:
    st.session_state["quantidade2"] = 0
if "quantidade3" not in st.session_state:
    st.session_state["quantidade3"] = 0


def layout_produtos(product):
    colA, colB = st.columns(2)
    with colA:
        st.subheader(product.name)
        st.image(image = product.url, width = 200)
     
    with colB:
        st.metric(
            label = "Preço",
            value = f'R$ {product.price}'
        )
        quantidade = st.number_input(
            "Quantidade", 
            min_value=1, 
            max_value=100, 
            value=1, 
            key = product.name
            )
        button = st.button("Adicionar ao carrinho", key = product.url)
        if button:
            st.session_state["carrinho"].addProduct(product)
            st.session_state["quantidade"] = quantidade
              
if "login" not in st.session_state:
    st.session_state.login = False
try:
    if st.session_state.login:
        col1 , col2 = st.columns(2)
        # Coluna 1
        with col1:
            
            st.image(
            image = "https://cdn.iconscout.com/icon/free/png-256/crunchyroll-4062809-3357695.png",
            width = 75,
            )
            st.title("Mangá Store")
            
        st.subheader("Mangás em destaque")
        st.text("__________________________________________________________________________________________")   
       
        for i in range(len(ProductController().getProducts())):
             layout_produtos(ProductController().getProducts()[i])
             st.text("__________________________________________________________________________________________")
             st.write('')
             st.write('')          
            
        # Coluna 2   
        with col2:
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.subheader("Bem vindo à melhor loja de mangás do Brasil!")        

    else:
        st.title("Bem vindo a Mangá Store!")
        st.text("__________________________________________________________")
        st.text(" ")    
        st.write("Para ter acesso a loja, faça o login!")
        
except:
    print("Erro")