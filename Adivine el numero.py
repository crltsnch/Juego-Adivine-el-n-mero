import random
entrada = random.randint(0, 99)
print("Adivine el numero")
numero_intentos = 1
def pedir_numero():
    while True:
        entrada = input("Introduzca un número entre 0 y 99: ")
        try:
            entrada = int(entrada)
        except:
            pass
        else:
            if 0 <= entrada <= 99:
                break

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