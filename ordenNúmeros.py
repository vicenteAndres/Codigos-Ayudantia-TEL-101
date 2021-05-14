cantidadDatos = int(input("Ingrese la cantidad de datos: "))

datos = list()


for i in range(0,cantidadDatos):
    dato = int(input("Ingrese su dato: "))
    datos.append(dato)

print(datos)

datosUnicos = list()

for j in datos:
    if j not in datosUnicos:
        datosUnicos.append(j)

print("Lista con valores únicos: ", datosUnicos)

datosUnicos.sort() #Ordenar de menor a mayor

datosUnicos.reverse()

print(datosUnicos)