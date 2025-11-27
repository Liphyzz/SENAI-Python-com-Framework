class Terreno:
    # Membros da classe
    # 1º Membro - Atributos
    __largura: float
    __comprimento: float
    
    # 2º Membro - Propriedades

    # Propriedades Largura
    @property
    def largura(self):
        return self.__largura
    @largura.setter
    def largura(self, largura:float):
        self.__largura = largura

    # Propriedades Comprimento
    @property
    def comprimento(self):
        return self.__comprimento
    @comprimento.setter
    def comprimento(self, comprimento:float):
        self.__comprimento = comprimento
    
    # 3º Membro - Construtor
    def __init__(self, largura:float, comprimento:float):
        self.largura = largura
        self.comprimento = comprimento

    # 4º Membro - Métodos
    def __area(self) -> float:
        return self.comprimento * self.largura
    def __preco(self, preco:float) -> float:
        return self.__area() * preco

    def dadosTerreno(self, preco:float) -> str:
        saida = f'''Largura = {self.largura}\nComprimento = {self.comprimento}\nÁrea: {self.__area()}\nPreço: {self.__preco(preco):.2f}'''
        return saida

try:
    largura = float(input("Digite a largura do terreno: "))
    comprimento = float(input("Digite o comprimento do terreno: "))
    preco = float(input("Digite o preço do metro quadrado: "))
    # Instanciar um objeto
    terreno = Terreno(largura, comprimento)
    # Saída de dados
    print(terreno.dadosTerreno(preco))
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número válido.")


    