tramo = int(input("Duración del tramo :"))
total = int(0)
while(tramo!=0):
    total = tramo + total
    tramo = int(input("Duracion del tramo :"))
if(total < 60):
    print("tiempo total de viaje :",total)   
else:
    print("tiempo total de viaje :",total//60,":",total%60)


