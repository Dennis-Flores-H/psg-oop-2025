# Análisis – Ejercicio 02

Requisitos
- Todos los instrumentos deben poder ejecutar la acción tocar().
- Cada instrumento produce un sonido distinto.
- Se deben crear:
  - Instrumento (base)
  - Guitarra
  - Piano
  - Tambor

Objetos
- Instrumento
- Guitarra
- Piano
- Tambor

Características
- Instrumento: material
- Guitarra: num_cuerdas
- Piano: num_teclas
- Tambor: tipo_percusión

Acciones
- Instrumento: tocar() (definición general)
- Guitarra: tocar() → "strum"
- Piano: tocar() → "plin"
- Tambor: tocar() → "boom"

# Diagrama de clases

```mermaid
classDiagram
    class Instrumento {
        -material: String
        +tocar()
    }

    class Guitarra {
        -num_cuerdas: int
        +tocar()
    }

    class Piano {
        -num_teclas: int
        +tocar()
    }

    class Tambor {
        -tipo_percusion: String
        +tocar()
    }

    Instrumento <|-- Guitarra
    Instrumento <|-- Piano
    Instrumento <|-- Tambor
