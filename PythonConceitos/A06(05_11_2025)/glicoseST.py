# PROBLEMA: MEDIÇÃO DA GLICOSE NO SANGUE 

# --Importação das Bibliotecas--
import streamlit as st

# --Constantes pré-definidas--
TITULO = "Níveis de Glicose"

# ---Configurações da Página---
st.set_page_config(page_title = TITULO)

# ---Início da página Stremlit---
st.title(TITULO)
st.markdown(
    """
 ____________________________________
| NÍVEL DE GLICOSE |  CLASSIFICAÇÃO  |
|——————————————————|—————————————————|
|     0  —  70     |   Hipoglicemia  |
|——————————————————|—————————————————|
|    71  —  100    |   Normal        |
|——————————————————|—————————————————|
|   101  —  140    |   Pré-diabetes  |
|——————————————————|—————————————————|
|       141+       |   Diabetes      |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
)

# --Entrada de Dados--
glicose = st.number_input("Insira o nível da glicose no sangue (mg/Dl): ", min_value = 0, max_value = 800)

# --Processamento de Dados + Saída de Dados--
if st.button("Classificar"):
    if glicose < 0:
        st.write("Valor incoreto! Eu espero...")
    if glicose >= 0 and glicose < 71:
        st.write("Hipoglicemia")
    elif glicose > 70 and glicose < 101:
        st.write("Normal")
    elif glicose > 100 and glicose < 141:
        st.write("Pré-diabetes")
    else:
        st.write("Diabetes")