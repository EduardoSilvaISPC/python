#Realice un programa que lea 4 números y diga cuántos son pares y
#cuantos impares y devuelva la sumatoria de los pares.

pares = 0
suma_pares = 0

for i in range(4):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
        suma_pares += num

impares = 4 - pares

print("Hay", pares, "números pares y", impares, "números impares.")
print("La suma de los números pares es:", suma_pares)