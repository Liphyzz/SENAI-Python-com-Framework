import streamlit as st


def C_f(t):
    return (t * (9/5)) + 32

def C_k(t):
    return t + 273.15

def F_c(t):
    return (t - 32) * (5/9)

def F_k(t):
    return (t - 32) * (5/9) + 273.15

def K_c(t):
    return t - 273.15

def K_f(t):
    return (t - 273.15) * (9/5) + 32


st.sidebar.title("Conversor de temperatura")
st.title("Conversor de temperatura")
st.sidebar.markdown("Converte a temperatura entre Celsius, Fahrenheit e Kelvins")

opcao_a_selecionar = st.sidebar.radio(options=["Celsius", "Fahrenheit", "Kelvin"], key="opcao_radio",label="Selecionar")

# --Entrada de Dados--
temp = st.number_input("Valor da temperatura", format="%.2f", step=1.0)

# if celsius_selecionado + fahrenheit_selecionado + kelvin_selecionado > 1:
#         st.sidebar.error("Por favor, selecione apenas uma unidade de tem")

#Processamento de dados
if st.button("Converter",icon="🌡️"):
             if opcao_a_selecionar in "Celsius":
                st.write(f"{temp}°C em Fahrenheit: {C_f(temp):.2f}°F")
                st.write(f"{temp}°C em Kelvin: {C_k(temp):.2f}K")
             elif opcao_a_selecionar in "Kelvin":
                st.write(f"{temp}°F em Celsius: {F_c(temp):.2f}°C")
                st.write(f"{temp}°F em Kelvin: {F_k(temp):.2f}K")
             elif opcao_a_selecionar in "Fahrenheit":
                st.write(f"{temp} K em Celsius: {K_c(temp):.2f}°C")
                st.write(f"{temp} K em Fahrenheit: {K_f(temp):.2f}°F")