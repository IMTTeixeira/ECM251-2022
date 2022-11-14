# Luan Teixeira         R.A: 20.01681-6

from cProfile import label
from controllers.usuario_controller import UsuarioController
import streamlit as st
        
st.image(
        image = "https://cdn.iconscout.com/icon/free/png-256/crunchyroll-4062809-3357695.png",
        width = 100,      
    )
    
            
nome_usuario = st.text_input(
        label = "Nome de usuário",
         
    )
        
senha_usuario = st.text_input(
        label = "Senha",
        type = "password",
        
    )        
if st.button("Fazer Login"):
        user_controller = UserController()
        cond = False
        if user_controller.checar_login(nome_usuario, senha_usuario):
            st.success("Login realizado com sucesso!")
            cond = True
            st.session_state["login"] = cond
        else:
            st.error("Login ou senha incorretos!")