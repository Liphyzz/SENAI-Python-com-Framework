# Continuar...
import streamlit as st

# --Início do Streamlit--
TITULO = "Registro de pessoas"
st.set_page_config(page_title = TITULO)
st.title(TITULO)

# --Variáveis pré-definidas--
total_alturas = float(0.00)
pessoas_menores = []
n_pessoas_menores = int(0)
# --Entrada de Dados--
try:
    q_pessoas = int(st.number_input("Quantas pessoas serão digitadas? (max. 10)", step = 1))

    confirmar = st.button("Confirmar")
    if confirmar:
        if q_pessoas < 1 or q_pessoas > 10:
            raise ValueError("O valor deve ser no mínimo 1 e no máximo 10.")
        i = 0
        while i < q_pessoas:
            st.header(f"Pessoa {i+1}:")
            n_pessoa = str(st.text_input(f"{i+1}° Nome:"))
            a_pessoa = float(st.number_input(f"{i+1}° Altura(m):", min_value = 0.5, max_value = 2.75, step = 0.01))
            i_pessoa = int(st.number_input(f"{i+1}° Idade(anos):", min_value = 1, max_value = 10, step = 1))
            
            total_alturas += a_pessoa
            
            if i_pessoa < 16:
                pessoas_menores.append(n_pessoa)
                n_pessoas_menores += 1
            
            i += 1
        
        altura_media = total_alturas / q_pessoas
        p_pessoas_menores = (n_pessoas_menores*100)/q_pessoas

        st.success(f"Altura média: {altura_media}")
        st.success(f"Pessoas com menos de 16 anos: {p_pessoas_menores}")
        j = 0
        while j < n_pessoas_menores:
            st.write(pessoas_menores[j])
            j+=1


except Exception as e:
    st.error(f"ERRO: {e}")