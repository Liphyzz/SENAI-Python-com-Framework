# PROBLEMA: ÁREAS DE DIFERENTES FIGURAS COM 3 MEDIDAS

# --Importação das Bibliotecas--
import streamlit as st

# ---Início da página Stremlit---
TITULO = "Três medidas"
st.title(TITULO)

# --Entrada de Dados--                                                                              (a)
#                                                                                                  bTra
a = st.number_input("Digite a medida A: ", min_value = 0.01, format="%.2f") # b trapézio     (b)    ___   (b)
b = st.number_input("Digite a medida B: ", min_value = 0.01, format="%.2f") # h trapézio    hTra  /|   |\ hTra
c = st.number_input("Digite a medida C: ", min_value = 0.01, format="%.2f") # b triângulo         ‾ ‾‾‾ ‾
#                                                                                             bTri bTra bTri = BTra
#                                                                                              (c) (a) (c)     (d?)
# B trapézio = b trapézio + 2b triângulo

# --Processamento de Dados--
aQuadrado = a * b
aTriangulo = (b * c) / 2
aTrapezio = ((a + (a + 2 * c) ) * b) / 2

# --Saída de Dados--
st.write(f"A área do quadrado é de {aQuadrado:.2f} m²")
st.write(f"A área do triângulo é de {aTriangulo :.2f} m²")
st.write(f"A área do trapézio é de {aTrapezio :.2f} m²")