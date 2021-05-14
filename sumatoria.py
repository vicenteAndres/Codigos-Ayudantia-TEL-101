numero = int(input("Ingrese el valor a calcular su sumatoria: \n"))

suma = 0
contador = 0

while contador <= numero:

    suma+=contador
    contador+=1

print("La sumatoria de ", numero, "es: ", suma)