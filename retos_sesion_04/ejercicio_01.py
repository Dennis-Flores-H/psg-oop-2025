class Cuenta:
    def __init__(self, numero_cuenta, titular, saldo=0.0):
        self.__numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = saldo

    # Propiedad para número de cuenta (solo lectura)
    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    # Propiedad para saldo (solo lectura)
    @property
    def saldo(self):
        return self.__saldo

    # Método de depósito
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"💰 Depósito de {monto} realizado. Saldo actual: {self.__saldo}")
        else:
            print("❌ Monto inválido para depósito")

    # Método de retiro
    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"🏧 Retiro de {monto} realizado. Saldo actual: {self.__saldo}")
        else:
            print("❌ Fondos insuficientes o monto inválido")


# Prueba de la clase
cuenta1 = Cuenta("001-2025-0001", "Erick", 1000)
print(f"TITULAR: {cuenta1.titular}")
print(f"NÚMERO DE CUENTA: {cuenta1.numero_cuenta}")
print(f"SALDO INICIAL: {cuenta1.saldo}")

cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.titular = "Carlos"
print(f"NUEVO TITULAR: {cuenta1.titular}")
