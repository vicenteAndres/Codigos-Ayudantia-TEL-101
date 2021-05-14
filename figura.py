altura = int(input("Ingrese altura: "))

ancho = int(input("Ingrese ancho: "))

contador = 0
while contador < altura:
    print("*" * ancho)
    contador += 1



#Forma a realizarlo con el ciclo for

"""
for i in range(1,altura+1):
    for j in range(1,ancho+1):
        print("*",end="")
    print("")
"""

