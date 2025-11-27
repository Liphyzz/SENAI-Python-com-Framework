class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def mais_velha(self, outra_pessoa):
        if self.idade > outra_pessoa.idade:
            return f"{self.nome} é a pessoa mais velha"
        elif self.idade < outra_pessoa.idade:
            return f"{outra_pessoa.nome} é a pessoa mais velha"
        else:
            return "As idades são iguais"


class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def media_salarial(self, outra_pessoa):
        media = (self.salario + outra_pessoa.salario)/2
        return media