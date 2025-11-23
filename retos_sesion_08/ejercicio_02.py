class Destino:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

    def __str__(self):
        return f"{self.nombre} ➡ {self.costo} USD"


class Catalogo:
    def __init__(self):
        self.destinos = []

    def __str__(self):
        resultado = "🗺 Destinos 🗺\n"
        for i, destino in enumerate(self.destinos, start=1):
            resultado += f"{i}. {destino}\n"
        return resultado.strip()

    def __len__(self):
        return len(self.destinos)

    def __getitem__(self, indice):
        return self.destinos[indice]

    def __setitem__(self, indice, valor):
        self.destinos[indice] = valor

    def __delitem__(self, indice):
        del self.destinos[indice]

    def __iter__(self):
        return iter(self.destinos)


# --- Pruebas ---
if __name__ == "__main__":
    catalogo = Catalogo()

    catalogo.destinos.append(Destino("París", 1200))
    catalogo.destinos.append(Destino("Londres", 1100))
    catalogo.destinos.append(Destino("Roma", 900))
    catalogo.destinos.append(Destino("Tokio", 2000))

    print(catalogo)
    print("Cantidad de destinos:", len(catalogo))

    print("Primer destino:", catalogo[0])

    catalogo[1] = Destino("Berlín", 1050)
    print(catalogo)

    del catalogo[2]
    print("Luego de borrar Roma:")
    print(catalogo)

    print("Iterando destinos:")
    for d in catalogo:
        print("   ", d)
