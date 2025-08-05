factores_conversion: dict[str, float] = {
    "metros": 1.0,
    "centimetros": 100.0,
    "milimetros": 1000.0,
    "kilometros": 0.001,
}


def sugerir_unidades() -> None:
    """
    Muestra las unidades disponibles al usuario.
    """
    print("\nUnidades disponibles:")
    for unidad in factores_conversion:
        print(f" - {unidad}")


def buscar_unidad(nombre: str) -> str | None:
    """
    Intenta encontrar una unidad válida con coincidencia parcial.

    Args:
        nombre (str): Texto ingresado por el usuario.

    Returns:
        str | None: Nombre completo de la unidad si se encuentra.
    """
    nombre = nombre.lower()
    for unidad in factores_conversion:
        if nombre in unidad:
            return unidad
    return None


def formatear_numero(numero: float) -> str:
    """
    Devuelve un número como string, sin decimales innecesarios.

    Args:
        numero (float): Número a formatear.

    Returns:
        str: Número formateado como texto.
    """
    if numero == int(numero):
        return str(int(numero))
    else:
        return f"{numero:.2f}"


def convertir_unidades(
    cantidad: float,
    origen: str,
    destino: str
) -> float | None:
    """
    Convierte una cantidad de una unidad a otra, usando factores base en metros.

    Args:
        cantidad (float): Valor numérico.
        origen (str): Unidad de origen.
        destino (str): Unidad de destino.

    Returns:
        float | None: Valor convertido, o None si alguna unidad es inválida.
    """
    origen_valido = buscar_unidad(origen)
    destino_valido = buscar_unidad(destino)

    if origen_valido is None:
        print(f"\n Unidad de origen no reconocida: '{origen}'")
        sugerir_unidades()
        return None

    if destino_valido is None:
        print(f"\n Unidad de destino no reconocida: '{destino}'")
        sugerir_unidades()
        return None

    en_metros = cantidad / factores_conversion[origen_valido]
    resultado = en_metros * factores_conversion[destino_valido]
    return resultado

print("Convertidor de unidades de longitud")
sugerir_unidades()

try:
    cantidad_usuario: float = float(input("\nCantidad a convertir: "))
    unidad_origen: str = input("Unidad de origen: ")
    unidad_destino: str = input("Unidad de destino: ")

    resultado = convertir_unidades(
        cantidad_usuario, unidad_origen, unidad_destino
    )

    if resultado is not None:
        origen_real = buscar_unidad(unidad_origen)
        destino_real = buscar_unidad(unidad_destino)
        print(
            f"\nResultado: {formatear_numero(cantidad_usuario)} {origen_real} = {formatear_numero(resultado)} {destino_real}"
        )

except ValueError:
    print("Error: la cantidad debe ser un número.")


