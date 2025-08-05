agenda: dict[str, str] = {}

def añadir_contacto() -> None:
    """
    Pide al usuario un nombre y un número,
    y lo guarda en la agenda.
    """
    nombre: str = input("Nombre del contacto: ")
    telefono: str = input("Número de teléfono: ")
    agenda[nombre] = telefono

def buscar_contacto() -> None:
    """
    Pide un nombre y muestra el número si está en la agenda.
    """
    nombre: str = input("Nombre del contacto a buscar: ")

    if nombre in agenda:
        print(f"El número de {nombre} es {agenda[nombre]}")
    else:
        print(f"No se encontró el contacto '{nombre}'")

def mostrar_contactos() -> None:
    """
    Muestra todos los contactos en la agenda.
    """
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("\nLista de contactos:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")

while True:
    print("\n--- AGENDA ---")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Salir")

    opcion: str = input("Elige una opción: ")

    if opcion == "1":
        añadir_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        mostrar_contactos()
    elif opcion == "4":
        print("¡Chaoo!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")



