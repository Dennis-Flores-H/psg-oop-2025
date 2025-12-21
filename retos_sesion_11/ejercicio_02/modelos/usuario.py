class Usuario:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.libros_prestados: list = []

    def prestar_libro(self, libro) -> None:
        self.libros_prestados.append(libro)

    def devolver_libros(self) -> None:
        self.libros_prestados.clear()
