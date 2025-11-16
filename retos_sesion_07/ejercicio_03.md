# Análisis – Ejercicio 03

Requisitos
- Crear una clase Romano que reciba una cadena con un número romano.
- Debe permitir sumar dos números romanos con el operador +.
- La suma debe devolver un nuevo objeto Romano.
- Convertir romano → entero y entero → romano.

Objeto
- Romano

Características
- valor_romano: String

Acciones
- convertir a entero
- convertir a romano
- sobrecargar operador +
- mostrar

# Diagrama de clases

```mermaid
classDiagram
    class Romano {
        -valor_romano: String
        -_romano_a_entero()
        -_entero_a_romano()
        +__add__(obj)
        +__str__()
    }
