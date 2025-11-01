class Nadador:
    def nadar(self):
        print("🏊 El personaje está nadando en el agua.")
    def mostrar(self):
        print("Tipo: Nadador | Habilidad: Nadar")

class Volador:
    def volar(self):
        print("🕊️ El personaje está volando en el aire.")
    def mostrar(self):
        print("Tipo: Volador | Habilidad: Volar")

class Pez(Nadador):
    def mostrar(self):
        print("🐠 Soy un Pez y puedo nadar.")
        self.nadar()

class Pajaro(Volador):
    def mostrar(self):
        print("🐦 Soy un Pájaro y puedo volar.")
        self.volar()

class Pato(Nadador, Volador):
    def mostrar(self):
        print("🦆 Soy un Pato, puedo nadar y volar.")
        self.nadar()
        self.volar()

# Implementación
pez = Pez()
pez.mostrar()

pajaro = Pajaro()
pajaro.mostrar()

pato = Pato()
pato.mostrar()
