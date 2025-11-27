class ContaPessoaFisica: # Super Classe
    # 1º Membro - Atributos privados 
    __numeroDaConta:int
    __titular:str
    __saldo:float

    # 2º Membro - Propriedades
    # Propriedade Numero da Conta
    @property 
    def _numeroDaConta(self) -> int:
        return self.__numeroDaConta
    @_numeroDaConta.setter
    def _numeroDaConta(self, numeroDaConta:int) -> int:
        self.__numeroDaConta = numeroDaConta
    # Propriedade Titular
    @property
    def _titular(self) -> str:
        return self.__titular
    @_titular.setter
    def _titular(self, titular:str) -> str:
        self.__titular = titular
    # Propriedade Saldo
    @property
    def _saldo(self) -> float:
        return self.__saldo
    @_saldo.setter
    def _saldo(self, saldo:float) -> float:
        self.__saldo = saldo

    # 3º Membro - Construtor
    def __init__(self, numeroDaConta:int, titular:str, saldo:float):
        self.__numeroDaConta = numeroDaConta
        self.__saldo = saldo
        self.__titular = titular
    
    # 4º Membro - Métodos
    def depositar(self, deposito:float) -> float:
        self._saldo += deposito 
    def saque(self, saque:float) -> float:
        self._saldo -= saque + 5.00
    def dados(self) -> str:
        saida = (f'''
        Número: {self._numeroDaConta}
        Titular: {self._titular}
        Saldo: {self._saldo}
        ''')
        return saida
    
    # Fim Super Classe

class ContaPessoaJuridica(ContaPessoaFisica): # Sub classe da classe ContaPessoaFisica
    # 1º Membro - Atributos
    __limite:float

    # 2º Membro - Propriedades
    @property
    def _limite(self) -> float:
        return self.__limite
    @_limite.setter
    def _limite(self, limite:float) -> float:
        self.__limite = limite
    
    # 3º Membro - Construtor
    def __init__(self, numeroDaConta:int, titular:str, saldo:float, limite:float):
        super().__init__(numeroDaConta, titular, saldo)
        self._limite = limite
    
    # 4º Membro - Métodos
    def limiteDisponivel(self) -> float:
        return self._limite

    def saque(self, saque:float) -> float: #Sobrescrita do método saque
        self._saldo -= saque
        return self._saldo

    def dados(self) -> str:
        dados = super().dados()
        saida = (f''' {super().dados()}Limite: {self._limite}
        ''')
        return saida


    # -- Fim Sub Classe

class ContaPoupanca(ContaPessoaFisica):
    # 1º Membro - Atributos
    __taxaDeJuros = 0.05

    # 2º Membro - Propriedades
    @property 
    def _taxaDeJuros(self) -> float:
        return self.__taxaDeJuros

    # 3º Membro - Construtor
    def __init__(self, numeroDaConta, titular, saldo):
        super().__init__(numeroDaConta, titular, saldo)

    # 4º Membro - Métodos
    def atualizarSaldo(self):
        self._saldo += self._saldo * self._taxaDeJuros
        return self._saldo

    def saque(self, quantia:float) -> float: #Sobrescrita do método saque
        self._saldo -= quantia
        return self._saldo
    



# -- Fim Classes --


# Programa principal

conta1 = ContaPessoaFisica(123456, "Clodoaldo", 1000)
conta2 = ContaPessoaJuridica(654321, "Adriano", 500, 100)
conta3 = ContaPoupanca(789, "Victor", 100)

# Saída de dados 1
print(f'''{conta1.dados()}{conta2.dados()}{conta3.dados()}''')

conta1.depositar(200)
print(f"Saldo após depósito na conta 1: {conta1._saldo}")
conta1.saque(50)
print(f"Saldo após saque na conta 1: {conta1._saldo}")

# Saída de dados 2
conta2.saque(100)
print(f"Saldo após saque na conta 2: {conta2._saldo}")
conta2.depositar(300)
print(f"Saldo após depósito na conta 2: {conta2._saldo}")

# Saída de dados 3
conta3.depositar(200)
print(f"Saldo após depósito na conta 3: {conta3._saldo}")
conta3.saque(50)
print(f"Saldo após saque na conta 3: {conta3._saldo}")
