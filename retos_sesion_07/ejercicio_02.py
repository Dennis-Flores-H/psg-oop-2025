class Instrumento:
    def __init__(self, material):
        self._material = material

    def tocar(self):
        print("El instrumento está sonando...")


class Guitarra(Instrumento):
    def __init__(self, material, num_cuerdas):
        super().__init__(material)
        self._num_cuerdas = num_cuerdas

    def tocar(self):
        print(f"🎸 La guitarra hace: strum (cuerdas: {self._num_cuerdas})")


class Piano(Instrumento):
    def __init__(self, material, num_teclas):
        super().__init__(material)
        self._num_teclas = num_teclas

    def tocar(self):
        print(f"🎹 El piano hace: plin (teclas: {self._num_teclas})")


class Tambor(Instrumento):
    def __init__(self, material, tipo_percusion):
        super().__init__(material)
        self._tipo_percusion = tipo_percusion

    def tocar(self):
        print(f"🥁 El tambor hace: boom (percusión: {self._tipo_percusion})")


# Ejemplo de uso (Polimorfismo)
def ejecutar_instrumento(instr):
    instr.tocar()


if __name__ == "__main__":
    instrumentos = [
        Guitarra("madera", 6),
        Piano("madera", 88),
        Tambor("cuero", "mano")
    ]

    for inst in instrumentos:
        ejecutar_instrumento(inst)