class Tarea:
    """
    Representa una tarea individual.
    """

    def __init__(self, titulo: str, descripcion: str) -> None:
        self.titulo: str = titulo
        self.descripcion: str = descripcion
        self.completada: bool = False

    def marcar_completada(self) -> None:
        """Marca la tarea como completada."""
        self.completada = True

    def __str__(self) -> str:
        estado = "✔ Completada" if self.completada else "⏳ Pendiente"
        return f"{self.titulo} - {estado}"


class GestorDeTareas:
    """
    Gestiona una colección de tareas.
    """

    def __init__(self) -> None:
        self.tareas: list[Tarea] = []

    def agregar_tarea(self, titulo: str, descripcion: str) -> None:
        self.tareas.append(Tarea(titulo, descripcion))

    def eliminar_tarea(self, titulo: str) -> None:
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo != titulo]

    def completar_tarea(self, titulo: str) -> None:
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.marcar_completada()

    def listar_tareas(self) -> None:
        if not self.tareas:
            print("No hay tareas registradas.")
        for tarea in self.tareas:
            print(tarea)


gestor = GestorDeTareas()

while True:
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Completar tarea")
    print("4. Listar tareas")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        titulo = input("Título: ")
        descripcion = input("Descripción: ")
        gestor.agregar_tarea(titulo, descripcion)
    elif opcion == "2":
        titulo = input("Título de la tarea a eliminar: ")
        gestor.eliminar_tarea(titulo)
    elif opcion == "3":
        titulo = input("Título de la tarea a completar: ")
        gestor.completar_tarea(titulo)
    elif opcion == "4":
        gestor.listar_tareas()
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")
