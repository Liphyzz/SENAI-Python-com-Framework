while True:
    a = int(input("Escreva um número de 0 à 10: "))
    b = int(input("Escreva um número de 0 à 10: "))

    if (a < 0 or a > 10) or (b < 0 or b > 10):
        pass
    else:
        break

print("Parabéns, você conseguiu ler e entender que o número não poderia ser maior que 10 ou menor do que 0")