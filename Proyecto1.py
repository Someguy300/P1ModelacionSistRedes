#main
print("""Sistema de gestion de viajes Agencia de Viajes Metro Travel
Antes de gestionar su viaje debemos preguntarle:""")

while True:
    print("¿Usted posee visa?")
    print("Presione [y] y [Enter] para Si")
    print("Presione [n] y [Enter] para No")
    inputVisa = input()
    if inputVisa == 'y' or inputVisa == 'n':
        break
    else:
        print("Ingrese un valor valido [y] o [n]")


print()
if inputVisa == 'y':
    print("Dada su disponibilidad de visa estas sus sus siguientes opciones para su aeropuerto de origen")
else:
    print("Dada su no disponibilidad de visa estas sus sus siguientes opciones para su aeropuerto de origen")

#INSERTAR AEROPUERTOS DE ORIGEN E INPUT AQUI

print()
print("Los aeropuertos disponibles como aeropuertos destino son:")

#INSERTAR AEROPUERTOS DESTINO E INPUT AQUI

print()
print("""Como desea planear su viaje?
Escogiendo la ruta mas barata? ó
Escogiendo la ruta con numero de vuelos minima?""")



while True:
    try:
        print("Presione [1] y [Enter] para ruta mas barata")
        print("Presione [2] y [Enter] para numero de vuelos minima")
        inputCriterio = int(input())
    except Exception:
        print("Ingrese un valor valido [1] o [2]")
        continue
    else:
        if inputCriterio == 1 or inputCriterio == 2:
            break
        else:
            print("Ingrese un valor valido [1] o [2]")

print()
if inputVisa == 1:
    print("Su viaje de acuerdo a la ruta mas barata es el siguiente")
else:
    print("Su viaje de acuerdo a la ruta con el minimo numero de vuelos es el siguiente")

#MOSTRAR RUTAS CON COSTO AQUI
