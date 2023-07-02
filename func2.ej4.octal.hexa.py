#Escribir una función que convierta un número decimal en los otros dos sistemas: 
#Binario y Hexadecimal. Mostrar mensajes pertenecientes a cada función.

numero = int(input("Ingrese el numero entero a convertir y vea la magia:"))
resultadoo = 0
resultadoh = 0
res = " "

def opcion1(numero, resultadoo):
    resultadoo = oct(numero)
    print ("El resultado de la conversion al sistema octal es: ", resultadoo)

def opcion2(numero, resultadoh):
    resultadoh = hex(numero)
    print ("El resultado de la conversion al sistema hexagecimal es: ", resultadoh)

def opcion_novalida():
    print("Opción inválida. Por favor, selecciona una opción válida.")

while True:
    print ("-----------")
    print("Elija a que sistema desea convertir su cantidad:")
    print ("   ")
    print("1. - OCTAL -")
    print ("   ")
    print("2. - HEXAGECIMAL - ")
    print ("   ")
    print("3. - Ingresa un nueva cantidad a convertir: - ")
    print ("   ")
    print("4. - SALIR - ")
    print ("   ")
    print ("-----------")

    opcion = input("Selecciono la opción: ")
    print ("   ")

    if opcion == "1":
        opcion1(numero, resultadoo)
    elif opcion == "2":
        opcion2(numero, resultadoh)
    elif opcion == "3":
        numero = int(input("Ingrese el numero entero a convertir y vea la magia:"))
    elif opcion == "4":
        print("¡Hasta luego!, Gracias por participar")
        print ("-----------")
        print ("   ")
        break
    else:
        opcion_novalida()