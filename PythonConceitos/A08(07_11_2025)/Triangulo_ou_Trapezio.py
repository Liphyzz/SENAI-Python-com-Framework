import streamlit as st

def Tri_ou_tra(a,b,c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        resultado = "triângulo"
    else:
        resultado = "trapézio"

    return resultado

TITULO = "É triângulo? E trapézio?"

st.set_page_config(page_title=TITULO, page_icon="🔺")

st.title(TITULO)

st.header("Insira as medidas dos lados 1, 2 e 3 para chegar no perímetro de um triângulo")

l1 = st.number_input("Insira o valor do lado 1(cm):", format="%.2f", step=1.0)
l2 = st.number_input("Insira o valor do lado 2(cm):", format="%.2f", step=1.0)
l3 = st.number_input("Insira o valor do lado 3(cm):", format="%.2f", step=1.0)

forma = Tri_ou_tra(l1,l2,l3)

ptriangulo = l1 + l2 + l3
atrapezio = ((l1 + l2) * l3)/2

if forma == "triângulo":
    st.success(f"Estas medidas formam um triângulo com perímetro de {ptriangulo}cm")
elif forma == "trapézio":
    if l2 < l1:
        st.warning(f"Estas medidas não formam um triângulo, mas servem como 'B, b e h' de um trapézio com uma área de {atrapezio}cm²")
    else: 
        st.error(f"Estas medidas não formam um triângulo e nem servem como 'B, b e h' de um trapézio!")
