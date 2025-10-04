class Vino:
    def __init__(self, nombre, tipo, cepa, anio):
        self.nombre = nombre
        self.tipo = tipo
        self.cepa = cepa
        self.anio = anio


class Queso:
    def __init__(self, nombre, variedad, edad, sal):
        self.nombre = nombre
        self.variedad = variedad
        self.edad = edad
        self.sal = sal


print("Inventario de la Vinoteca 🍷🧀")

# Instancias de vinos
vino1 = Vino("Cabernet Sauvignon Reserva", "tinto", "Cabernet Sauvignon", 2018)
vino2 = Vino("Chardonnay Premium", "blanco", "Chardonnay", 2020)
vino3 = Vino("Merlot Joven", "tinto", "Merlot", 2022)
vino4 = Vino("Rosé Mediterráneo", "rosado", "Garnacha", 2021)

# Instancias de quesos
queso1 = Queso("Queso Manchego", "curado", "12 meses", True)
queso2 = Queso("Queso Brie", "blando", "4 semanas", False)
queso3 = Queso("Queso Parmesano", "duro", "24 meses", True)

# Mostrar información
print("\n--- Vinos ---")
print("Vino 1:", vino1.nombre, vino1.tipo, vino1.cepa, vino1.anio)
print("Vino 2:", vino2.nombre, vino2.tipo, vino2.cepa, vino2.anio)
print("Vino 3:", vino3.nombre, vino3.tipo, vino3.cepa, vino3.anio)
print("Vino 4:", vino4.nombre, vino4.tipo, vino4.cepa, vino4.anio)

print("\n--- Quesos ---")
print("Queso 1:", queso1.nombre, queso1.variedad, queso1.edad, "Sal:", queso1.sal)
print("Queso 2:", queso2.nombre, queso2.variedad, queso2.edad, "Sal:", queso2.sal)
print("Queso 3:", queso3.nombre, queso3.variedad, queso3.edad, "Sal:", queso3.sal)
