#Realice un programa que lea tres números, muestre cuál es el mayor y
#determine si es par o impar.

numero1 = float(input ("Ingrse la cantidad 1:"))
numero2 = float(input ("Ingrse la cantidad 2:"))
numero3 = float(input ("Ingrse la cantidad 3:"))

#comparar
if numero1 > numero2 and numero1 > numero3:
    if numero1 % 2 == 0:
        print("La cantidad 1 es la mayor y además es par")
    else:
        print("La cantidad 1 es la mayor y además es impar")
elif numero2 > numero1 and numero2 > numero3:
    if numero2 % 2 == 0:
        print("La cantidad 2 es la mayor y además es par")
    else:
        print("La cantidad 2 es la mayor y además es impar")
else:
    if numero3 % 2 == 0:
        print("La cantidad 3 es la mayor y además es par")
    else:
        print("La cantidad 3 es la mayor y además es impar")