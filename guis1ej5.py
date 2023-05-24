#Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
#el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
#de cambio quiere, si de dólares a pesos o viceversa.

# Solicitar al usuario que ingrese la cantidad a convertir y el tipo de cambio

cantidad = float(input("Ingrese la cantidad a convertir: "))
valor_dolar = float(input ("Ingrese el valor del dolar hoy: "))
tipo_cambio = input("¿Quiere convertir de pesos a dólares (1) o de dólares a pesos (2)? ")

# Convertir la cantidad según el tipo de cambio solicitado
if tipo_cambio.lower() == "1":
    conversion = cantidad / valor_dolar
    print("La cantidad de", cantidad, "pesos equivale a", conversion, "dólares")
elif tipo_cambio.lower() == "2":
    conversion = cantidad * valor_dolar
    print("La cantidad de", cantidad, "dólares equivale a", conversion, "pesos")
else:
    print("El tipo de cambio ingresado no es válido")