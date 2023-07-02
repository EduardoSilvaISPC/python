#Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. Mostrar
#el resultado dos veces

a = int (input("Ingrese el primer valor a sumar: "))
b = int (input("Ingrese el segundo valor a sumar: "))

c = int (input("Ingrese el primer valor a restar: "))
d = int (input("Ingrese el segundo valor a restar: "))


def sumandos(a,b):
    return a+b


def restandos(c,d):
    return c-d

print ("------------------------")

print ("El resultado de la suma es: " ,sumandos(a,b))


print ("------------------------")

print ("El resultado de la resta es: " , restandos(c,d))

print ("------------------------")