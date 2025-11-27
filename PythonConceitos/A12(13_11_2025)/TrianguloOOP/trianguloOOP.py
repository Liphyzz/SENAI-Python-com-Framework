class triangulo:
    # Atributos
    a:int
    b:int
    c:int

    def area(self):
        p = (self.a + self.b + self.c) / 2
        area = (p * (p - self.a) * (p - self.b) * (p - self.c))
        return area
    