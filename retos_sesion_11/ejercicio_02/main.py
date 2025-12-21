from modelos.libro import Libro
from modelos.usuario import Usuario
from logica.biblioteca import Biblioteca

libros = [
    Libro("1984", "George Orwell", "123"),
    Libro("El Quijote", "Cervantes", "456"),
    Libro("La Odisea", "Homero", "789"),
]

biblioteca = Biblioteca(libros)

while True:
    nombre = input("\nNombre del usuario (o 'salir'): ")
    if nombre.lower() == "salir":
        break

    usuario = Usuario(nombre)
    biblioteca.listar_libros()
    opcion = int(input("Seleccione un libro por número: "))
    biblioteca.registrar_prestamo(usuario, libros[opcion - 1])

    biblioteca.mostrar_prestamos()
