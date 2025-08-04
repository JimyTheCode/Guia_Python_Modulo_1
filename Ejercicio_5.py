def adivina_el_numero():
    """
    Juego de adivinar un número secreto entre 1 y 100.
Returns:
    Retorna la cantidad de intentos realizados.
    """
    numero_secreto = 42
    numero = 0
    intentos = 0

    while numero != numero_secreto:
        numero = int(input("Ingresa tu número: "))
        intentos += 1

        if numero < numero_secreto:
            print(f"{numero} es menor que el número secreto.")
        elif numero > numero_secreto:
            print(f"{numero} es mayor que el número secreto.")
        else:
            print(f"¡Correcto! El número era {numero_secreto}.")

    return intentos

print("Adivina el número secreto entre 1 y 100.")
resultado = adivina_el_numero()
print(f"Lo lograste en {resultado} intentos.")

