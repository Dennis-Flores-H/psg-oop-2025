Imagina un sistema que modela el trabajo de cocineros en una cocina profesional.
Cada cocinero tiene tres elementos clave:
- Una lista de ingredientes disponibles.
- Un conjunto de recetas definidas que puede preparar
- Un contador de productividad, que aumenta cada vez que prepara una receta con éxito. Si hay más de un cocinero, sus puntos individuales pueden sumarse para obtener una métrica agregada de productividad.

Las únicas recetas permitidas en el sistema son:

Receta	    Ingredientes Requeridos
---------------------------------------
pan	    |   harina, agua
pizza	|   harina, agua, sal, tomate, queso
galleta	|   harina, agua, sal, chocolate

- Realiza el análisis y diagrama de clases de la clase Cocinero en el archivo ejercicio_02.md.
- Escribe el codigo en Python para la clase Cocinero en el archivo ejercicio_02.py.
- Implementa los métodos de instancia, clase y estáticos según corresponda.
- Instancia tres Cocineros y prueba sus métodos.
- Muestra la métrica agregada de productividad.

Análisis

Requisitos:
- Cada cocinero tiene:
    - Una lista de ingredientes disponibles.
    - Un conjunto de recetas posibles.
    - Un contador de productividad (aumenta si prepara una receta con éxito).
- Si hay varios cocineros, se puede sumar su productividad total.
- Solo existen tres recetas válidas:
    - pan → harina, agua
    - pizza → harina, agua, sal, tomate, queso
    - galleta → harina, agua, sal, chocolate

Objetos:
- Cocinero

Características:
- Cocinero: ingredientes, productividad

Acciones:
- Preparar receta
- Mostrar productividad
- Calcular productividad total (estático)

Tipo de métodos:
- Método de instancia: preparar_receta()
- Método de clase: crear_cocinero()
- Método estático: productividad_total(lista_cocineros)


```mermaid
classDiagram
    class Cocinero {
        list ingredientes
        int productividad
        dict recetas
        preparar_receta(nombre)
        crear_cocinero(ingredientes)
        productividad_total(cocineros)
    }
```