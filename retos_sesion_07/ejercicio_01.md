# Análisis – Ejercicio 01

Requisitos
- El carpintero usa diferentes herramientas para trabajar.
- Cada herramienta debe tener su propio método usar().
- El carpintero no necesita saber qué tipo de herramienta recibe.
- Se deben crear las herramientas:
  - Martillo
  - Destornillador
  - Llave inglesa

Objetos
- Martillo
- Destornillador
- LlaveInglesa

Características
- Martillo: peso, material_mango
- Destornillador: tipo_punta, largo
- LlaveInglesa: tamaño, material

Acciones
- Martillo: usar()
- Destornillador: usar()
- LlaveInglesa: usar()

# Diagrama de clases (Duck Typing)

```mermaid
classDiagram
    class Martillo {
        -peso: float
        -material_mango: String
        +usar()
    }

    class Destornillador {
        -tipo_punta: String
        -largo: float
        +usar()
    }

    class LlaveInglesa {
        -tamaño: float
        -material: String
        +usar()
    }