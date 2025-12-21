class Tienda:
    """Clase que representa una tienda en línea."""
    def calcular_impuesto(self, monto:float , tasa:float) -> float:
        """Calcula el impuesto basado en el monto y la tasa.

        Args:
            monto (float): El monto sobre el cual se calcula el impuesto.
            tasa (float): La tasa de impuesto.

        Returns:
            float: El monto del impuesto calculado.
        """
        return monto * tasa
    def pagar(self, monto: float, metodo: str) -> None:
        """Procesa el pago utilizando el método especificado.

        Args:
            monto (float):  El monto a pagar.
            metodo (str): El método de pago (tarjeta, transferencia, qr).
        """
        tasas = {
            "tarjeta": 0.05,
            "transferencia": 0.02,
            "qr": 0.01
        }
        tasa = tasas.get(metodo, 0)
        impuesto = self.calcular_impuesto(monto, tasa)
        total = monto + impuesto
        print(f"Pago con {metodo}: Monto={monto}, Impuesto={impuesto}, Total={total}")
tienda = Tienda()
tienda.pagar(100, "tarjeta")
tienda.pagar(100, "transferencia")
tienda.pagar(100, "qr")