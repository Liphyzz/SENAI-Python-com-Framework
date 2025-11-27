class calculadoraCirculo:
    #Atributo da classe
    PI = 3.14

    #Métodos estáticos da classe
    @staticmethod
    def circunferencia(raio) -> float:
        return 2 * calculadoraCirculo.PI * raio
    
    @staticmethod
    def area(raio) -> float:
        return calculadoraCirculo.PI * (raio ** 2)