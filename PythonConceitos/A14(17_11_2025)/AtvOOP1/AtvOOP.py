import classes as c
import streamlit as st


TITULO = "Programação Orientada a Objeto no Streamlit"
# --Início Streamlit--
st.set_page_config(page_title=TITULO)
st.title(TITULO)


# Inicializa o estado da sessão para ambos os formulários
if 'form1_visible' not in st.session_state:
    st.session_state.form1_visible = False

if 'form2_visible' not in st.session_state:
    st.session_state.form2_visible = False


# Funções de callback para alternar a visibilidade de cada formulário
def show_form1_only():
    if st.session_state.form1_visible == False:
        st.session_state.form1_visible = True
        st.session_state.form2_visible = False # Esconde o outro
    else:
        st.session_state.form1_visible = False
        st.session_state.form2_visible = False

def show_form2_only():
    if st.session_state.form2_visible == False:
        st.session_state.form1_visible = False # Esconde o outro
        st.session_state.form2_visible = True
    else:
        st.session_state.form1_visible = False
        st.session_state.form2_visible = False


c1, c2 = st.columns(2, border = True)

# Colunas para cada acessar cada função
with c1:
    st.header("Função 1: Pessoa mais velha")
    st.divider()
    st.button("Mostrar/Esconder Formulário 1", on_click=show_form1_only)

with c2:
    st.header("Função 2: Média salarial")
    st.divider()
    st.button("Mostrar/Esconder Formulário 2", on_click=show_form2_only)


# Formulários escondidos a serem visibilizados
if st.session_state.form1_visible:
    with st.form(key = "form1"):
        st.subheader("Pessoa 1:")
        nome1 = st.text_input("Nome da pessoa 1", key="n1")
        idade1 = st.text_input("Idade da pessoa 1", key="i1")

        st.subheader("Pessoa 2:")
        nome2 = st.text_input("Nome da pessoa 2", key="n2")
        idade2 = st.text_input("Idade da pessoa 2", key="i2")

        st.write()

        botaof1 = st.form_submit_button("Calcular pessoa mais velha")

        if botaof1 and nome1.replace(" ", "").isalpha() and idade1.isdigit() and nome2.replace(" ", "").isalpha() and idade2.isdigit():
            pessoa1 = c.Pessoa(nome1, idade1)
            pessoa2 = c.Pessoa(nome2, idade2)

            st.success(pessoa1.mais_velha(pessoa2))

        elif botaof1 and (not nome1.replace(" ", "").isalpha() or not idade1.isdigit() or not nome2.replace(" ", "").isalpha() or not idade2.isdigit()):
            st.error("Insira valores válidos (Nome só aceita letras e espaços. Idade só aceita números naturais)")

if st.session_state.form2_visible:
    with st.form(key = "form2"):
        st.subheader("Funcionário 1:")
        nomef1 = st.text_input("Nome do funcionário 1", key="nf1")
        salario1 = st.number_input("Salário do funcionário 1", key="s1", step=0.5)

        st.subheader("Funcionário 2:")
        nomef2 = st.text_input("Nome do funcionário 2", key="nf2")
        salario2 = st.number_input("Salário do funcionário 2", key="s2", step=0.5)

        st.write()

        botaof2 = st.form_submit_button("Calcular média entre os salários")

        if botaof2 and nomef1.replace(" ", "").isalpha() and nomef2.replace(" ", "").isalpha():
            f1 = c.Funcionario(nomef1, salario1)
            f2 = c.Funcionario(nomef2, salario2)

            st.success(f"Média salarial: {f1.media_salarial(f2)}")

        elif botaof2 and (not nomef1.replace(" ", "").isalpha() or not nomef2.replace(" ", "").isalpha()):
            st.error("Insira valores válidos (Nome só aceita letras e espaços. Salário só aceita números racionais)")