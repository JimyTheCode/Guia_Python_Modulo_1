def Edad_usuario (Edad):
    """
   Esta función toma la edad del usuario y define si es mayor de edad, joven adulto o mayor de edad.

   Args:
       Edad (int): valor numérico insertado por el usuario.

   Returns:
       str: Respuesta = Es la validación de la edad
       """

    Respuesta = ""

    if Edad < 18:
        Respuesta = (f"Su edad es: {Edad} Es menor de edad")
    elif Edad >= 18 and Edad <= 25:
        Respuesta = (f"Su edad es: {Edad} Es un joven adulto")
    else:
        Respuesta = (f"Su edad es: {Edad} Es mayor de edad")

    return  Respuesta

Edad = int(input("Ingrese su edad: "))
print(Edad_usuario(Edad))
