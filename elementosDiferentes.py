lista1 = [1,2,3,4,5,6,11] #Lista 1 en cuestión
lista2= [4,5,6,7,8,9,11,13,14] #Lista 2 en cuestión

listaIguales = list() #Creamos lista para almacenar datos iguales
listaDistintos = list() #Creamos lista para almacenar datos distintos

for i in lista1:  #Entramos a lista1 para comenzar a comparar datos
    for j in lista2: #Entramos a lista2 para comenzar a comparar datos
        if i not in lista2: #Si el dato comparado desde lista1 no está en lista2
            if i not in listaDistintos: #Si el dato comparado desde lista1 no está dentro de lista distintos
                listaDistintos.append(i) #Se agrega el valor a lista distintos
        else:
            if i not in listaIguales: #Hacemos este paso para que no se repitan los datos dentro de la lista al estar en un ciclo
                listaIguales.append(i)


for i in lista2: #En este caso hacemos la comparación desde los elementos de la lista2 sobre la lista1
    for j in lista1:
        if i not in lista1:
            if i not in listaDistintos:
                listaDistintos.append(i)

                #Aquí nos saltamos el else del ciclo anterior debido a que ya se almacenaron los datos iguales en ambas listas
        

print("Elementos en ambas listas: ", listaIguales)

print("Elementos diferentes en listas: ", listaDistintos)