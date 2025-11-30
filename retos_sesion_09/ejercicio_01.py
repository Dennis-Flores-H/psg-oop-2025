import random

class PiedraPapelTijera:
    __instancia = None
    jugador_gana = 0
    computadora_gana = 0
    opciones = ["piedra", "papel", "tijera"]

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

    def iniciarPartida(self):
        jugador = input("Elige piedra, papel o tijera: ").lower()
        computadora = random.choice(self.opciones)
        print(f"La computadora eligió: {computadora}")

        if jugador == computadora:
            print("Empate.")
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            print("¡Ganaste!")
            self.jugador_gana += 1
        else:
            print("Perdiste.")
            self.computadora_gana += 1

    def mostrarPuntaje(self):
        print(f"Puntaje → Jugador: {self.jugador_gana} | Computadora: {self.computadora_gana}")

    def reiniciarJuego(self):
        self.jugador_gana = 0
        self.computadora_gana = 0
        print("El juego ha sido reiniciado.")


juego = PiedraPapelTijera()

while True:
    print("===============")
    print("Piedra, Papel o Tijera")
    print("1. Iniciar partida")
    print("2. Mostrar puntajes")
    print("3. Reiniciar juego")
    print("4. Salir")
    print("===============")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        juego.iniciarPartida()
    elif opcion == "2":
        juego.mostrarPuntaje()
    elif opcion == "3":
        juego.reiniciarJuego()
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")
