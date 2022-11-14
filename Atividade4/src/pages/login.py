# Luan Teixeira         R.A: 20.01681-6

from cProfile import label
from controllers.usuario_controller import UsuarioController
import streamlit as st

tab1, tab2, tab3 = st.tabs(["Fazer Login", "Cadastre-se", "Configurações do usuário"])

with tab1:
    if st.session_state.login == False:
        st.image(
                image = "https://cdn.iconscout.com/icon/free/png-256/crunchyroll-4062809-3357695.png",
                width = 100,      
            )
            
                    
        nome_usuario = st.text_input(
                label = "Nome de usuário",
                key = 1
                
            )
                
        senha_usuario = st.text_input(
                label = "Senha",
                type = "password",
                key = 2
                
            )        
        if st.button("Fazer Login"):
                try:
                    usuario_controller = UsuarioController()
                    if usuario_controller.checar_login(nome_usuario, senha_usuario):
                        st.success("Login realizado com sucesso!")
                        st.session_state["login"] = True
                        st.session_state["nome_usuario"] = nome_usuario
                        st.session_state["senha_usuario"] = senha_usuario
                    else:
                        st.error("Login ou senha incorretos!")
                except:
                    st.error("Erro ao realizar login!")
    else:
        st.success(f'Você está logado como {st.session_state["nome_usuario"]}')


with tab2:
    st.image(
            image = "https://cdn.iconscout.com/icon/free/png-256/crunchyroll-4062809-3357695.png",
            width = 100,      
        )
        
                
    nome_usuario = st.text_input(
            label = "Crie um nome de usuário",
            key = 3
            
        )

    email_usuario = st.text_input(
            label = "E-mail",
            key = 4
            
        )
            
    senha_usuario = st.text_input(
            label = "Crie uma senha",
            type = "password",
            key = 5
            
        )        

    senha_confirmar = st.text_input(
            label = "Confirme sua senha",
            type = "password",
            key = 6

        )
    if st.button("Cadastrar"):  
        if senha_usuario == senha_confirmar:
                usuario_controller = UsuarioController()
                usuario_novo = usuario_controller.cadastrar_usuario(nome_usuario, email_usuario, senha_usuario)
                if usuario_novo:
                    st.success("Cadastro realizado com sucesso!")
        else:
            st.error("As senhas não conferem!")

with tab3:
    st.image(
            image = "https://cdn.iconscout.com/icon/free/png-256/crunchyroll-4062809-3357695.png",
            width = 100,      
        )
        
                
    nome_usuario = st.text_input(
            label = "Digite nome de usuário (Se não quiser alterar, escreva o mesmo)",
            key = 7,

        )
    
    email_usuario = st.text_input(
            label = "Digite um e-mail (Se não quiser alterar, escreva o mesmo)",
            key = 8,

        )
            
    senha_usuario = st.text_input(
            label = "Digite outra senha (Se não quiser alterar, escreva a mesma)",
            type = "password",
            key = 9,
            
        )        
    
    if st.button("Atualizar"):
            try:
                usuario_controller = UsuarioController()
                if usuario_controller.atualizar_usuario(nome_usuario, email_usuario, senha_usuario) == True:
                    st.success("Usuário atualizado com sucesso!")
                    st.session_state["nome_usuario"] = nome_usuario
                    st.session_state["senha_usuario"] = senha_usuario
            except:
                st.error("Erro ao atualizar usuário!")

