def calificaciones(lista):
    """
    Calcula el promedio, la calificación más alta y la más baja
    a partir de una lista de calificaciones numéricas.

    Args:
    lista (list): Lista de calificaciones (números enteros o decimales)

    Return:
    tuple: (promedio, mayor calificación, menor calificación)
    """
    suma = 0
    for nota in lista:
        suma += nota
    promedio = suma / len(lista)
    mayor = max(lista)
    menor = min(lista)
    return (promedio, mayor, menor)

notas = [4.5, 5.0, 3.2, 2.4, 4.3]

resultado = calificaciones(notas)

print(f"Promedio: {resultado[0]}")
print(f"Nota más alta: {resultado[1]}")
print(f"Nota más baja: {resultado[2]}")

