#Cantidad mínima de billetes

dinero = int(input("Ingrese la cantidad de dinero: \n"))

billetes20k = dinero // 20000
dinero-= (billetes20k*20000)

billetes10k = dinero // 10000
dinero-= (billetes10k*10000)

billetes5k = dinero // 5000
dinero-= ( billetes5k*5000)

billetes2k = dinero // 2000
dinero-= (billetes2k*2000)

billetes1k = dinero // 1000
dinero = dinero - (billetes1k*1000)

print("La cantidad de billetes de 20k es: ", billetes20k)
print("La cantidad de billetes de 10k es: ",billetes10k)
print("La cantidad de billetes de 5k es: ", billetes5k)
print("La cantidad de billetes de 2k es: ", billetes2k)
print("La cantidad de billetes de 1k es: ",billetes1k)