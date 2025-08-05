def es_palindromo(palabra_usuario: str):
    """
    Verifica si una palabra o frase es un palíndromo.

    Ignora espacios y mayúsculas/minúsculas.

    Args:
        palabra_usuario (str): La palabra o frase a evaluar.

    Returns:
        bool: True si es palíndromo, False si no.
    """
    palabra_limpia: str = palabra_usuario.replace(" ", "").lower()
    palabra_invertida: str = palabra_limpia[::-1]

    return palabra_limpia == palabra_invertida

palabra: str = input("Escribe una palabra o frase para verificar si es un palíndromo : ")
print(es_palindromo(palabra))


