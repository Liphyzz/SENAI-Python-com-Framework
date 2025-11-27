# ----------- Início Classe -----------

class Retangulo:
    # Membros da classe

    # 1º Membro - Atributos
    __base:float
    __altura:float

    # 2º Membro - Propriedades

    # Propriedade da base
    @property # Pegar o valor do atributo
    def base(self):
        return self.__base
    @base.setter # Definir o valor do atributo
    def base(self, base:float):
        if base < 0:
            base = 0
        self.__base = base

    # Propriedade da altura
    @property # Pegar o valor do atributo
    def altura(self):
        return self.__altura
    @altura.setter # Definir o valor do atributo
    def altura(self, altura:float):
        if altura < 0:
            altura = 0
        self.__altura = altura

    #3º Membro - Construtor
    def __init__(self, base:float, altura:float):
        self.base = base
        self.altura = altura
    
    #4º Membro - Métodos
    def area(self) -> float:
        return self.altura * self.base

    def perimetro(self) -> float:
        return(self.base * 2) + (self.altura * 2)
    
    def diagonal(self) -> float:
        from math import sqrt, pow
        return sqrt(pow(self.base, 2) + pow(self.altura, 2))
    
    def dadosRetangulo(self) -> str:
        saida = f'''Área = {self.area()}\nPerímetro = {self.perimetro()}\nDiagonal = {self.diagonal()} '''
        return saida
    
# ----------- Fim classe ----------- 

# ----------- Início programa principal ----------- 

# Entrada de dados
try:
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    # Instanciar um objeto do tipo retângulo
    retangulo = Retangulo(base, altura)
    # Saída de dados
    print(retangulo.dadosRetangulo())
except ValueError:
    print("Digite um valor numérico para prosseguir.")