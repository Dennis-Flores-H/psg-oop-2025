class Departamento:
    def __init__(self, numero, inquilinos):
        self.numero = numero
        self.inquilinos = inquilinos

    def info(self):
        print(f"🏠 Departamento {self.numero} - Inquilinos: {', '.join(self.inquilinos)}")


class Oficina:
    def __init__(self, numero, telefono):
        self.numero = numero
        self.telefono = telefono

    def info(self):
        print(f"💼 Oficina {self.numero} - Teléfono: {self.telefono}")


class Piso:
    def __init__(self, numero):
        self.numero = numero
        self.departamentos = []
        self.oficinas = []

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def agregar_oficina(self, oficina):
        self.oficinas.append(oficina)

    def mostrar_detalles(self):
        print(f"\n🔹 Piso {self.numero}")
        for d in self.departamentos:
            d.info()
        for o in self.oficinas:
            o.info()


class Edificio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.pisos = []

    def agregar_piso(self, piso):
        self.pisos.append(piso)

    def mostrar_informacion(self):
        print(f"\n🏢 Edificio {self.nombre} - Dirección: {self.direccion}")
        for p in self.pisos:
            p.mostrar_detalles()


# Ejemplo de uso
edificio = Edificio("Torre La Paz", "Av. Camacho #123")
piso1 = Piso(1)
piso1.agregar_departamento(Departamento(101, ["Carlos", "Ana"]))
piso1.agregar_oficina(Oficina("1A", "22223333"))

piso2 = Piso(2)
piso2.agregar_departamento(Departamento(201, ["Luis"]))
piso2.agregar_oficina(Oficina("2B", "22224444"))

edificio.agregar_piso(piso1)
edificio.agregar_piso(piso2)
edificio.mostrar_informacion()
