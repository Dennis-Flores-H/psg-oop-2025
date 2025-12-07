# Clase base Monstruo
class Monstruo:
    def __init__(self, tipo, fuerza, debilidad):
        self.tipo = tipo
        self.fuerza = fuerza
        self.debilidad = debilidad
    
    def luchar(self, oponente):
        if self.tipo == oponente.fuerza:
            return f"{self.tipo} 🧟‍♂️ gana a {oponente.tipo}"
        elif self.tipo == oponente.debilidad:
            return f"{oponente.tipo} 🧟‍♂️ gana a {self.tipo}"
        elif self.tipo == oponente.tipo:
            return f"{self.tipo} 🧟‍♂️ lucha igual contra {oponente.tipo}"
        else:
            return f"La batalla entre {self.tipo} y {oponente.tipo} es incierta"

# Clases derivadas para los diferentes tipos de monstruos
class Dragon(Monstruo):
    def __init__(self):
        super().__init__("Dragon", "Zombi", "Vampiro")

class Zombi(Monstruo):
    def __init__(self):
        super().__init__("Zombi", "Vampiro", "Dragon")

class Vampiro(Monstruo):
    def __init__(self):
        super().__init__("Vampiro", "Dragon", "Zombi")

# Fabricas para crear monstruos
class Spawner:
    def crear(self):
        pass

class SpawnerDragon(Spawner):
    def crear(self):
        return Dragon()

class SpawnerZombi(Spawner):
    def crear(self):
        return Zombi()

class SpawnerVampiro(Spawner):
    def crear(self):
        return Vampiro()

# Logica del juego
def jugar_batalla():
    while True:
        # Menu de seleccion de monstruos
        print("🧩 Seleccion de Monstruos 🧩")
        print("Jugador 1: Elige tu monstruo (dragon/zombi/vampiro):")
        print("Jugador 2: Elige tu monstruo (dragon/zombi/vampiro):")
        print('Escribe "salir" para terminar.')

        # Seleccion de monstruos por parte de los jugadores
        jugador_1 = input("Jugador 1, elige tu monstruo: ").lower().strip()
        jugador_2 = input("Jugador 2, elige tu monstruo: ").lower().strip()

        if jugador_1 == "salir" or jugador_2 == "salir":
            print("🚶‍♂️ Saliendo del juego.")
            break
        
        # Creacion de monstruos segun la eleccion
        if jugador_1 == "dragon":
            monstruo_1 = SpawnerDragon().crear()
        elif jugador_1 == "zombi":
            monstruo_1 = SpawnerZombi().crear()
        elif jugador_1 == "vampiro":
            monstruo_1 = SpawnerVampiro().crear()
        else:
            print("❌ Opcion no valida para Jugador 1.")
            continue

        if jugador_2 == "dragon":
            monstruo_2 = SpawnerDragon().crear()
        elif jugador_2 == "zombi":
            monstruo_2 = SpawnerZombi().crear()
        elif jugador_2 == "vampiro":
            monstruo_2 = SpawnerVampiro().crear()
        else:
            print("❌ Opcion no valida para Jugador 2.")
            continue

        # Resultados de la batalla
        print(f"\n{monstruo_1.tipo} 🧟‍♂️ listo para luchar")
        print(f"{monstruo_2.tipo} 🧟‍♂️ listo para luchar")
        print(monstruo_1.luchar(monstruo_2))

# Iniciar el juego
jugar_batalla()
