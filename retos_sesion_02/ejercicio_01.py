class Animal:
    origen = "feral"

    def __init__(self, especie, tipo, lugar):
        self.especie = especie
        self.tipo = tipo
        self.lugar = lugar


print("Animales registrados en el zoológico... 🦁🐍🦅")

# Instancias de animales
animal1 = Animal("León", "mamífero", "Sabana africana")
animal2 = Animal("Tigre", "mamífero", "Selva asiática")
animal3 = Animal("Cocodrilo", "reptil", "Río Amazonas")
animal4 = Animal("Águila", "ave", "Montañas rocosas")

# Mostrar información de los animales
print("Animal 1:", animal1.origen, animal1.especie, animal1.tipo, animal1.lugar)
print("Animal 2:", animal2.origen, animal2.especie, animal2.tipo, animal2.lugar)
print("Animal 3:", animal3.origen, animal3.especie, animal3.tipo, animal3.lugar)
print("Animal 4:", animal4.origen, animal4.especie, animal4.tipo, animal4.lugar)