import streamlit as st
# Problema duração de tempo
TITULO = "Calculadora de Duração de Tempo"
st.set_page_config(page_title=f"{TITULO}")
st.title(TITULO)

# Entrada de dados
tempo = st.number_input("Digite o tempo em segundos: ", min_value= 0, step=2, 
                        help="Insira a duração em segundos para converter em horas, minutos e segundos.")
horas = tempo // 3600 # Calculo das horas
minutos = (tempo % 3600) // 60 # Calculo dos minutos
segundos = tempo % 60 # Calculo dos segundos. Ou seja, se o usuário digitar 60, não existira

# Saída de dados
st.write(f"{horas} horas, {minutos} minutos e {segundos} segundos.")