# PROBLEMA: CALCULAR PREÇO DE UM TERRENO

# --Declaração de Variáveis--
largura: float
comprimento: float

# --Entrada de Dados --
largura = float(input("Insira a largura do terreno em m²: "))
comprimento = float(input("Insira o comprimento do terreno em m²: "))
valor_mQuadrado = float(input("Digite o valor do metro quadrado do terreno: ") )

# --Processamento de Dados --
area = largura * comprimento
preco = area * valor_mQuadrado

# --Saída de Dados--
print(f"O preço desse terreno é: R${preco}")