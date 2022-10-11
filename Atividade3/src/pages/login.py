from cProfile import label
from controllers.user_controller import UserController
import streamlit as st
        

col1, col2, col3 = st.columns(3,gap= "small")
with col2:
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
        if user_controller.checkLogin(nome_usuario, senha_usuario):
            st.success("Login realizado com sucesso!")
            cond = True
            st.session_state["login"] = cond
        else:
            st.error("Login ou senha incorretos!")