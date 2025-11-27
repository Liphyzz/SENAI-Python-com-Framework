PI = 3.141592

# Entrada de dados
raio = float(input("Digite o valor do raio: "))

# Processamento de dados
circunferencia = 2 * PI * raio
area = PI * (raio ** 2)

# Saída de dados
print(f'''  Circunferência: {circunferencia:.2f}
            Área: {area:.2f}
            PI: {PI}
        ''')
