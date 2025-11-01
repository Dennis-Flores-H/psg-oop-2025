class Vehiculo:
    def __init__(self, velocidad, medio):
        self._velocidad = velocidad  # Atributo protegido
        self.medio = medio

    def get_velocidad(self):
        return self._velocidad


class Bicicleta(Vehiculo):
    def __init__(self, velocidad, medio="terrestre"):
        super().__init__(velocidad, medio)

    def pedalear(self):
        self._velocidad += 5
        print(f"🚴‍♂️ La bicicleta pedalea, nueva velocidad: {self._velocidad} km/h")


class Avion(Vehiculo):
    def __init__(self, velocidad, medio="aéreo"):
        super().__init__(velocidad, medio)

    def volar(self):
        self._velocidad += 100
        print(f"✈️ El avión acelera al volar, nueva velocidad: {self._velocidad} km/h")


# Implementación
bici = Bicicleta(10)
print(f"Bicicleta - Medio: {bici.medio}, Velocidad: {bici.get_velocidad()} km/h")
bici.pedalear()

avion = Avion(200)
print(f"Avión - Medio: {avion.medio}, Velocidad: {avion.get_velocidad()} km/h")
avion.volar()
