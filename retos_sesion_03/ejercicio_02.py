class Cocinero:
    recetas = {
        "pan": {"harina", "agua"},
        "pizza": {"harina", "agua", "sal", "tomate", "queso"},
        "galleta": {"harina", "agua", "sal", "chocolate"}
    }

    def __init__(self, ingredientes):
        self.ingredientes = set(ingredientes)
        self.productividad = 0

    @classmethod
    def crear_cocinero(cls, ingredientes):
        print(f"Nuevo cocinero listo con ingredientes: {ingredientes}")
        return cls(ingredientes)

    def preparar_receta(self, nombre):
        if nombre not in Cocinero.recetas:
            print(f"❌ Receta {nombre} no existe")
            return

        necesarios = Cocinero.recetas[nombre]
        if necesarios.issubset(self.ingredientes):
            self.productividad += 1
            print(f"✅ {nombre} preparado con éxito. Productividad: {self.productividad}")
        else:
            faltan = necesarios - self.ingredientes
            print(f"⚠️ No se pudo preparar {nombre}. Faltan: {faltan}")

    @staticmethod
    def productividad_total(lista_cocineros):
        total = sum(c.productividad for c in lista_cocineros)
        print(f"📊 Productividad total de la cocina: {total}")
        return total


# Prueba del sistema
c1 = Cocinero.crear_cocinero(["harina", "agua", "sal"])
c2 = Cocinero.crear_cocinero(["harina", "agua", "sal", "tomate", "queso"])
c3 = Cocinero.crear_cocinero(["harina", "agua", "sal", "chocolate"])

c1.preparar_receta("pan")
c2.preparar_receta("pizza")
c3.preparar_receta("galleta")
c3.preparar_receta("pizza")

Cocinero.productividad_total([c1, c2, c3])
