class Romano:
    _valores = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100
    }

    def __init__(self, valor_romano):
        self.valor_romano = valor_romano
        self._valor_entero = self._romano_a_entero()

    def _romano_a_entero(self):
        total = 0
        previo = 0
        for letra in reversed(self.valor_romano):
            valor = self._valores[letra]
            if valor < previo:
                total -= valor
            else:
                total += valor
            previo = valor
        return total

    def _entero_a_romano(self, numero):
        conversion = [
            (100, "C"), (90, "XC"), (50, "L"),
            (40, "XL"), (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"), (1, "I")
        ]
        resultado = ""
        for valor, simbolo in conversion:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado

    def __add__(self, otro):
        suma = self._valor_entero + otro._valor_entero
        return Romano(self._entero_a_romano(suma))

    def __str__(self):
        return self.valor_romano


# Ejemplo de uso
if __name__ == "__main__":
    num1 = Romano("X")   # 10
    num2 = Romano("V")   # 5

    resultado = num1 + num2
    print(resultado)  # XV