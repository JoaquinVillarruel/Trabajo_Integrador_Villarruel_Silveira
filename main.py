#Calcular promedio

numeros = [] #Se crea la lista
#Se solicita la cantidad de numero a ingresar
cantidad = int(input("Indique la cantidad de numeros que quiere ingresar: "))
#Se piden los numero uno por uno
for i in range(cantidad):
    numero = float(input(f"Ingrese un numero: "))
    numeros.append(numero)
#Se calcula y muestra el promedio
print(f"El promedio de los numeros es: {sum(numeros)/cantidad}")