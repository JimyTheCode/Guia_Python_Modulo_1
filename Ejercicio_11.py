def comparar_listas(lista1, lista2):
    """
    Recibe dos listas de enteros y devuelve una tupla con tres conjuntos:
    - Elementos en ambas listas.
    - Elementos solo en la primera lista.
    - Elementos solo en la segunda lista.

    Args:
        lista1 (list): Primera lista.
        lista2 (list): Segunda lista.

    Returns:
        tuple: (en_ambas, solo_en_lista1, solo_en_lista2)
    """

    set1: set[int] = set(lista1)
    set2: set[int] = set(lista2)

    en_ambas: set[int] = set1 & set2
    solo_en_lista1: set[int] = set1 - set2
    solo_en_lista2: set[int] = set2 - set1

    return en_ambas, solo_en_lista1, solo_en_lista2

lista_a: list[int] = [1, 2, 3, 4, 5]
lista_b: list[int] = [4, 5, 6, 7]

resultado = comparar_listas(lista_a, lista_b)

print("Elementos en ambas listas:", resultado[0])
print("Solo en la primera lista:", resultado[1])
print("Solo en la segunda lista:", resultado[2])
