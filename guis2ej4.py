#Leer 10 números y mostrar solamente los números positivos, y su sumatoria

suma_positivos = 0

for i in range(10):
    numero = float(input("Ingrese un número " + str(i+1)+": "))
    if numero > 0:
        print(numero)
        suma_positivos += numero

print("La sumatoria de los números positivos es:", suma_positivos)