saldo = int(input("Ingrese el saldo inicial: "))

print(saldo)

print("Bienvenido al cajero automático, qué desea hacer?\n"
        "1.- Añadir dinero\n"
        "2.- Retirar dinero\n"
        "3.- Mostrar dinero\n"
        "4.- Salir")


oportunidades = 3

while oportunidades > 0:

    opcion = int(input("Ingrese la opción del 1 al 4: "))

    if opcion == 1:
        extra = int(input("Ingrese su dinero: "))
        saldo += extra
        print("El saldo es: ", saldo)
        break

    elif opcion == 2:
        retiro = int(input("Ingrese el dinero a retirar: "))
        if retiro > saldo:
            print("Saldo insuficiente :(")
            oportunidades= oportunidades -1
        else:
            saldo = saldo - retiro
            print("Su saldo es: ", saldo)
            break

    elif opcion == 3:
        print(saldo)
        break

    elif opcion == 4:
        print("Gracias por utilizarme")
        break

    else:
        print("Error")
        oportunidades-=1
