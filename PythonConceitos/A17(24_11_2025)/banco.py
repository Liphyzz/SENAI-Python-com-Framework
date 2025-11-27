from abc import ABC , abstractmethod

class Conta(ABC):
    __numero:str
    __saldo:float

    @property
    def _numero(self) -> str:
        return self.__numero
    @_numero.setter
    def _numero(self, numero:str) -> str:
        if numero == "" or numero == None:
            raise ValueError("Valor inválido")
        else:
            self.__numero = numero
        
    @property
    def _saldo(self) -> float:
        return self.__saldo
    
    @_saldo.setter
    def _saldo(self, saldo:float) -> float:
        if saldo < 0:
            raise ValueError("Valor inválido para saldo de conta")
        else:
            self.__saldo = saldo
        
    def __init__(self, numero:str, saldo:float):
        self._numero = numero
        self._saldo = saldo
    
    def depositar(self, valor:float) -> None:
        self._saldo += valor

    def sacar (self, valor:float) -> None:
        self._saldo -= valor
# Fim super classe

class ContaPoupanca(Conta):
    __taxaDeJuros:float
    
    @property
    def _taxa(self) -> float:
        return self.__taxaDeJuros
    @_taxa.setter
    def _taxa(self, valor:float) -> float:
        if valor < 0:
            raise ValueError("Valor de taxa de juros inválida")
        else:
            self.__taxaDeJuros = valor
    
    def __init__(self, numero, saldo, taxa):
        super().__init__(numero, saldo)
        self._taxa = taxa
    
    def aplicarJuros(self) -> None:
        self._saldo += self._saldo * ( self._taxa / 100 )
# Fim da classe Conta Poupança

class ContaEmpresa(Conta):
    __limite:float

    @property
    def _limite(self) -> float :
        return self.__limite
    @_limite.setter
    def _limite(self, limite:float) -> float:
        if limite < 0:
            raise ValueError("Valor inválido")
        else:
            self.__limite = limite
    
    def __init__(self, numero, saldo, limite):
        super().__init__(numero, saldo)
        self._limite = limite
    
    def solicitarCredito(self, valor:float) -> float:
        self._limite -= valor
        self._saldo += valor
    
# Fim classes

conta1 = ContaEmpresa("123456", 20000.00, 50000.00)
conta2 = ContaPoupanca("666", 500, 25)



