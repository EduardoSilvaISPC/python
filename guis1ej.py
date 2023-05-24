#Realizar un programa que permita ingresar “f” o “m” y determinar si vota
#en mesa femenina o masculina.

# Solicitar al usuario que ingrese su género

genero = input("Ingrese su género (f/m): ")

# Determinar la mesa de votación según el género
if genero.lower() == "f":
    print("Usted vota en la mesa femenina")
elif genero.lower() == "m":
    print("Usted vota en la mesa masculina")
else:
    print("El género ingresado no es válido")