# Definición
class Mensaje:
    def __init__(self, contenido):
        self.contenido = contenido
    def enviar(self, *args):
        if "audio" in args:
            print(f"📣 {self.contenido}")
        if "texto" in args:
            print(f"💬 {self.contenido}")
        if "video" in args:
            print(f"🎥 {self.contenido}")

mensaje = Mensaje("Hola, ¿cómo estás?")
mensaje.enviar("texto")
mensaje.enviar("audio")
mensaje.enviar("texto", "audio")
mensaje.enviar("video")
mensaje.enviar("audio", "video")
