cantidadNotas = int(input("Ingrese la cantidad de notas: "))

listaNotas = list()

for i in range(cantidadNotas):
    nota = float(input("Ingrese su nota: "))
    listaNotas.append(nota) 

    
print(listaNotas)

notasDestacadas = list()
notasNoDestacadas = list()

listaCopia = list(listaNotas)

for j in range(len(listaCopia)):
    if listaCopia[j] > 90:
        notasDestacadas.append(listaCopia[j])
    else:
        listaNotas.remove(listaCopia[j])
        notasNoDestacadas.append(listaCopia[j])


print("Lista inicial: ", listaCopia)

print("Lista final: ", listaNotas)

print("Lista notas destacadas:", notasDestacadas)

print("Lista notas no destacadas: ", notasNoDestacadas)







    


