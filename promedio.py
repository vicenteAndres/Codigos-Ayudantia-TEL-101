cantidadNotas = int(input("Ingrese la cantidad de notas: "))

listaNotas = list()

for i in range(cantidadNotas):
    nota = float(input("Ingrese su nota: "))
    listaNotas.append(nota)

print(listaNotas)

promedio = sum(listaNotas)/cantidadNotas

print(promedio)

if promedio >= 55:
    print("El estudiante ha aprobado la asignatura :)")

else:
    print("El estudiante ha reprobado la asignatura:c")