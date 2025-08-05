"""
Simulador de Cajero Automático

Este programa permite consultar saldo, depositar dinero y retirar dinero
de una cuenta simulada. El saldo se almacena en una variable global.
"""

saldo: float = 1000.00


def formatear_numero(numero: float) -> str:
    """
    Formatea un número float usando guion bajo como separador de miles.

    Args:
        numero: Número a formatear

    Returns:
        Cadena con el número formateado, por ejemplo: 1_000.00
    """
    parte_entera, parte_decimal = f"{numero:.2f}".split(".")
    parte_entera_con_sep = f"{int(parte_entera):_}"
    return f"{parte_entera_con_sep}.{parte_decimal}"


def consultar_saldo() -> None:
    """
    Muestra el saldo actual de la cuenta.
    """
    print(f"\nSaldo actual: ${formatear_numero(saldo)}")


def depositar() -> None:
    """
    Permite al usuario depositar dinero en la cuenta.
    Valida que el monto sea positivo.
    """
    global saldo
    try:
        monto: float = float(input("Ingrese el monto a depositar: "))
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
            return
        saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${formatear_numero(saldo)}")
    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")


def retirar() -> None:
    """
    Permite al usuario retirar dinero de la cuenta.
    Valida que el monto no exceda el saldo disponible.
    """
    global saldo
    try:
        monto: float = float(input("Ingrese el monto a retirar: "))
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
            return
        if monto > saldo:
            print("Fondos insuficientes.")
            return
        saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: ${formatear_numero(saldo)}")
    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")


def mostrar_menu() -> None:
    """
    Muestra el menú de operaciones y ejecuta la opción seleccionada
    hasta que el usuario decida salir.
    """
    while True:
        print("\n--- Cajero Automático ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion: str = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            print("Gracias por usar el cajero automático. Hasta luego.")
            break
        else:
            print(f"Opción inválida: '{opcion}'. Intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()

