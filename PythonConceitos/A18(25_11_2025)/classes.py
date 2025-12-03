from abc import ABC, abstractmethod

class Contribuinte(ABC):
    __nome: str
    __rendaAtual: float


    @property
    def _nome(self) -> str:
        return self.__nome
    @_nome.setter
    def _nome(self, nome) -> str:
        if nome == "" or nome == None:
            raise ValueError("Valor inválido")
        else:
            self.__nome = nome
   
    @property
    def _rendaAtual(self) -> float:
        return self.__rendaAtual
    @_rendaAtual.setter
    def _rendaAtual(self, _rendaAtual) -> float:
        if _rendaAtual < 0 or _rendaAtual == None:
            raise ValueError("Valor inválido")
        else:
            self.__rendaAtual = _rendaAtual


    @abstractmethod
    def definicaoImposto(self):
        pass


    def __init__(self, nome: str, rendaAtual: float):
        self._nome = nome
        self._rendaAtual = rendaAtual


class Fisico(Contribuinte):
    __gastosSaude: float


    @property
    def _gastosSaude(self) -> float:
        return self.__gastosSaude
    @_gastosSaude.setter
    def _gastosSaude(self, gastosSaude) -> float:
        if gastosSaude < 0 or gastosSaude == None:
            raise ValueError("Valor inválido")
        else:
            self.__gastosSaude = gastosSaude


    def __init__(self, nome: str, rendaAtual: float, gastosSaude: float):
        super().__init__(nome, rendaAtual)
        self._gastosSaude = gastosSaude
       
    def definicaoImposto(self) -> float:
        renda = self._rendaAtual
        imposto = 0.15 * renda if renda < 20000 else 0.25 * renda
        if self._gastosSaude > 0:
            imposto -= 0.5 * self._gastosSaude
        return f"Imposto a pagar: R${imposto:.2f}"


class Juridico(Contribuinte):
    __numeroFuncionarios: int


    @property
    def _numeroFuncionarios(self):
        return self.__numeroFuncionarios
    @_numeroFuncionarios.setter
    def _numeroFuncionarios(self, numeroFuncionarios):
        if numeroFuncionarios < 0 or numeroFuncionarios == None:
            raise ValueError("Valor inválido")
        else:
            self.__numeroFuncionarios = numeroFuncionarios


    def __init__(self, nome: str, rendaAtual: float, numeroFuncionarios: int):
        super().__init__(nome, rendaAtual)
        self._numeroFuncionarios = numeroFuncionarios
   
    def definicaoImposto(self) -> float:
        renda = self._rendaAtual
        if self._numeroFuncionarios > 10:
            imposto = 0.14 * renda
        else:
            imposto = 0.16 * renda
        return f"Imposto a pagar: R${imposto:.2f}"