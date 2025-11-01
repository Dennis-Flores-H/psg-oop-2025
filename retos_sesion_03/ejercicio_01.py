class Atleta:
    def __init__(self, nombre, energia=100, fuerza=10):
        self.nombre = nombre
        self.energia = energia
        self.fuerza = fuerza

    @classmethod
    def crear_atleta(cls, nombre):
        print(f"Atleta {nombre} ha ingresado al juego 🏃")
        return cls(nombre)

    def entrenar(self):
        if self.energia >= 20:
            self.fuerza += 5
            self.energia -= 20
            print(f"{self.nombre} ha entrenado 💪 | Fuerza: {self.fuerza} | Energía: {self.energia}")
        else:
            print(f"{self.nombre} está demasiado cansado para entrenar 💤")

    def descansar(self):
        self.energia += 30
        print(f"{self.nombre} ha descansado 😴 | Energía: {self.energia}")

    def comer(self, comida):
        if comida == "🍔":
            self.energia += 25
            print(f"{self.nombre} ha comido una hamburguesa 🍔 | Energía: {self.energia}")
        else:
            print(f"{self.nombre} no come {comida}")

    @staticmethod
    def comparar_fuerza(a1, a2):
        if a1.fuerza > a2.fuerza:
            print(f"{a1.nombre} es más fuerte que {a2.nombre}")
        elif a1.fuerza < a2.fuerza:
            print(f"{a2.nombre} es más fuerte que {a1.nombre}")
        else:
            print(f"{a1.nombre} y {a2.nombre} tienen la misma fuerza")


# Prueba de los métodos
atleta1 = Atleta.crear_atleta("Erick")
atleta2 = Atleta.crear_atleta("Carlos")

atleta1.entrenar()
atleta2.comer("🍔")
atleta2.entrenar()
atleta1.descansar()

Atleta.comparar_fuerza(atleta1, atleta2)
