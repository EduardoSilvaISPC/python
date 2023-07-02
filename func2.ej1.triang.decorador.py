#Realice un programa que contengan funciones de los tres tipos de triángulos. 
#Los mismos deben estar acompañados de los mensajes respecto a la función decoradora. 
#Para mejorarlo pueden agregar los nombres de cada función según los triángulos.

lado = float(input("Ingrese valor para los lados del triangulo (equilatero) : "))
lado1 = float(input("Ingrese valor para el lado del triangulo (escaleno): "))
lado2 = float(input("Ingrese valor para el lado2 del triangulo (escaleno): "))
lado3 = float(input("Ingrese valor para el lado3 del triangulo (escaleno): "))
base = float(input("Ingrese valor para la base del triangulo (isoseles, escaleno): "))

def titulo_decorador(nombre):
    def decorador(func):
        def triangulos(*param1, **param2):
            print(f"Función ejecutada: {nombre}")
            return func(*param1, **param2)
        return triangulos
    return decorador

@titulo_decorador("Triángulo Equilátero")
def triangulo_equilatero(lado):
    return lado * 3

@titulo_decorador("Triángulo Isósceles")
def triangulo_isosceles(base, lado):
    return base + 2 * lado

@titulo_decorador("Triángulo Escaleno")
def triangulo_escaleno(lado1, lado2, lado3):
    return lado1 + lado2 + lado3


print("---------------------")
resultado_equilatero = triangulo_equilatero(lado)
print(f"Resultado del Perimetro Triángulo Equilátero: {resultado_equilatero}")
print("---------------------")
resultado_isosceles = triangulo_isosceles(base, lado)
print(f"Resultado del Perimetro Triángulo Isósceles: {resultado_isosceles}")
print("---------------------")
resultado_escaleno = triangulo_escaleno(lado1, lado2, lado3)
print(f"Resultado del Perimetro Triángulo Escaleno: {resultado_escaleno}")
print("---------------------")