# Luan Teixeira         R.A: 20.01681-6

from models.carrinho import Carrinho
import streamlit as st
from controllers.usuario_controller import UsuarioController
from controllers.produto_controller import ProdutoController
from controllers.carrinho_controller import CarrinhoController

controller = ProdutoController()
controller_carrinho = CarrinhoController()

def criar_produtos():
    try:
        with st.container():
            for produto in controller.get_all_produtos():
                colA, colB = st.columns(2)
                with colA:
                    st.subheader(produto.nome)
                    st.image(image = produto.imagem, width = 200)
                
                with colB:
                    st.metric(
                        label = "Preço",
                        value = f'R$ {produto.preco}'
                    )
                    quantidade = st.number_input(
                        "Quantidade", 
                        min_value=1, 
                        max_value=100, 
                        value=1, 
                        key = produto.id
                        )
                    if st.button("Adicionar ao carrinho", key = produto.id):
                        produtos_adicionados = []
                        for produto in controller_carrinho.get_all_carrinho():
                            produtos_adicionados.append(produto.produto_id)
                        if produto.id not in produtos_adicionados:
                            controller_carrinho.adicionar_carrinho(Carrinho(produto.id,produto.nome,produto.preco,produto.imagem,quantidade))
                            st.success('Produto adicionado ao carrinho!')
                        else:
                            quantidade_atual = controller_carrinho.get_all_carrinho()[produtos_adicionados.index(produto.id)].quantidade
                            controller_carrinho.get_all_carrinho()[produtos_adicionados.index(produto.id)].quantidade = quantidade_atual + quantidade
                            st.success('Produto adicionado ao carrinho!')
                            
    except:
        print("Erro ao criar produtos")

if "login" not in st.session_state:
    st.session_state["login"] = False
    
try:
    if st.session_state.login:
        tab1, tab2 = st.tabs(["Mangás", "Cadastro de Produtos"])
        st.title("Bem vindo à Mangá Store")
        st.subheader("Mangás em destaque")        
        criar_produtos()
        
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