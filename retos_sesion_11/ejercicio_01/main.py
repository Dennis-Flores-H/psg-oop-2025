from models.lista_tareas import ListaTareas

lista = ListaTareas()

while True:
    print("\n--- Menú ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Eliminar tareas completadas")
    print("6. Eliminar todas las tareas")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        descripcion = input("Descripción de la tarea: ")
        lista.agregar_tarea(descripcion)
    elif opcion == "2":
        lista.mostrar_tareas()
    elif opcion == "3":
        lista.mostrar_tareas()
        indice = int(input("Índice de la tarea: "))
        lista.completar_tarea(indice)
    elif opcion == "4":
        lista.mostrar_tareas()
        indice = int(input("Índice de la tarea: "))
        lista.eliminar_tarea(indice)
    elif opcion == "5":
        lista.eliminar_completadas()
    elif opcion == "6":
        lista.eliminar_todas()
    elif opcion == "7":
        break
    else:
        print("Opción inválida.")
