def Frase_usario (Frase):
    """
   Esta función toma la una frase que digitará el usuario, borra los espacios para no tenerlos en cuenta, no permite ingresar simbolos.
   Y cuenta cuantas consonates y vocales contiene la frase digitada por el usuario.

   Args:
       Frase (str): frase que ingresa el usuario.

   Returns:
       dict: numero de vocales y de consonantes de la frase.
       """

    vocales = ["a", "e", "i", "o", "u"]
    contadorV = 0
    contadorC = 0
    Frase_Nueva = Frase.replace(" ", "").lower()

    for i in Frase_Nueva:
        if ord(i) >= 97 and ord(i) <= 122 :
            if i in vocales:
                contadorV += 1
            else:
                contadorC += 1
        else:
            print(f"{i} no es un caracter valido")

    return { "vocales" : contadorV, "consonantes" : contadorC }

Frase = input("Ingrese su frase: ")
resultado = Frase_usario(Frase)

print(f"El total de vocales es: {resultado['vocales']}")
print(f"El total de consonantes:  {resultado['consonantes']}")
