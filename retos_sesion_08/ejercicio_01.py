class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    # --- Operaciones aritméticas ---
    def __add__(self, otra):
        num = self.numerador * otra.denominador + otra.numerador * self.denominador
        den = self.denominador * otra.denominador
        return Fraccion(num, den)

    def __sub__(self, otra):
        num = self.numerador * otra.denominador - otra.numerador * self.denominador
        den = self.denominador * otra.denominador
        return Fraccion(num, den)

    def __mul__(self, otra):
        num = self.numerador * otra.numerador
        den = self.denominador * otra.denominador
        return Fraccion(num, den)

    def __truediv__(self, otra):
        num = self.numerador * otra.denominador
        den = self.denominador * otra.numerador
        return Fraccion(num, den)

    # --- Comparaciones ---
    def __eq__(self, otra):
        return self.numerador * otra.denominador == otra.numerador * self.denominador

    def __ne__(self, otra):
        return not self.__eq__(otra)

    def __lt__(self, otra):
        return self.numerador * otra.denominador < otra.numerador * self.denominador

    def __gt__(self, otra):
        return self.numerador * otra.denominador > otra.numerador * self.denominador


# --- Pruebas ---
if __name__ == "__main__":
    f1 = Fraccion(3, 4)
    f2 = Fraccion(5, 6)

    print("f1 =", f1)
    print("f2 =", f2)

    print("Suma:", f1 + f2)
    print("Resta:", f1 - f2)
    print("Multiplicación:", f1 * f2)
    print("División:", f1 / f2)

    print("f1 == f2?", f1 == f2)
    print("f1 != f2?", f1 != f2)
    print("f1 < f2?", f1 < f2)
    print("f1 > f2?", f1 > f2)
