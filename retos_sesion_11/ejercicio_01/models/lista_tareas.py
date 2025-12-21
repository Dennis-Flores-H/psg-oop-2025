from models.tarea import Tarea


class ListaTareas:
    def __init__(self) -> None:
        self.tareas: list[Tarea] = []

    def agregar_tarea(self, descripcion: str) -> None:
        self.tareas.append(Tarea(descripcion))

    def mostrar_tareas(self) -> None:
        if not self.tareas:
            print("No hay tareas pendientes.")
            return

        for indice, tarea in enumerate(self.tareas, start=1):
            estado = "✔️" if tarea.completada else " "
            print(f"{indice}. [{estado}] {tarea.descripcion}")

    def completar_tarea(self, indice: int) -> None:
        if 0 < indice <= len(self.tareas):
            self.tareas[indice - 1].marcar_completada()
        else:
            print("Índice inválido.")

    def eliminar_tarea(self, indice: int) -> None:
        if 0 < indice <= len(self.tareas):
            self.tareas.pop(indice - 1)
        else:
            print("Índice inválido.")

    def eliminar_completadas(self) -> None:
        self.tareas = [t for t in self.tareas if not t.completada]

    def eliminar_todas(self) -> None:
        self.tareas.clear()
