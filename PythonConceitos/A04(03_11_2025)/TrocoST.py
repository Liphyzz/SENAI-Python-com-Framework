# PROBLEMA: CÁLCULO DO TROCO

# --Importação das Bibliotecas--
import streamlit as st

# ---Início da página Stremlit---
TITULO = "Calculadora de Troco"
st.title(TITULO)

# --Entrada de Dados--
prc_unidade = st.number_input("Preço unitário do produto: ", min_value = 0.00, step=0.01, format="%.2f")
qntd_comprada = st.number_input("Quantidade comprada: ", min_value = 0, step=1) 
din_recebido = st.number_input("Dinheiro recebido: ", min_value = 0.00, step=0.01, format="%.2f")

# --Processamento de Dados--
valor_total = float(prc_unidade * qntd_comprada)
troco = float(din_recebido - valor_total)

# --Saída de Dados--
st.write(f"Valor total: R${valor_total:.2f}")
st.write(f"Valor recebido: R${din_recebido:.2f}")
st.write(f"TROCO: R${troco:.2f}")