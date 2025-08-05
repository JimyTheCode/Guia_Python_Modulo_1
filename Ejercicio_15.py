"""
Script para generar un reporte de calificaciones de estudiantes.

Este programa almacena un diccionario de estudiantes con sus respectivas calificaciones.
Calcula el promedio de cada estudiante, determina su estado (Aprobado o Reprobado),
y muestra un reporte formateado con esta información.
"""

def calcular_promedio(calificaciones: list[float]) -> float:
    """
    Calcula el promedio de una lista de calificaciones.

    Parámetros:
    - calificaciones: Lista de números (float) representando las calificaciones del estudiante.

    Retorna:
    - float: El promedio de las calificaciones.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def obtener_estado(promedio: float) -> str:
    """
    Determina si el estudiante aprueba o reprueba según su promedio.

    Parámetros:
    - promedio: Promedio de calificaciones del estudiante.

    Retorna:
    - str: "Aprobado" si el promedio es mayor o igual a 3.0, "Reprobado" en caso contrario.
    """
    return "Aprobado" if promedio >= 3.0 else "Reprobado"


def generar_reporte(estudiantes: dict[str, list[float]]) -> None:
    """
    Genera y muestra un reporte con el promedio y estado de cada estudiante.

    Parámetros:
    - estudiantes: Diccionario donde la clave es el nombre del estudiante (str)
      y el valor es una lista de calificaciones (list[float]).
    """
    print("\nReporte de Calificaciones:")
    print("-" * 30)

    for nombre, calificaciones in estudiantes.items():
        promedio = calcular_promedio(calificaciones)
        estado = obtener_estado(promedio)
        print(f"- Estudiante: {nombre}, Promedio: {promedio:.2f}, Estado: {estado}")

    print("-" * 30)


if __name__ == "__main__":
    estudiantes: dict[str, list[float]] = {
        "Ana": [4.5, 4.8, 4.2],
        "Juan": [2.5, 3.0, 2.9],
        "Luis": [3.5, 3.2, 3.8],
        "María": [1.5, 2.0, 2.8],
        "Pedro": [5.0, 4.9, 5.0],
        "Luisa": [2.9, 3.1, 3.0],
        "Carlos": [4.0, 4.0, 4.0]
    }

    generar_reporte(estudiantes)
