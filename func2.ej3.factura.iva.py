#Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
#La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
#y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

total_sin_iva = float (input("Ingrese el total de la factura sin IVA: "))
iva = 21
respuesta = "s"

def calcularIva(total_sin_iva, iva, respuesta):
    while respuesta == "s":
        total_factura = total_sin_iva + (total_sin_iva * iva / 100)
        print("El importe total con IVA es:", total_factura)
        respuesta = input("Desea ingresar otro importe para calcular el total? s / n: ").lower()
        if respuesta == "s":
            total_sin_iva = float(input("Ingrese el total de la factura sin IVA: "))

calcularIva(total_sin_iva, iva, respuesta)