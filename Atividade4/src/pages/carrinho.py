# Luan Teixeira         R.A: 20.01681-6

# import streamlit as st
# from controllers.usuario_controller import UsuarioController
# from models.carrinho import Carrinho
# from controllers.produto_controller import ProdutoController
# from controllers.carrinho_controller import CarrinhoController
# import time

# controller = ProdutoController()
# controller_carrinho = CarrinhoController()
# controller_usuario = UsuarioController()
# if st.session_state.login:
#     def criar_produtos():
#         try:
#             with st.container():
#                 for produto in controller.get_all_produtos():
#                     colA, colB , colC = st.columns(3)
#                     with colA:
#                         st.subheader(produto.nome)
#                         st.image(image = produto.imagem, width = 250)
                        
#                     with colB: 
#                         st.text(f'      {random.choice(condicao_produto)} | {random.randrange(0,1000)} Vendidos') # Gera valores aleatorio com a biblioteca random do Python
#                     with colC:
#                         try:
#                             st.metric(label = "Preço", value = f'R$ {itens.preco}')
#                             quantidade = st.number_input("Quantidade", min_value=1, max_value=10, value=1, key = itens.id)
#                             if st.button("Adicionar ao carrinho", key = itens.nome ):
#                                 products_id_in_cart = []
#                                 for product in controller_carrinho.pegar_todos_itens():
#                                     products_id_in_cart.append(product.product_id) # Adiciona todos ids em um array
#                                 if itens.id not in products_id_in_cart: # Verifica se o id do produto ja esta no banco de dados. Caso não esteja, produto adicionado ao carrinho, caso contrário a quantidade é somada no carrinho
#                                     controller_carrinho.inserir_produto(Cart(itens.id,itens.nome,itens.preco,itens.imagem,quantidade))
#                                     st.success('Produto adicionado ao carrinho!')
#                                 else:
#                                     quantidade_anterior = controller_carrinho.pegar_quantidade_produto_carrinho(itens.id)
#                                     quantidade_nova = quantidade + quantidade_anterior
#                                     controller_carrinho.atualizar_quantidade_produto_carrinho(itens.id,quantidade_nova)
#                                     st.success('Produto adicionado ao carrinho!')
#                         except:
#                             print('Erro ao adicionar ao carrinho')
#                     st.write("")
#                     st.write('')
#         except:
#             print("Erro layout produtos")

# try:
#     if st.session_state.zoro:
#         col1 , col2, col3, col4= st.columns(4)
       
#         # Coluna 1
#         with col1:
            
#             st.image(
#             image = "assets/github_icon.png",
#             width = 75,
#             )
#             st.title("AnimeHub")
            
#         st.subheader("Camisetas selecionados especialmente para você!")
#         st.caption("__________________________________________________________________________________________") 
        
        
#     # =================================================================================#       
                    
# # ANTES DE LOGAR:           
#     else:
#         colA, colB, colC = st.columns(3)
#         with colA:
#             pass
            
#         with colB:
#             st.image(
#                 image = "assets/github_icon.png",
#                 width = 100,
#             )
#         with colC:
#             pass
#         st.write('')
#         st.write('')
#         st.write('')
#         st.info('Faça login para acessar essa página')
        
# except:
#     raise Exception("erro na pagina home")

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
    #except:
        #print("Erro layout carrinho")
        
    
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
            


       
# =================================================================================#       
                    
# ANTES DE LOGAR:           
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