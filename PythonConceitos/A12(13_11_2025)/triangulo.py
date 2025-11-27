
# Problema triângulo sem OOP
# Entrada de dados

# TRIÂNGULO X
print("Inserir as medidas do triângulo X")
ax = int(input("Digite a medida A: "))
bx = int(input("Digite a medida B: "))
cx = int(input("Digite a medida C: "))

# TRIÂNGULO Y
print("Inserir as medidas do triângulo Y")
ay = int(input("Digite a medida A: "))
by = int(input("Digite a medida B: "))
cy = int(input("Digite a medida C: "))

# Processamento de dados
p = (ax + bx + cx) / 2
areax = (p * (p - ax) * (p- bx) * (p- cx)) ** 0.5

p = (ay + by + cy) / 2
areay = (p * (p - ay) * (p- by) * (p- cy)) ** 0.5

# Condicional para verificar qual triângulo é maior

if areax > areay:
    saida = "A área do triângulo X é maior que a área do triângulo Y"
elif areay > areax:
    saida = "A área do triângulo Y é maior que a área do triângulo X"
else:
    saida = "As áreas dos triângulos são iguais"

# Saída de dados
print(f"A área do triângulo X = {areax:.1f}")
print(f"A área do triângulo Y = {areay:.1f}")
print(saida)
