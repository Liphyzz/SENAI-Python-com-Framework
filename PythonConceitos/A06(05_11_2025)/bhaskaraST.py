# PROBLEMA: RESOLVER FÓRMULA DE BHASKARA

# --Importação de Bibliotecas--
from streamlit import header, write, text_input, button, warning, success, error
from math import pow, sqrt

# --Variáveis pré-definidas--
delta = "(esperando dados...)"

# --Funções pré-definidas--
def calculoDelta(delta):
    valor = (sqrt(delta)) / (2*a)
    return valor

# ---Início da página Stremlit---
header('Calculadora de Bháskara')
write("Calculadora de raízes de uma equação de segundo grau")
write("ax² + bx + c = 0")


# --Entrada de dados--
a = text_input('Digite o valor de a:', icon = "")
b = text_input('Digite o valor de b:')
c = text_input('Digite o valor de c:')

# -b ± √(b²-4.a.c)
#—————————————————
#       2a        

# --Processamento de dados--
if button("Calcular raízes"):
    try:
        a = float(a)
        b= float(b)
        c = float(c)
        delta = pow(b, 2) - 4 * a * c
        if delta < 0:
            warning("A equação não possui raízes reais")
        elif delta == 0:
            raiz = round(-b + calculoDelta(delta), ndigits=3)
            success(f"A equação possui uma raíz real: {raiz}")
        else:
            raiz1 = round(-b + calculoDelta(delta), ndigits=3)
            raiz2 = round(-b - calculoDelta(delta), ndigits=3)
            success(f"As raízes da equação são:")
            success(f"• Raiz 1: {raiz1}")
            success(f"• Raiz 2: {raiz2}")
    except ValueError:
        error("Por favor, insira valores válidos para a, b e c.")
    except ZeroDivisionError:
        error("O valor de 'a' não pode ser zero em uma equação de segundo grau.")

# --Saída de Dados--
write("O valor de delta é ", delta)