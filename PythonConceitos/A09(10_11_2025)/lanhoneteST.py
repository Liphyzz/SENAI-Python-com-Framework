# PROBLEMA: GERENCIAR ESTOQUE DA LANCHONETE CLODOALDO

# Importação de Bibliotecas
import streamlit as st

# Início Streamlit
st.title("Lanchonete do Clodoaldo")
st.write("Escolha seu lanche favorito!")
st.header("Menu de opções do restaurante")
st.subheader("Opções de lanches")
st.markdown(
    """
| Código | Descrição do item | Preço  |
|--------|-------------------|--------|
| 1001   | X-Burguer         |R$ 8,00 |
| 1002   | X-SENAI           |R$ 12,00|
| 1003   | X-Campeão         |R$ 13,00|
| 1004   | X-ESP32           |R$ 15,00|
| 1005   | X-C37             |R$ 18,00|
"""
)

# Entrada de dados
opcao = st.selectbox("Selecione o código do lanche desejado:",
                     options=["1001", "1002", "1003", "1004", "1005"])
codigo = int(opcao) # COnvette a string selecionada em numero inteiro
quantidade = st.number_input("Digite a quantidade selecionada", min_value=1, step=1)

# Estrutura de controle de seleção
match codigo:
    case 1001:
        preco = 8.00
    case 1002:
        preco = 12.00
    case 1003:
        preco = 13.00
    case 1004:
        preco = 15.00
    case 1005:
        preco = 18.00
# Processamento de dados
total = preco * quantidade

# Saída de dados
st.subheader("Total a pagar: R$ " + (str(total)))

# Final!!!