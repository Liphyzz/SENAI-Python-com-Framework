# PROBLEMA: CADASTRO DE PESSOAS

# --Importação de Bibliotecas--
import streamlit as st

# --Início do Streamlit--
TITULO = "Registro de pessoas"
st.set_page_config(page_title=TITULO)
st.title(TITULO)

# --Variáveis de estado--
if "confirmado" not in st.session_state:
    st.session_state.confirmado = False
if "q_pessoas" not in st.session_state:
    st.session_state.q_pessoas = None
if "exibir" not in st.session_state:
    st.session_state.exibir = False

# --Entrada de Dados--
try:
    q_pessoas = st.text_input("Quantas pessoas serão digitadas? (máx. 10)")
    confirmar = st.button("Confirmar")

    # --- Quando clica em confirmar ---
    if confirmar:
        if not q_pessoas.strip():
            st.warning("⚠️ Digite um número entre 1 e 10 antes de continuar.")
            st.stop()
        try:
            q_pessoas = int(q_pessoas)
        except ValueError:
            st.error("❌ Valor inválido. Digite um número inteiro entre 1 e 10.")
            st.stop()
        if q_pessoas < 1 or q_pessoas > 10:
            st.error("❌ O número de pessoas deve ser entre 1 e 10.")
            st.stop()

        # Se passou na validação, salva no estado
        st.session_state.q_pessoas = q_pessoas
        st.session_state.confirmado = True

    # --- Se já confirmado anteriormente ---
    if st.session_state.confirmado == True:
        total_alturas = 0.0
        pessoas_menores = []
        n_pessoas_menores = 0
        q_pessoas = st.session_state.q_pessoas

        st.write("")
        st.header(f"Cadastro de {q_pessoas} pessoas:")

        for i in range(q_pessoas):
            st.subheader(f"Pessoa {i+1}:")
            n_pessoa = st.text_input(f"Nome:", key=f"nome_{i}")
            a_pessoa = st.number_input(f"Altura (m):", min_value=0.5, max_value=2.75, step=0.01, key=f"altura_{i}")
            i_pessoa = st.number_input(f"Idade (anos):", min_value=1, max_value=120, step=1, key=f"idade_{i}")

            total_alturas += a_pessoa
            if i_pessoa < 16:
                pessoas_menores.append(n_pessoa)
                n_pessoas_menores += 1

        # --- Botão para exibir resultados ---
        st.write("")
        exibir = st.button("📊 Exibir resultado")
        if exibir:
            st.session_state.exibir = True

        # --- Mostrar resultados somente após clicar ---
        if st.session_state.exibir:
            if q_pessoas > 0:
                altura_media = total_alturas / q_pessoas
                p_pessoas_menores = (n_pessoas_menores * 100) / q_pessoas

                st.success(f"Altura média: {altura_media:.2f} m")
                st.success(f"Pessoas com menos de 16 anos: {p_pessoas_menores:.1f}%")

                if pessoas_menores:
                    st.write("Menores de 16 anos:")
                    for nome in pessoas_menores:
                        st.write(f"- {nome}")

        # --- Botão para reiniciar o cadastro ---
        if st.button("🔄 Reiniciar cadastro"):
            st.session_state.clear()
            st.rerun()

except Exception as e:
    st.error(f"ERRO: {e}")