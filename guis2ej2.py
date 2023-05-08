#Leer 10 números y obtener la cantidad de mayores y la cantidad de
#menores a 100, cuál es el número máximo y cuál es el número mínimo.

mayores = 0
menores = 0
maximo = None
minimo = None

for i in range(10):
    num = int(input("Ingrese un número: "))
    if num > 100:
        mayores += 1
    else:
        menores += 1
        
    if maximo is None or num > maximo:
        maximo = num
        
    if minimo is None or num < minimo:
        minimo = num
        
print("Cantidad de números mayores a 100:", mayores)
print("Cantidad de números menores a 100:", menores)
print("Número máximo:", maximo)
print("Número mínimo:", minimo)