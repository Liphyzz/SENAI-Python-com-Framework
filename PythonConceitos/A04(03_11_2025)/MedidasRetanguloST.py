# PROBLEMA: CALCULOS COM RETÂNGULOS

# --Importação das Bibliotecas--
import streamlit as st
import math as mt

# ---Início da página Stremlit---
TITULO = "Problema Retângulo"
st.title(TITULO)

# --Entrada de Dados--
base = st.number_input("Digite a base do retângulo (m): ", min_value = 0.01, format="%.2f")
altura = st.number_input("Digite a altura do retângulo (m): ", min_value = 0.01, format="%.2f")

# --Processamento de Dados--
area = base * altura
perimetro = 2 * (base + altura)
diagonal = mt.sqrt(base ** 2 + altura ** 2)

# --Saída de Dados--
st.write(f"A área do retângulo é {area :.2f} m²")
st.write(f"O perímetro do retângulo é {perimetro :.2f} m")
st.write(f"A diagonal do retângulo é {diagonal :.2f} m")