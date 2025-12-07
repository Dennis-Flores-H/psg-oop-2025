# Clase base Helado
class Helado:
    def __init__(self, sabor, envase):
        self.sabor = sabor
        self.envase = envase
    
    def comer(self):
        print(f"Comiendo {self.sabor} 🍦 en {self.envase}")

# Clases derivadas para los diferentes tipos de helado
class HeladoVainilla(Helado):
    def __init__(self, envase):
        super().__init__("Vainilla", envase)
    
    def comer(self):
        print(f"Comiendo Helado de Vainilla 🍦 en {self.envase}")

class HeladoChocolate(Helado):
    def __init__(self, envase):
        super().__init__("Chocolate", envase)
    
    def comer(self):
        print(f"Comiendo Helado de Chocolate 🍦 en {self.envase}")

# Clase base Maquina
class Maquina:
    def preparar(self, envase):
        pass

# MaquinaVainilla hereda de Maquina
class MaquinaVainilla(Maquina):
    def preparar(self, envase):
        return HeladoVainilla(envase)

# MaquinaChocolate hereda de Maquina
class MaquinaChocolate(Maquina):
    def preparar(self, envase):
        return HeladoChocolate(envase)

# Clase Encargado
class Encargado:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def tomar_pedido(self, sabor, envase):
        if sabor == "vainilla":
            maquina = MaquinaVainilla()
            helado = maquina.preparar(envase)
        elif sabor == "chocolate":
            maquina = MaquinaChocolate()
            helado = maquina.preparar(envase)
        else:
            raise ValueError("❌ Helado no disponible. Intente de nuevo.")
        
        return helado

# Lógica del pedido del cliente
def pedir_helado():
    encargado = Encargado("Juan")
    while True:
        # Menú interactivo para el cliente
        print("🍨 Pedidos de Helado 🍨")
        print("1. Vainilla en Cono")
        print("2. Vainilla en Vaso")
        print("3. Chocolate en Cono")
        print("4. Chocolate en Vaso")
        print('Escribe "salir" para terminar.')

        # El cliente ingresa su pedido
        tipo_helado = input("Elige un número para tu pedido: ").lower().strip()
        
        if tipo_helado == "salir":
            print("🚶‍♂️ Saliendo de la heladería.")
            break
        
        # Determinamos el sabor y el envase según la opción del cliente
        if tipo_helado == "1":
            sabor = "vainilla"
            envase = "cono"
        elif tipo_helado == "2":
            sabor = "vainilla"
            envase = "vaso"
        elif tipo_helado == "3":
            sabor = "chocolate"
            envase = "cono"
        elif tipo_helado == "4":
            sabor = "chocolate"
            envase = "vaso"
        else:
            print("❌ Opción no válida. Por favor, elige un número del menú.")
            continue
        
        try:
            helado = encargado.tomar_pedido(sabor, envase)
            helado.comer()
        except ValueError as e:
            print(e)

# Iniciar el proceso de pedido
pedir_helado()
