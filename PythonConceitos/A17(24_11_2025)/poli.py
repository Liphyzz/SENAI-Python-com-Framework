class Trabalhador:
    #1° Membro da classe - Atributos
    __nome:str
    __jornada:float

    #2° Membro da classe - Propriedade
    #Propriedade do atributo nome
    @property
    def _nome(self)->str:
        return self.__nome
    @_nome.setter
    def _nome(self, nome:str)-> str:
        if nome == "" or nome == None:
            raise ValueError("Nome inválido")
        else:
            self.__nome = nome
     #Propriedade do atributo jornada      
    @property
    def _jornada(self)->float:
        return self.__jornada
    @_jornada.setter
    def _jornada(self, jornada:float)-> float:
        if jornada <= 0:
            raise ValueError("Jornada inválida")
        else:
            self.__jornada = jornada
   
    #3° Membro - Construtor
    def __init__(self, nome:str, jornada:float):
        self._nome = nome
        self._jornada = jornada

    #4° Membro - Métodos
    def pagamento(self)->float:
        pass
#---Fim super classe Trabalhador---#

class EmpregadoSenai(Trabalhador):
    #1° membro - Atributos
    __valorPorHora:float

    #2° Membro - Propriedade
    @property
    def _valorPorHora(self) ->float:
        return self.__valorPorHora
    @_valorPorHora.setter
    def _valorPorHora(self, valor) -> float:
        if valor <= 0:
            raise ValueError("Valor por hora invalido")
        else:
            self.__valorPorHora = valor
   
    #3° Membro - Construtor
    def __init__(self, nome, jornada, valor):
        super().__init__(nome, jornada)
        self._valorPorHora = valor
   
    #4° Membro - Metodo
    def pagamento(self) ->float:
        pagamento = self._jornada * self._valorPorHora
        return pagamento
#---Fim sub classe ------

class Terceirizado(EmpregadoSenai):
    #1° Membro - Atributo
    __adicional = 0.2

    #2° Membro - Construtor
    def __init__(self, nome, jornada, valor):
        super().__init__(nome, jornada, valor)
   
    #3° Membro - Metodo
    def pagamento(self) ->float:
        pagamento = super().pagamento() * (1 + self.__adicional)
        return pagamento
#----Fim sub sub classe Terceirizado ----#

#----Inicio codigo principal-------
lista = []
funcionario:Trabalhador


def main():
    quantidade = int(input("Digite a quantidade de funcionarios a ser inserida: "))

    for i in range(quantidade):
        print(f"Colaborador n° {i+1}")
        colaborador = input("O colaborador eh terceirazado (s/n) ? ")
        nome = input("Nome do colaborador: ")
        horas = int(input("Horas trabalhadas: "))
        valor = float(input("Valor da hora do colaborador: "))
        if colaborador is "s":
            funcionario  = Terceirizado(nome, horas, valor)
        else:
            funcionario = EmpregadoSenai(nome, horas, valor)
        lista.append(funcionario)
    print("\nPagamentos dos colaboradores:")
    for colaborador in lista:
        print(f"{colaborador._nome} - R$ {colaborador.pagamento():.2f}")

if __name__ == "__main__":
    main()
#---- fim codigo principal----#