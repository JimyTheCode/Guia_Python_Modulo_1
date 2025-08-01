def Edad (edad):
    """
   Esta función toma la edad de la persona.

   Args:
       edad (int): El primer valor.

   Returns:
       int: Edad de la persona.
       """
    return  edad

edad = int(input("Ingrese su Edad: "))

result = Edad(edad)

if result <=17 :
    print(f"Su edad es: {result} es un niño y es menor de edad")
elif result >= 18 and result <= 25 :
    print(f"Su edad es: {result} y es un joven y es mayor de edad")
else :
    print(f"Su edad es: {result} y es un adulto y es mayor de edad")
