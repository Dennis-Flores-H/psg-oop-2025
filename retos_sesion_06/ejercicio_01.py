class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino

    def info(self):
        print(f"🧍 Pasajero: {self.nombre}, Destino: {self.destino}")


class Minibus:
    def __init__(self, ruta, paradas):
        self.ruta = ruta
        self.paradas = paradas
        self.pasajeros = []
        self.indice_parada = 0
        self.direccion = 1  # 1 ida, -1 vuelta

    def mover(self):
        parada_actual = self.paradas[self.indice_parada]
        print(f"🚌 Parada actual: {parada_actual}")
        self.bajar()
        self.indice_parada += self.direccion
        if self.indice_parada == len(self.paradas) - 1 or self.indice_parada == 0:
            self.direccion *= -1

    def subir(self, pasajero):
        if pasajero.destino in self.paradas:
            self.pasajeros.append(pasajero)
            print(f"✅ {pasajero.nombre} sube al minibus (Destino: {pasajero.destino})")
        else:
            print(f"❌ {pasajero.nombre} no puede subir, destino fuera de ruta")

    def bajar(self):
        parada_actual = self.paradas[self.indice_parada]
        bajan = [p for p in self.pasajeros if p.destino == parada_actual]
        for p in bajan:
            print(f"⬇️ {p.nombre} baja en {parada_actual}")
            self.pasajeros.remove(p)

    def mostrar_pasajeros(self):
        print("👥 Pasajeros a bordo:")
        for p in self.pasajeros:
            p.info()


# Ejemplo de uso
minibus = Minibus(42, ["Arce", "Prado", "Perez"])
juan = Pasajero("Juan", "Prado")
ana = Pasajero("Ana", "Perez")

minibus.subir(juan)
minibus.subir(ana)

for _ in range(5):
    minibus.mover()
    minibus.mostrar_pasajeros()