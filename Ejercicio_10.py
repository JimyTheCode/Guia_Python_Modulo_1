def contar_palabras(texto: str) -> dict[str, int]:
    """
    Cuenta la frecuencia de cada palabra en un texto.

    Convierte todo el texto a minúsculas, separa por espacios
    y cuenta cuántas veces aparece cada palabra.

    Args:
        texto (str): El texto que se desea analizar.

    Returns:
        dict[str, int]: Un diccionario con las palabras como claves
                        y sus frecuencias como valores.
    """
    texto = texto.lower()
    palabras: list[str] = texto.split()
    frecuencias: dict[str, int] = {}

    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias

texto_usuario: str = input("Escribe un texto para contar las palabras: ")
resultado: dict[str, int] = contar_palabras(texto_usuario)

print("\nFrecuencia de palabras en el texto:")
for palabra, cantidad in resultado.items():
    print(f"{palabra}: {cantidad}")


