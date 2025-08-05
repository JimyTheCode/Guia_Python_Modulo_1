def mostrar_menu() -> None:
    """
    Muestra el menú de opciones disponibles para gestionar la lista de compras.
    """
    print("\nMenú de opciones:")
    print("1. Agregar ítem a la lista")
    print("2. Eliminar ítem de la lista")
    print("3. Ver la lista completa")
    print("4. Salir")


def agregar_item(lista: list[str]) -> None:
    """
    Solicita al usuario un ítem y lo agrega a la lista de compras.

    Args:
        lista (list): Lista actual de compras.
    """
    item: str = input("Ingresa el ítem que deseas agregar: ")
    lista.append(item)
    print(f"'{item}' fue agregado a la lista.")


def eliminar_item(lista: list[str]) -> None:
    """
    Solicita al usuario un ítem y lo elimina de la lista si existe.

    Args:
        lista (list): Lista actual de compras.
    """
    item: str = input("Ingresa el ítem que deseas eliminar: ")
    if item in lista:
        lista.remove(item)
        print(f"'{item}' fue eliminado de la lista.")
    else:
        print(f"'{item}' no está en la lista.")


def ver_lista(lista: list[str]) -> None:
    """
    Muestra todos los ítems de la lista de compras.

    Args:
        lista (list): Lista actual de compras.
    """
    if lista:
        print("\nLista de compras:")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")
    else:
        print("\nLa lista de compras está vacía.")


def gestionar_lista_compras() -> None:
    """
    Ejecuta el programa principal para gestionar la lista de compras
    utilizando un bucle while y un menú interactivo.
    """
    lista_compras: list[str] = []
    opcion: str = ""

    while opcion != "4":
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            agregar_item(lista_compras)
        elif opcion == "2":
            eliminar_item(lista_compras)
        elif opcion == "3":
            ver_lista(lista_compras)
        elif opcion == "4":
            print("¡Gracias por usar el gestor de lista de compras!")
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")


gestionar_lista_compras()
