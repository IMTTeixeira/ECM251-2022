import streamlit as st
from controllers.user_controller import UserController
from models.carrinho import Carrinho
from controllers.product_controller import ProductController
import time


def criar_carrinho(product_carrinho):
    st.write('__________________________________________________________')
    for item in product_carrinho.getList():
        with st.container():
            colA, colB, colC, colD, colE = st.columns(5,gap = 'small')
            with colA:
                st.image(image = item.url, width = 100)
            with colB:
                st.subheader("Adicionado")
                st.write(item.name)
                
            with colC:
                st.subheader("Qtd.")
                st.write(product_carrinho.getQuantidade())
            with colD:
                st.subheader("Preço")
                st.write(item.price)
            with colE:
                    st.metric(
                    label = "Total",
                    value = format(item.price*product_carrinho.getQuantidade(), '.2f'),
                        )
        
    
try:
    if st.session_state.login:
        st.title("Carrinho")
        criar_carrinho(st.session_state["carrinho"])
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('Frete: R$ 15,00')
        if st.session_state["carrinho"].getList() != []:
            st.metric(
            label = "Total da compra",
            value = format(sum([product.price*st.session_state["carrinho"].getQuantidade() for product in st.session_state["carrinho"].getList()]) + 15, '.2f'),
        )
        st.selectbox(
            label = "Forma de pagamento",
            options = ["Cartão de crédito", "Boleto", "Pix", "PicPay", "PayPal"],
        )
        if st.button("Finalizar compra"):

            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
                if percent_complete == 30:    
                    st.warning("Processando pagamento...")
                if percent_complete == 99:
                    st.success("Compra finalizada!")
                    for i in range(len(st.session_state["carrinho"].getList())):
                        st.session_state["carrinho"].getList().pop()
            
            


       
    else:
        st.title("Bem vindo ao meu site!")
        st.text("__________________________________________________________")
        st.write("Por favor, faça o login para acessar a loja!")
except:
    pass