import matplotlib.pyplot as plt


def leer_datos(archivo1,archivo2):
    try:
        arch1 = open(archivo1,"r")
        arch2 = open(archivo2,"r")
    except OSError:
        print("Alguno de los archivos no se encuentra disponible. Revíselos")
    else:
        nombreProductos = []
        cantidadVendidas = []
        precioProductos = []
        categoriaProductos = []
        for i in arch1:
            linea = i.strip().split()
            nombreProductos.append(linea[0])
            cantidadVendidas.append(linea[1])

        for j in arch2:
            linea = j.strip().split()
            precioProductos.append(linea[1])
            categoriaProductos.append(linea[2])
        return [nombreProductos,cantidadVendidas,precioProductos,categoriaProductos]

print(leer_datos("ventas.txt","datos.txt"))

def por_tipo(tipo_prod, L):

    listaProd = []
    listaCantidad = []
    listaPrecios = []
    listaVentas = []
    for x in range (0, len(L[3])):
        #print (L[3][x])
        if L[3][x] == tipo_prod:
            listaProd.append(L[0][x])
            listaCantidad.append(L[1][x])
            listaPrecios.append(L[2][x])
    for x in range (0, len(listaProd)):
        ventaTotal = int(listaCantidad[x]) * int(listaPrecios[x])
        listaVentas.append(ventaTotal)
    #print(listaProd)
    #print(listaVentas)
    
    fig = plt.figure(dpi = 100)
    plt.plot(listaProd,listaVentas, "o-")
    fig.suptitle("Venta Semanal de " + tipo_prod, fontsize=20)
    plt.xlabel('Productos', fontsize=14)
    plt.ylabel('Venta Total', fontsize=14)
    plt.show()

lista = leer_datos("ventas.txt","datos.txt")
por_tipo("Abarrotes", lista)



listaDatos = leer_datos("ventas.txt","datos.txt")
def compara_tipo(datos):
    listaCantidad = []
    listaTipo = []
    listaTamaño = []
    cantidadTotal = 0
    for x in range (0, len(datos[3])):
        if datos[3][x] not in listaTipo:
            listaTipo.append(datos[3][x])

    for tipo in listaTipo:
        cantidadTipo = 0
        for x in range(len(datos[3])):
            if tipo == datos[3][x]:
                cantidadTipo += int(datos[1][x]) * int(datos[2][x])
        listaCantidad.append(cantidadTipo)
        cantidadTotal += cantidadTipo
    for x in range (len(listaTipo)):
        porcentaje = listaCantidad[x] * 100 / cantidadTotal
        listaTamaño.append(porcentaje)

        
    etiquetas = listaTipo
    tamaño = listaTamaño


    fig1 = plt.figure(dpi=100)
    ax1 = fig1.add_subplot(1,1,1)
    
    ax1.pie(tamaño, labels=etiquetas, autopct="%.1f%%", shadow = True, startangle=0)
    fig1.suptitle("Ventas Semanales totales $"+str(cantidadTotal), fontsize=20)
    plt.show()
    
compara_tipo(listaDatos)
    
    
