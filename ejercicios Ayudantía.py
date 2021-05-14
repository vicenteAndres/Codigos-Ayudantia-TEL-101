sala1 = [
["X","X","X","O","O"],
["X","X","X","X","O"],
["X","O","X","O","X"],
["X","X","X","X","O"],
["O","O","X","O","O"],
]
sala2 = [
["X","X","X"],
["X","X","X"],
["X","X","X"],
["X","X","X"],
]

def asientos_disponibles(sala): #Creamos la función asientos_disponibles con el parámetro sala
    for fila in sala: #Comenzamos a recorrer la lista sala por cada fila que viene siendo una lista
        for asiento in fila: #Aquí recorremos cada posición dentro de las listas fila
            if asiento == "O": #Si la posición dentro de la fila es igual a O
                return True #Nos retorna el True
        return False #En caso contrario, retorna el False

print("Sala 1:", asientos_disponibles(sala1))
print("Sala 2:", asientos_disponibles(sala2))


def disponible(fila,columna,sala): #Definimos la función con parámetros fila,columna,sala
    if fila >= 0 and fila <len(sala): #Aquí decimos: Si fila(número dentro del parámetro) es mayor a 0 y menor a el largo de sala(viene siendo el número de listas dentro de sala)
        if columna >= 0 and columna < len(sala)[fila]: #Si columna es mayor a 0 y menor al largo de los elementos dentro de la fila de sala
            if sala[fila][columna]== "O": #Si el valor de la posición sala[fila][columna] es igual a O
                return True #Retorna True
            else: #En caso contrario, retorna False
                return False
    return False #Este otro False viene haciendo referencia al momento cuando no se cumple el primer if, es decir, que fila esté dentro del rango inicial

print(disponible(0,3,sala1))
print(disponible(0,2,sala1))
print(disponible(4,4,sala1))


def porcentaje_disponible(sala): #Definimos la función porcentaje_disponibles con el parámetro sala
    cantidadAsientos = 0 #Creamos una variable para cuantificar la cantidad de asientos dentro de la sala
    cantidadDisponibles = 0 #Creamos otra variable para cuantificar la cantidad de asientos disponibles
    for fila in sala: #Comenzamos a recorrer la lista sala por cada fila que viene siendo una lista
        for asiento in fila: #Aquí recorremos cada posición dentro de las listas fila
            if asiento == "O": #Si la posición dentro de la fila es igual a O
                cantidadDisponibles+=1 #Sumamos uno a cantidad de asientos disponibles
            cantidadAsientos+=1 #Cada vez que ocurre el ciclo "for asiento in fila", incrementamos el valor de cantidad de asientos en 1
    return (cantidadDisponibles/cantidadAsientos)*100 #Retornamos el valor de porcentaje. Podemos utilizar la función round para poder redonder a x decimales.

print("Porcentaje sala 1: ", porcentaje_disponible(sala2))


def espacio_suficiente(m,sala): #Creamos la función espacio_suficiente con parámetro m que equivale a cantidad de amigos y el parámetro sala
    cantidadDisponible = 0 #Inicializamos la variable en 0
    for fila in sala: #Comenzamos a recorrer la lista sala por cada fila que viene siendo una lista
        for asiento in fila:  #Aquí recorremos cada posición dentro de las listas fila
            if asiento == "O": #Si la posición dentro de la fila es igual a O
                cantidadDisponible+=1   #Sumamos uno a cantidad de asientos disponibles
    
    if m <= cantidadDisponible: #Si la cantidad de amigos es menor o igual a los asientos disponibles, quiere decir que hay espacio para todos
        return True #Retorna True
    else: #De lo contrario, retorna False
        return False

print(espacio_suficiente(12,sala1))
print(espacio_suficiente(3,sala1))
print(espacio_suficiente(10,sala1))






