class BeatBox:
    __instancia = None
    pista = "Ninguna"
    volumen = 50
    efecto = "Ninguno"

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

    def seleccionar_pista(self):
        self.pista = input("Ingresa el nombre de la pista: ")
        print(f"Pista seleccionada: {self.pista}")

    def ajustar_volumen(self):
        cambio = int(input("Ingresa un número para subir/bajar el volumen (+/-): "))
        self.volumen += cambio
        if self.volumen < 0:
            self.volumen = 0
        if self.volumen > 100:
            self.volumen = 100
        print(f"Volumen actual: {self.volumen}")

    def aplicar_efecto(self):
        efecto = input("Elige un efecto (eco, reverb, distorsion): ").lower()
        if efecto in ["eco", "reverb", "distorsion"]:
            self.efecto = efecto
            print(f"Efecto aplicado: {self.efecto}")
        else:
            print("Efecto no válido.")

    def mostrar_estado(self):
        print("Estado actual de la consola:")
        print(f"Pista: {self.pista}")
        print(f"Volumen: {self.volumen}")
        print(f"Efecto: {self.efecto}")


consola = BeatBox()

while True:
    print("===============")
    print("Consola BeatBox")
    print("1. Seleccionar pista")
    print("2. Ajustar volumen")
    print("3. Aplicar efecto")
    print("4. Mostrar estado")
    print("5. Salir")
    print("===============")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        consola.seleccionar_pista()
    elif opcion == "2":
        consola.ajustar_volumen()
    elif opcion == "3":
        consola.aplicar_efecto()
    elif opcion == "4":
        consola.mostrar_estado()
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")
