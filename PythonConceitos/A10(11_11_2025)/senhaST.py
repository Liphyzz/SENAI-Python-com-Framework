import streamlit as st

TITULO = "senhaST"
st.set_page_config(page_title = TITULO)
st.title(TITULO)

USUARIO = "Clodoaldo"
SENHA = "Senha123"
MAXIMO_TENTATIVAS = 10

link_destino = "https://www.github.com/edxzyluksz/Python-com-Framework"

# --Entrada de Dados--
usuario_entrada = st.text_input("Nome do usuário")
usuario_senha = st.text_input("Senha", type = "password")

# --Estrutura de controle em loop--
botao_confirmar = st.button("Confirmar")

if 'tentativas' not in st.session_state:
    st.session_state.tentativas = 0


if botao_confirmar == True:
    if st.session_state.tentativas >= MAXIMO_TENTATIVAS:
        st.error("Suas tentativas acabaram, acesso bloqueado!")
    else:
        while st.session_state.tentativas < MAXIMO_TENTATIVAS:
            if usuario_entrada != USUARIO:
                st.warning("Usuário incorreto!")
                break
            if usuario_senha != SENHA:
                st.warning("Senha incorreta!")
                break
            if usuario_entrada == USUARIO and usuario_senha == SENHA:
                st.success("Usuário e senha corretos, login concluido!")
                js = f"window.open('{link_destino}')"  # comando JS para abrir nova aba
                html = f'<script>{js}</script>'
                st.components.v1.html(html, height=0)
                break