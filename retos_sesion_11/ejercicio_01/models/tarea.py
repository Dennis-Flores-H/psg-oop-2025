class Tarea:
    def __init__(self, descripcion: str) -> None:
        self.descripcion: str = descripcion
        self.completada: bool = False

    def marcar_completada(self) -> None:
        self.completada = True
