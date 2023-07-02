#Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos
#variables locales nombradas suma y resta, respectivamente. Recuerda: en estos ejercicios trabajamos
#argumentos para este ejercicio sería dos.

numero1 = float (input("Ingrese el primer numero: "))
numero2 = float (input("Ingrese el segundo numero: "))


def sumayresta(suma,resta):
    print(f"El resultado de la suma es: {suma} ,\nel resultado de la resta es: {resta}")


suma =  float (numero1 + numero2)
resta = float (numero1 - numero2)

sumayresta(suma,resta)
