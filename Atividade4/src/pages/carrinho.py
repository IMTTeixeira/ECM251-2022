# # Luan Teixeira         R.A: 20.01681-6

# import streamlit as st
# from controllers.usuario_controller import UsuarioController
# from models.carrinho import Carrinho
# from controllers.produto_controller import ProdutoController
# import time


# def criar_carrinho(produto_carrinho):
#     st.write('__________________________________________________________')
#     for produto in produto_carrinho.getList():
#         with st.container():
#             colA, colB, colC, colD = st.columns(4)
#             with colA:
#                 st.image(image = produto.url, width = 100)
#             with colB:
#                 st.subheader("Produtos")
#                 st.write(produto.nome)
                
#             with colC:
#                 st.subheader("Qtd.")
#                 st.write(produto_carrinho.getQuantidade())
#             with colD:
#                 st.metric(
#                 label = "Total",
#                 value = format(produto.preco*produto_carrinho.getQuantidade(), '.2f'),
#                     )
        
    
# try:
#     if st.session_state.login:
#         st.title("Carrinho")
#         criar_carrinho(st.session_state["carrinho"])
#         if st.session_state["carrinho"].getList() != []:
#             st.subheader('Frete: R$ 15,00')
#             st.metric(
#             label = "Total da compra",
#             value = format(sum([produto.preco*st.session_state["carrinho"].getQuantidade() for produto in st.session_state["carrinho"].getList()]) + 15, '.2f'),
#             )
#             st.selectbox(
#                 label = "Escolha a forma de pagamento",
#                 options = ["Cartão de crédito", "Boleto", "Pix", "PicPay", "PayPal"],
#             )
#             if st.button("Finalizar compra"):               
#                 for percent_complete in range(100):
#                     time.sleep(0.01)                    
#                     if percent_complete == 30:    
#                         st.warning("Processando pagamento...")
#                     if percent_complete == 99:
#                         st.success("Compra finalizada!")
#                         st.write("Agradecemos por comprar na Mangá Store!")
#                         for i in range(len(st.session_state["carrinho"].getList())):
#                             st.session_state["carrinho"].getList().pop()
                        
            
            


       
#     else:
#         col1, col2 = st.columns(2)
#         with col1:
#             st.image("https://cdn.iconscout.com/icon/free/png-256/crunchyroll-4062809-3357695.png", width = 100)
#         with col2:
#             st.title("Bem vindo a Mangá Store!")
#             st.text(" ")    
#             st.write("Para ter acesso a loja, faça o login!")
# except:
#     pass