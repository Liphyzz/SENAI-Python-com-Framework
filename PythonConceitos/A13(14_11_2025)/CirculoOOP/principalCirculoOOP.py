from calculadoraOOP import calculadoraCirculo

# Entrada de dados
raio = float(input("Digite o valor do raio: "))

# Processamento de dados
circunferencia = calculadoraCirculo.circunferencia(raio)
area = calculadoraCirculo.area(raio)

# Saída de dados
print(f'''  Circunferência: {circunferencia:.2f}
            Área: {area:.2f}
            PI: {calculadoraCirculo.PI}
        ''')