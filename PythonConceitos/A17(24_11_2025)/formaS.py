from abc import ABC, abstractmethod
from enum import Enum

class Cor(Enum):
    VERMELHO = "Vermelho"
    AZUL = "Azul"
    VERDE = "Verde"
    AMARELO = "Amarelo"

class Forma(ABC):
    _cor:Cor
   
    @abstractmethod
    def area(self) ->float:
        pass

class Circulo(Forma):
    __raio:float
   
    @property
    def _raio(self) -> float:
        return self.__raio
   
    @_raio.setter
    def _raio(self, raio: float) -> float:
        self.__raio = raio
   
    def __init__(self, raio:float, cor:Cor):
        self._raio = raio
        super()._cor = cor
   
    def area (self) -> float:
        from math import pi
        return pi * (self._raio ** 2)

class Retangulo(Forma):
    __largura:float
    __altura:float

    @property
    def _largura(self) -> float:
        return self.__largura
    @_largura.setter
    def _largura(self, largura:float) -> float:
        self.__largura = largura

    @property
    def _altura(self) -> float:
        return self.__altura
    @_altura.setter
    def _altura(self, altura:float) -> float:
        self.__altura = altura

    def __init__(self, largura:float, altura:float, cor:Cor):
        self._largura = largura
        self._altura = altura
        super()._cor = cor

    def area(self) -> float:
        return self._largura * self._altura