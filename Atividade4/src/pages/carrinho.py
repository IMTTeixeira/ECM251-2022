# Luan Teixeira         R.A: 20.01681-6

import streamlit as st
from controllers.usuario_controller import UsuarioController
from models.carrinho import Carrinho
from controllers.produto_controller import ProdutoController
from controllers.carrinho_controller import CarrinhoController
import time

controller_carrinho = CarrinhoController()
def criar_carrinho():
    #try:
        st.write('__________________________________________________________')
        for produto in controller_carrinho.get_all_carrinho():
            with st.container():
                
                colA, colB, colC, colD = st.columns(4)
            with colA:
                st.image(image = produto.imagem, width = 100)
            with colB:
                st.subheader("Produtos")
                st.write(produto.nome)
                
            with colC:
                st.subheader("Quantidade")
                st.write(produto.quantidade)
            with colD:
                st.metric(
                label = "Total",
                value = format(produto.preco * produto.quantidade, '.2f')
                )

                if st.button('Remover produto', key = produto.nome):
                    controller_carrinho.remover_carrinho(produto.id)
                    st.success('Produto removido do carrinho!')
                        
                    
            st.write('__________________________________________________________')
    
try:
    if st.session_state.login:
        st.image(
            image = "https://cdn.iconscout.com/icon/free/png-256/crunchyroll-4062809-3357695.png",
            width = 100
            )
        st.title("Carrinho")
        criar_carrinho()
        st.write('__________________________________________________________')
        valor_total = 0
        for produto in controller_carrinho.get_all_carrinho():
            valor_total += produto.preco * produto.quantidade
        valor_total = format(valor_total, '.2f')
        st.write('')
        st.write('')
        st.subheader("Total")
        st.text(f'R${valor_total}')
            
        st.write('')
        st.write('')
       
        st.write('')
        st.selectbox(
            label = "Forma de pagamento",
            options = ["Cartão de crédito", "Boleto", "Pix", "PicPay", "PayPal"],
        )
        if st.button("Finalizar compra"):
            for percent_complete in range(100):
                    time.sleep(0.01)                    
                    if percent_complete == 30:    
                        st.warning("Processando pagamento...")
                    if percent_complete == 99:
                        st.success("Compra finalizada!")
                        st.write("Agradecemos por comprar na Mangá Store!")
                    produtos_carrinho = controller_carrinho.get_all_carrinho()
                    for itens in produtos_carrinho:
                        controller_carrinho.limpar_carrinho()
                     
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://cdn.iconscout.com/icon/free/png-256/crunchyroll-4062809-3357695.png", width = 100)
        with col2:
            st.title("Bem vindo a Mangá Store!")
            st.text(" ")    
            st.write("Para ter acesso a loja, faça o login!")
except:
    pass