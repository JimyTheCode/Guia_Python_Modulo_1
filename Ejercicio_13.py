"""
Sistema de gestión de inventario para una tienda.

Este programa permite al usuario agregar productos, realizar ventas y mostrar
el inventario actual. El inventario se representa como una lista de diccionarios,
donde cada diccionario contiene:
- nombre: str
- precio: float
- cantidad: int
"""

inventario: list[dict[str, str | float | int]] = []


def formatear_numero(numero: float) -> str:
    """
    Formatea un número float con separadores de miles usando guiones bajos.

    Args:
        numero (float): El número a formatear.

    Returns:
        str: Número formateado como string, por ejemplo 10_000.00
    """
    parte_entera, parte_decimal = f"{numero:.2f}".split(".")
    parte_entera_con_sep = f"{int(parte_entera):_}"
    return f"{parte_entera_con_sep}.{parte_decimal}"


def agregar_producto() -> None:
    """
    Agrega un nuevo producto al inventario.
    Si el producto ya existe, actualiza su cantidad.
    """
    nombre: str = input("Nombre del producto: ").strip().lower()
    precio: float = float(input("Precio del producto: "))
    cantidad: int = int(input("Cantidad en stock: "))

    for producto in inventario:
        if producto["nombre"] == nombre:
            producto["cantidad"] += cantidad
            print(f"Producto '{nombre}' actualizado. Nueva cantidad: {producto['cantidad']}")
            return

    nuevo_producto: dict[str, str | float | int] = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(nuevo_producto)
    print(f"Producto '{nombre}' agregado con precio ${formatear_numero(precio)} y cantidad {cantidad}.")


def realizar_venta() -> None:
    """
    Realiza la venta de un producto si hay suficiente stock.
    """
    nombre: str = input("Nombre del producto vendido: ").strip().lower()
    cantidad_vendida: int = int(input("Cantidad vendida: "))

    for producto in inventario:
        if producto["nombre"] == nombre:
            if producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] -= cantidad_vendida
                total: float = producto["precio"] * cantidad_vendida
                print(f"Venta realizada: {cantidad_vendida} unidad(es) de '{nombre}'. "
                      f"Total: ${formatear_numero(total)}")
                print(f"Stock restante de '{nombre}': {producto['cantidad']}")
            else:
                print(f"No hay suficiente stock. Solo quedan {producto['cantidad']} unidad(es) de '{nombre}'.")
            return

    print(f"Producto '{nombre}' no encontrado en el inventario.")


def mostrar_inventario() -> None:
    """
    Muestra el listado completo del inventario.
    """
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n--- Inventario Actual ---")
    for producto in inventario:
        print(
            f"Nombre: {producto['nombre'].capitalize()} | "
            f"Precio: ${formatear_numero(producto['precio'])} | "
            f"Cantidad: {producto['cantidad']}"
        )


def mostrar_menu() -> None:
    """
    Muestra el menú principal y ejecuta la opción seleccionada por el usuario.
    """
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion: str = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            realizar_venta()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            print("Gracias por usar el sistema de inventario.")
            break
        else:
            print(f"Opción inválida: '{opcion}'. Intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu()

