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
#                             st.metric(label = "Preço", value = f'R$ {itens.price}')
#                             quantidade = st.number_input("Quantidade", min_value=1, max_value=10, value=1, key = itens.id)
#                             if st.button("Adicionar ao carrinho", key = itens.name ):
#                                 products_id_in_cart = []
#                                 for product in controller_carrinho.pegar_todos_itens():
#                                     products_id_in_cart.append(product.product_id) # Adiciona todos ids em um array
#                                 if itens.id not in products_id_in_cart: # Verifica se o id do produto ja esta no banco de dados. Caso não esteja, produto adicionado ao carrinho, caso contrário a quantidade é somada no carrinho
#                                     controller_carrinho.inserir_item(Cart(itens.id,itens.name,itens.price,itens.url,quantidade))
#                                     st.success('Produto adicionado ao carrinho!')
#                                 else:
#                                     quantidade_anterior = controller_carrinho.pegar_quantidade_item_carrinho(itens.id)
#                                     quantidade_nova = quantidade + quantidade_anterior
#                                     controller_carrinho.atualizar_quantidade_item_carrinho(itens.id,quantidade_nova)
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
    try:
        st.write('__________________________________________________________')
        for produto in controller_carrinho.get_all_carrinho():
            with st.container():
                
                colA, colB, colC, colD = st.columns(4)
            with colA:
                st.image(image = item.url, width = 100)
            with colB:
                st.subheader("Produtos")
                st.write(item.name)
                
            with colC:
                st.subheader("Qtd.")
                st.write(product_carrinho.getQuantidade())
            with colD:
                st.metric(
                label = "Total",
                value = format(item.price*product_carrinho.getQuantidade(), '.2f'),
                    )
                    if st.button('Remover', key = item.product_id):
                        controller_cart.deletar_item_carrinho(item.product_id) # Ao clicar, remove produto do carrinho
                        st.success('Produto removido do carrinho!')
    except:
        print("Erro layout carrinho")
                        
                    
            st.write('__________________________________________________________')
    except:
        print("Erro layout carrinho")
        
    
try:
    if st.session_state.zoro:
        st.image(
            image = "assets/github_icon.png",
            width = 75,
            )
        st.title("Carrinho")
        layout_carrinho()
        
        colA ,colB, colC, colD, colE = st.columns(5)
        with colA:
            pass
        with colB:
            pass
        with colC:
            pass
        with colD:
            pass
        with colE:
            total = 0
            for itens in controller_cart.pegar_todos_itens():
                total += controller_cart.pegar_quantidade_item_carrinho(itens.product_id)*controller_cart.pegar_preco_item_carrinho(itens.product_id) # Contabilizando total do carrinho pegando o valor e a quantidade do produto em cada item no carrinho
            total = format(total, '.2f')
            st.write('')
            st.write('')
            st.subheader("Total")
            st.text(f'R${total}')
            
        st.write('')
        st.write('')
       
        st.write('')
        st.selectbox(
            label = "Forma de pagamento",
            options = ["Cartão de crédito", "Boleto", "Pix"],
        )
        if st.button("Finalizar compra"):

            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
                if percent_complete == 99:
                    st.balloons()
                    st.success("Compra finalizada com sucesso!")
                    for itens in controller_cart.pegar_todos_itens():
                        controller_cart.deletar_item_carrinho(itens.product_id) # Quando a compra é finalizada, todos produtos dentro do carrinho sao removidos
            
            


       
# =================================================================================#       
                    
# ANTES DE LOGAR:           
    else:
        colA, colB, colC = st.columns(3)
        with colA:
            pass
            
        with colB:
            st.image(
                image = "assets/github_icon.png",
                width = 100,
            )
        with colC:
            pass
        st.write('')
        st.write('')
        st.write('')
        st.info('Faça login para acessar essa página')
except:
    pass