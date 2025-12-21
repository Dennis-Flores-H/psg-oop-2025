import random


class DadosDeLaSuerte:
    """
    Juego Dados de la Suerte
    Permite lanzar dos dados y evaluar el resultado segun las reglas
    """

    def __init__(self) -> None:
        self.dado_uno: int = 0
        self.dado_dos: int = 0
        self.suma: int = 0
        self.estado_juego: str = "en_juego"

    def lanzar_dados(self) -> None:
        """Lanza dos dados y calcula la suma."""
        self.dado_uno = random.randint(1, 6)
        self.dado_dos = random.randint(1, 6)
        self.suma = self.dado_uno + self.dado_dos
        print(f"🎲 Dados: {self.dado_uno} + {self.dado_dos} = {self.suma}")

    def evaluar_resultado(self) -> None:
        """Evalúa el resultado del lanzamiento."""
        if self.suma in (7, 11):
            self.estado_juego = "ganado"
        elif self.suma in (2, 3, 12):
            self.estado_juego = "perdido"
        else:
            self.estado_juego = "continuar"

    def mostrar_resultado(self) -> None:
        """Muestra el resultado al jugador."""
        if self.estado_juego == "ganado":
            print("🎉 ¡Ganaste el juego!")
        elif self.estado_juego == "perdido":
            print("💀 Has perdido el juego.")
        else:
            print("🔁 Puedes volver a lanzar los dados.")

    def iniciar_juego(self) -> None:
        """Inicia el flujo principal del juego."""
        while True:
            self.lanzar_dados()
            self.evaluar_resultado()
            self.mostrar_resultado()

            if self.estado_juego in ("ganado", "perdido"):
                break

            respuesta = input("¿Deseas volver a lanzar? (SI/NO): ").lower()
            if respuesta != "si":
                print("👋 Juego finalizado por el jugador.")
                break


juego = DadosDeLaSuerte()
juego.iniciar_juego()
