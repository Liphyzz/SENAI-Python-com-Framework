from streamlit import title, header, number_input, columns, success, button, warning, balloons
title("🎯 Simulação de lançamento de dardos 🎯")

'''Simulação de lançamento de três dardos. O objetivo do aplicativo é 
mostrar o dardo com a maior distância'''

# Entrada de dados
header("Insira a distância percorrida (em metros) por cada um dos 3 dardos: ")
coluna1, coluna2, coluna3 = columns(3)
with coluna1:
    dardo1 = number_input("Distância do 1º dardo", min_value=0.0, step=1.0)
with coluna2:
    dardo2 = number_input("Distância do 2º dardo", min_value=0.0, step=1.0)
with coluna3:
    dardo3 = number_input("Distância do 3º dardo", min_value=0.0, step=1.0)
maior_distancia = float(max(dardo1, dardo2, dardo3))

# Estrutura de controle de decisão
if (dardo1 > dardo2):
    if (dardo1 > dardo3):
        dardo_vencedor = "dardo 1"
        pre_texto = "O dardo com a maior distância registrada foi o "
        resultado = "vitória"

    elif (dardo1 == dardo3):
        dardo_vencedor = "dardos 1 e 3"
        pre_texto = "Os dardos com a maiores distâncias resgistradas foram os "
        resultado = "empate"

    else:
        dardo_vencedor = "dardo 3"
        pre_texto = "O dardo com a maior distância registrada foi o "
        resultado = "vitória"

elif (dardo1 == dardo2):
    if (dardo1 > dardo3):
        dardo_vencedor = "dardos 1 e 2"
        pre_texto = "Os dardos com a maiores distâncias resgistradas foram os "
        resultado = "empate"

    elif (dardo1 == dardo3):
        dardo_vencedor = "dardos 1, 2 e 3"
        pre_texto = "Os dardos com a maiores distâncias resgistradas foram os "
        resultado = "empate"

    else:
        dardo_vencedor = "dardo 3"
        pre_texto = "O dardo com a maior distância registrada foi o "
        resultado = "vitória"

else:
    if (dardo2 > dardo3):
        dardo_vencedor = "dardo 2"
        pre_texto = "O dardo com a maior distância registrada foi o "
        resultado = "vitória"

    elif (dardo2 == dardo3):
        dardo_vencedor = "dardos 2 e 3"
        pre_texto = "Os dardos com a maiores distâncias resgistradas foram os "
        resultado = "empate"

    else:
        dardo_vencedor = "dardo 3"
        pre_texto = "O dardo com a maior distância registrada foi o "
        resultado = "vitória"


# Saída de dados
if button("Apresentar dados de lançamento"):
    if resultado == "vitória":
        success(f"{pre_texto}{dardo_vencedor} com {maior_distancia}")
        balloons()
        
    else:
        warning(f"{pre_texto}{dardo_vencedor} com {maior_distancia}")


