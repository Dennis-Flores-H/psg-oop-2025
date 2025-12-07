# Análisis

## Requisitos
- Se preparan helados de dos sabores: vainilla o chocolate.
- Los helados se pueden servir en dos tipos de envase: cono o vaso.
- La máquina de vainilla solo prepara helados de vainilla.
- La máquina de chocolate solo prepara helados de chocolate.
- Cada maquina produce un tipo de helado.
- Un cliente puede pedir el helado que desea.
- Cada pedido debe incluir el sabor y el envase del helado.
- El cliente puede hacer múltiples pedidos de helado hasta que decida escribir "salir".
- Los helados deben ser representados en el formato: "[sabor] 🍦 en [envase]".
- Todos los helados se pueden comer.

## Objetos
- Helado (Vainilla, Chocolate)
- Maquina (MaquinaVainilla, MaquinaChocolate)
- Encargado

## Características

### Helado:
    - sabor
    - envase

-  Vainilla:
    - sabor: vainilla
    - envase: cono/vaso

- Chocolate:
    - sabor: chocolate
    - envase: cono/vaso

### Maquina:
    - tipo_helado

- MaquinaVainilla:
    - tipo_helado: vainilla

- MaquinaChocolate:
    - tipo_helado: chocolate

### Encargado:
    - nombre

## Acciones

### Helado:
- comer() → el cliente come el helado.

### Maquina:
- preparar() → prepara el helado solicitado.

### MaquinaVainilla:
- preparar() → prepara helado de vainilla.

### MaquinaChocolate:
- preparar() → prepara helado de chocolate.

### Encargado:
- tomar_pedido() → recibe el pedido del cliente y crea el helado correspondiente.

---

# Diseño

## Clases:

- **Helado:**
    - **Nombre:** Helado
    - **Atributos:**
        - sabor
        - envase
    - **Métodos:**
        - comer()

- **HeladoVainilla:**
    - **Nombre:** HeladoVainilla
    - **Atributos:**
        - sabor: vainilla
        - envase: cono/vaso
    - **Métodos:**
        - comer()

- **HeladoChocolate:**
    - **Nombre:** HeladoChocolate
    - **Atributos:**
        - sabor: chocolate
        - envase: cono/vaso
    - **Métodos:**
        - comer()

- **Maquina:**
    - **Nombre:** Maquina
    - **Atributos:**
        - tipo_helado
    - **Métodos:**
        - preparar()

- **MaquinaVainilla:**
    - **Nombre:** MaquinaVainilla
    - **Atributos:**
        - tipo_helado: vainilla
    - **Métodos:**
        - preparar()

- **MaquinaChocolate:**
    - **Nombre:** MaquinaChocolate
    - **Atributos:**
        - tipo_helado: chocolate
    - **Métodos:**
        - preparar()

- **Encargado:**
    - **Nombre:** Encargado
    - **Atributos:**
        - nombre
    - **Métodos:**
        - tomar_pedido()

---

# Diagrama de clases

```mermaid
classDiagram
    class Helado {
        -sabor
        -envase
        +comer()
    }
    class HeladoVainilla {
        -sabor: vainilla
        -envase: cono/vaso
        +comer()
    }
    class HeladoChocolate {
        -sabor: chocolate
        -envase: cono/vaso
        +comer()
    }
    class Maquina {
        -tipo_helado
        +preparar()
    }
    class MaquinaVainilla {
        -tipo_helado: vainilla
        +preparar()
    }
    class MaquinaChocolate {
        -tipo_helado: chocolate
        +preparar()
    }
    class Encargado {
        -nombre
        +tomar_pedido()
    }
    Helado <|-- HeladoVainilla
    Helado <|-- HeladoChocolate
    Maquina <|-- MaquinaVainilla
    Maquina <|-- MaquinaChocolate
    Maquina --> Helado
    Encargado --> Maquina
```