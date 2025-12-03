from classes import Contribuinte, Fisico, Juridico
import os


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===================================")
    print("        CÁLCULO DE IMPOSTOS        ")
    print("===================================\n")
    while True:
        try:
            quantidadeContribuintes = int(input("Digite a quantidade de contribuintes: "))
            if quantidadeContribuintes < 0:
                raise ValueError
            break
        except ValueError:
            print("ERRO: Escreva um (número inteiro) maior que zero!\n")


    colaboradores = []


    for i in range(quantidadeContribuintes):
        print(f"\n--- Contribuinte {i+1} ---------------------")
        nome = input("Digite o nome: ")
        renda = float(input("Digite a renda atual em R$: "))


        opcao = input("\nTipo de contribuinte:\n1- Pessoa Física\n2- Pessoa Jurídica\nR: ")
        if opcao == "1":
            gastoSaude = float(input("\nDigite o gasto com saúde em R$: "))
            colaborador = Fisico(nome, renda, gastoSaude)
        else:
            numeroFuncionarios = int(input("\nDigite o número de funcionários: "))
            colaborador = Juridico(nome, renda, numeroFuncionarios)
        print("----------------------------------------")


        colaboradores.append(colaborador)

    print("\n==================================")
    print("            RESULTADOS             ")
    print("==================================\n")
    for pessoa in colaboradores:
        print(f"Contribuinte: {pessoa._nome}")
        print(f"Renda Atual: R${pessoa._rendaAtual:.2f}")
       
        if isinstance(pessoa, Fisico):
            print(f"\nGastos com Saúde: R${pessoa._gastosSaude:.2f}")
        elif isinstance(pessoa, Juridico):
            print(f"\nNúmero de Funcionários: {pessoa._numeroFuncionarios}")


        print(pessoa.definicaoImposto())

        print("\n----------------------------------------\n")


if __name__ == "__main__":
    main()