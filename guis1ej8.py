#Realice un programa que le permita al usuario simular el pago
#ingresando el importe y la forma de pago:

#Contado (1): se aplica un descuento del 10% al importe

#Tarjeta (2): se aplica un interés de 10%

#Débito (3): se aplica un descuento del 5%
#Mostrar el importe, el descuento o interés y el importe total.

pago1=float(input("Ingrese la cantidad a abonar: "))
forma_pago = (input("Ingrese la forma de pago: \n(C) Contado \n(T) Tarjeta de credito \n(D) Debito \n"))

#Evaluar forma de pago
if forma_pago == "C" or forma_pago == "c":
    total = float(pago1 * 0.90)
    interes = float(pago1 - total)
    print ("Ud sebe abonar en total: "+ str(total) +", su descuento es de: $ " +str(interes))
elif forma_pago =="T" or forma_pago == "t":
    total1 = float(pago1 * 1.10)
    interes1=float(total1 - pago1)
    print ("Ud sebe abonar en total: "+ str(total1) +", su recargo es de: $ "+ str(interes1))
elif forma_pago=="D" or forma_pago == "d":
    total2= float(pago1*0.95)
    interes2=float(pago1-total2)
    print ("Ud sebe abonar en total: " +str(total2) +", su descuento es de: $ " +str(interes2))
else:
     print ("La opcion seleccionada no se encuentra disponible. Bye, Bye")   
