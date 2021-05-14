cantidadPersonas = int(input("Inrgese la cantidad de gente que asiste: "))

contador = 0
precio = 0
pagoTotal = 0

while contador < cantidadPersonas:

    edad = int(input("Ingrese la edad: \n"))

    if edad < 3 and edad > 0:
        precio = 0
        pagoTotal += precio
    elif edad >= 3 and edad <= 12:
        precio = 10
        pagoTotal+=precio
    elif edad > 12:
        precio = 15
        pagoTotal+=precio
    
    contador+=1

if cantidadPersonas > 0 and cantidadPersonas < 3:
    pagoTotal= pagoTotal*0.9 #Descuento del 10%
elif cantidadPersonas >= 3 and cantidadPersonas <6:
    pagoTotal = pagoTotal*0.75 #Descuento del 25%
elif cantidadPersonas >= 10: 
    pagoTotal= pagoTotal*0.5 #Descuento del 50%

print("El total a pagar es: ", pagoTotal, " dólares")

