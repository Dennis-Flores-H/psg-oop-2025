
class Martillo:
    def __init__(self, peso, material_mango):
        self._peso = peso
        self._material_mango = material_mango

    def usar(self):
        print(f"🔨 Golpeando con el martillo de {self._peso}kg con mango de {self._material_mango}")


class Destornillador:
    def __init__(self, tipo_punta, largo):
        self._tipo_punta = tipo_punta
        self._largo = largo

    def usar(self):
        print(f"🪛 Ajustando tornillos con destornillador {self._tipo_punta} de {self._largo}cm")


class LlaveInglesa:
    def __init__(self, tamaño, material):
        self._tamaño = tamaño
        self._material = material

    def usar(self):
        print(f"🔧 Apretando tuercas con llave inglesa tamaño {self._tamaño} hecha de {self._material}")


# Ejemplo de uso (Duck Typing)
def usar_herramienta(herramienta):
    herramienta.usar()


if __name__ == "__main__":
    h1 = Martillo(1.5, "madera")
    h2 = Destornillador("plana", 15)
    h3 = LlaveInglesa(12, "acero")

    usar_herramienta(h1)
    usar_herramienta(h2)
    usar_herramienta(h3)
