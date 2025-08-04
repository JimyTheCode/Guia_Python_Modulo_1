def Tablas_multiplicacion (numero):
    """
   Esta función permite crear la tabla de multiplicar de 1 a 10 segun el numero que digite el usuario.

   Args:
       numero (int): El numero con que se realiza la tabla de multiplicar.
   Returns:
       """
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese el número de la tabla de multiplicar que quiere realizar: "))
Tablas_multiplicacion(numero)
