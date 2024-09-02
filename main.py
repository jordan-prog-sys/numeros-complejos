class Complejo:
    def __init__(self, real: float, imaginario: float):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        return f"({self.real} + {self.imaginario}i)"

    def sumar(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return Complejo(real, imaginario)

    def restar(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return Complejo(real, imaginario)

    def multiplicar(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return Complejo(real, imaginario)

    def dividir(self, otro):
        divisor = otro.real ** 2 + otro.imaginario ** 2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / divisor
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / divisor
        return Complejo(real, imaginario)


# Ejemplo de uso:
c1 = Complejo(4, 3)
c2 = Complejo(2, -1)

print("Suma:", c1.sumar(c2))
print("Resta:", c1.restar(c2))
print("Multiplicación:", c1.multiplicar(c2))
print("División:", c1.dividir(c2))6

