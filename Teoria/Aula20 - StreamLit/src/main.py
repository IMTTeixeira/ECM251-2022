import streamlit as st

home, info, cadastro = st.tabs(["Home", "Info", "Cadastro"])
with home:
    st.title('Hello World StreamLit 😘👻')
    st.write('Tmj Bira')
    st.markdown('## Subtitulo de **Seção**:')
    st.code(
        """
        def somar(a,b):
            return a + b
        val1 = 10
        val2 = 12
        print(somar(val1, val2))
        """, language='python'
    )
    st.code(
        """
        python -m streamlit run arquivo.py
        """, language='bash'
    )
    st.metric(
        label = "Total da compra (R$):",
        value = 105.92
    )

with info:
    def fui_apertado():
        print('Fui apertado')

    def somar2(v1,v2):
            resultado  = v1 + v2
            st.session_state["resultado"] = resultado

    numero1 = st.number_input(
        label = 'Valor 1:',
        min_value = 0,
        max_value = 100,
        )
    numero2 = st.number_input(
        label = 'Valor 2:',
        min_value = 0,
        max_value = 100,
        )

    st.button(
        label ="Clique aqui👍",
        help = "Clique aqui para ver o resultado",
        on_click = somar2,
        kwargs = {'v1': numero1, 'v2': numero2}
        )

    if "resultado" in st.session_state:
        st.metric(
        label = "Resultado da soma:",
        value = st.session_state["resultado"]
    )

with cadastro:
    col1 , col2, col3 = st.columns(3)

    with col1:
        st.image(
        "https://cdna.artstation.com/p/assets/images/images/038/995/552/large/kamley-weigands-arthur.jpg?1624638538",
        caption = "Arthur Leywin",
        )

    with col2:
        st.image(
        "assets/seris.png",
        caption = "Seris Vitra",)

    with col3:
        st.image(
        "assets/caera",
        caption = "Caera Denoir",)

    st.sidebar.title("Navegação")