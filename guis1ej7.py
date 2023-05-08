#Introducir los lados de un triángulo y visualizar por pantalla si dicho
#triángulo es equilátero, isósceles o escaleno.

#introducir lados
lado1 = float(input("Introduzca la medida del lado 1 en cm: "))
lado2 = float(input("Introduzca la medida del lado 2 en cm: "))
lado3 = float(input("Introduzca la medida del lado 3 en cm: "))

#Equilatero isoceles o escaleno
if lado1==lado2==lado3:
    print("El triangulo es equilatero")
elif lado1==lado2:S
    print("El triangulo es isoceles")
else:
    print("El triangulo es escaleno")