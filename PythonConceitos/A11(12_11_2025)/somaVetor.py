import PySimpleGUI as sg
import numpy as np

n = int(0)

#Lista para guardar o layout da janela
layout =  [
    [sg.Text("Digite a quantidade de números que deseja inserir:")],
    [sg.Input(key='N')],
    [sg.Button("ok"), sg.Button("Cancelar")]
]
janela = sg.Window("Calculadora", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or 'Cancelar' in evento:
        janela.close()
        break
    if evento == "ok":
        try:
            n = int(valores['N'])
            if n <=0:
                sg.popup("Insira somente números positivos")
                continue
            break
        except:
            sg.popup("Por favor, insira um valor válido")
janela.close()
numeros = []#Outra lista

for i in range(n):
    layout = [
        [sg.Text(f"Digite o {i+1}° número")],
        [sg.Input(key='Campeão')],
        [sg.Button("ok"), sg.Button("Cancelar")]
    ]
    janela = sg.Window("Entrada de número", layout)
    
    while True:
        eventos,valores = janela.read()
        print(evento)
        if eventos == sg.WIN_CLOSED or evento == 'Cancelar':
            janela.close()
            break
        if eventos == 'ok':
            try:
                num = float(valores['Campeão'])
                numeros.append(num)
                break
            except:
                sg.popup("Por favor, insira valores válidos!")

janela.close() # Comando para fechar a janela

# Utilização da NumPy
vetor = np.array(numeros)
soma = np.sum(vetor)# ou np.sum(np.array(numeros))
media = np.mean(vetor)# ou np.mean(np.array(numeros))

# Resultados
resultado_layout = [
    [sg.Text("Elementos do vetor")],
    [sg.Text(",".join(map(str, vetor)))],
    [sg.Text(f"Soma dos elementos = {soma}")],
    [sg.Text(f"Media dos elementos = {media}")],
    [sg.Button("Fechar")]
]
resultado_janela = sg.Window("Resultado", resultado_layout)

while True:
    evento_resultado = resultado_janela.read()
    if evento_resultado == sg.WINDOW_CLOSED or 'Fechar' in evento_resultado:
        resultado_janela.close()
        break
resultado_janela.close()

