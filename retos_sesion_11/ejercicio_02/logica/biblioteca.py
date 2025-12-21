from modelos.usuario import Usuario


class Biblioteca:
    def __init__(self, libros: list) -> None:
        self.libros = libros
        self.usuarios: list[Usuario] = []

    def listar_libros(self) -> None:
        for indice, libro in enumerate(self.libros, start=1):
            print(f"{indice}. {libro.titulo} - {libro.autor}")

    def registrar_prestamo(self, usuario: Usuario, libro) -> None:
        usuario.prestar_libro(libro)
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)

    def mostrar_prestamos(self) -> None:
        for usuario in self.usuarios:
            print(f"Usuario: {usuario.nombre}")
            for libro in usuario.libros_prestados:
                print(f"- {libro.titulo}")
