#Realizar un programa de funciones que contengan funciones con bucles 
#y control de flujo fuera de la función decoradora. 
#Al menos se deben tener dos condicionales o bucles.

lado = float(input("Ingrese valor para los lados del triangulo (equilatero, isoseles) : "))
lado1 = float(input("Ingrese valor para el lado del triangulo (escaleno): "))
lado2 = float(input("Ingrese valor para el lado2 del triangulo (escaleno): "))
lado3 = float(input("Ingrese valor para el lado3 del triangulo (escaleno): "))
base = float(input("Ingrese valor para la base del triangulo (isoseles): "))

def titulo_decorador(nombre):
    def decorador(func):
        def triangulos(*param1, **param2):
            print(f"Función ejecutada: {nombre}")
            return func(*param1, **param2)
        return triangulos
    return decorador

@titulo_decorador("Triángulo Equilátero")
def triangulo_equilatero(lado):
    if lado > 0:
        return lado * 3
    else:
        print("El valor del lado es 0 o menos de 0, no se puede construir el perimtro del triangulo")


@titulo_decorador("Triángulo Isósceles")
def triangulo_isosceles(base, lado):
    if base != lado:
        return base + 2 * lado
    else:
        print("La base y los lados del triangulo escaleno no pueden ser iguales.")

@titulo_decorador("Triángulo Escaleno")
def triangulo_escaleno(lado1, lado2, lado3):
    return lado1 + lado2 + lado3


print(" ")
print("---------------------")
resultado_equilatero = triangulo_equilatero(lado)
print(f"Resultado del Perimetro Triángulo Equilátero: {resultado_equilatero}")
print(" ")
print("---------------------")
resultado_isosceles = triangulo_isosceles(base, lado)
print(f"Resultado del Perimetro Triángulo Isósceles: {resultado_isosceles}")
print(" ")
print("---------------------")
resultado_escaleno = triangulo_escaleno(lado1, lado2, lado3)
print(f"Resultado del Perimetro Triángulo Escaleno: {resultado_escaleno}")
print(" ")
print("---------------------")