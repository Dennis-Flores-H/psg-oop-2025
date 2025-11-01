class Celula:
    def __init__(self, adn, tipo, energia=100):
        self.__ADN = adn
        self.tipo = tipo
        self.__energia = energia

    # Propiedad de solo lectura para ADN
    @property
    def ADN(self):
        return self.__ADN

    # Propiedad de solo lectura para energía
    @property
    def energia(self):
        return self.__energia

    # Método para comer (aumenta energía)
    def comer(self, cantidad):
        if cantidad > 0:
            self.__energia += cantidad
            print(f"🍽️ La célula ha comido. Energía actual: {self.__energia}")
        else:
            print("❌ Cantidad inválida")

    # Método para dividirse (reduce energía)
    def dividirse(self):
        if self.__energia >= 50:
            self.__energia -= 50
            print("🧫 La célula se ha dividido correctamente.")
            print(f"Energía restante: {self.__energia}")
        else:
            print("⚠️ Energía insuficiente para dividirse.")


# Prueba de la clase
celula1 = Celula("ATCG-2025", "eucariota")
print(f"Tipo: {celula1.tipo}")
print(f"ADN: {celula1.ADN}")
print(f"Energía inicial: {celula1.energia}")

celula1.comer(30)
celula1.dividirse()
celula1.dividirse()
celula1.tipo = "procariota"
print(f"Nuevo tipo: {celula1.tipo}")
