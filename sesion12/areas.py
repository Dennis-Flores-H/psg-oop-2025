class Calculadora:
    """Calculadora de areas de cuadrados y rectángulos."""
    def area(self, lado1, lado2):
        """Calcula el área de un rectángulo o cuadrado.

        Args:
            lado1 (int): El primer lado.
            lado2 (int): El segundo lado.
        
        Returns:
            int: El área calculada de la figura.
        """
        return lado1 * lado2
calculadora = Calculadora()
print(calculadora.area(5, 10))  # Área del rectángulo
print(calculadora.area(5, 5))   # Área del cuadrado