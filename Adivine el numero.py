import random
numero = int(random.randint(0, 99))
print("Adivine el numero")
intento = int(input("piensa un numero entre 0 y 99 incluidos: "))
numero_intentos = 1

print("piensa un numero entre 0 y 99 incluidos: ")
if intento == numero:
    print("Ha ganado")

else:
    if int(intento) < numero:
        print("Demasiado pequeño")
    elif int(intento) > numero:
        print("Demasiado grande")
    while int(intento) != numero:
        intento = int(input("piensa un numero entre 0 y 99 incluidos: "))
        numero_intentos += 1
        if intento > numero:
            print("Demasiado grande")
        elif intento < numero:
            print("Demasiado pequeño")
        elif intento == numero:
            print("Ha ganado")
print("" + str(numero_intentos))