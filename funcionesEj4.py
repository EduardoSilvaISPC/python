#Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso,
#mostrar un mensaje que muestre TRUE

numero1 = float (input("Ingrese el primer numero a comparar: "))
numero2 = float (input("Ingrese el segundo numero a comparar: "))

def compara(numero1, numero2):
    if numero1 == numero2:
        return True
    else:
        return False

print ("Los numeros son iguales =", compara(numero1, numero2))

