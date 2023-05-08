#Realice un programa donde el usuario ingrese su edad. Si es mayor de
#16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.

#Ingrese la edad

edad = int(input("Ingrese su edad real: "))

if edad > 16:
    print("Ud puede votar")
else:
    print("Ud no vota, todavia")