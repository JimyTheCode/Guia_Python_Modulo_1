def IMC (peso, altura):
    """
   Esta función toma el peso de la persona y la divide sobre la altura elevada a la 2.

   Args:
       peso (float): El primer valor.
       altura (float): El segundo valor.

   Returns:
       float: El peso sobre la altura ** 2.
       """
    return  peso / (altura ** 2)

peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))

result = IMC(peso, altura)

if result < 18.5 :
    print(f"Su indice de maza corporal es de: {round(result, 2)} Está bajo de peso ")
elif result >= 18.5 and result < 25 :
    print(f"Su indice de maza corporal es de: {round(result, 2)} Su peso es normal ")
elif result >= 29.9 and result > 50 :
    print(f"Su indice de maza corporal es de: {round(result, 2)} Está en sobre peso ")
