cantidadNotas = int(input("Ingrese la cantidad de notas: "))

sumaNotas = 0
contador = 0

while contador < cantidadNotas:
    nota = int(input("Ingrese su nota entre 0 y 100: \n"))
    
    sumaNotas+=nota
    contador+=1


if cantidadNotas == 0:
    print("No hubo notas para calcular:(")

elif cantidadNotas > 0:
    promedioNotas = sumaNotas/cantidadNotas
    print("Su promedio es: ", promedioNotas)

else:
    print("Error. Colocó cantidad de notas negativas")



