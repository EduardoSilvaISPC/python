#Confeccione un programa que pida un número del 1 al 7 y diga el día de
#la semana correspondiente.

numero_dia = int(input("Ingrese un numero entre 1 y 7: "))

#camparar
if numero_dia == 1:
    print("Lunes")
elif numero_dia == 2:
    print("Martes")
elif numero_dia == 3:
    print("Miércoles")
elif numero_dia == 4:
    print("Jueves")
elif numero_dia == 5:
    print("Viernes")
elif numero_dia == 6:
    print("Sábado")
elif numero_dia == 7:
    print("Domingo")
else:
    print("Número no válido. Ingrese un número del 1 al 7.")
