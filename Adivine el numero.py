import random
numero = random.randint(0, 99)
intento = input(Introduzca numero entre 0 y 99: ))
numero_intentos = 1
print("Adivine el numero")
print("Introduzca el numero a adivinar")

def pedir_numero():
    while True:
        while True:
            intento = input("Introduzca un numero entre 0 y 99: ")
            try:
                intento = int(intento)
            except:
                pass
            else:
                if 0 <= entrada <= 99:
                    break 
        if intento < numero:
            print("Demasiado pequeño")
        elif intento > numero:
            print("Demasiado grande")
        else:
            print("Ha ganado")
            break

print("" + str(numero_intentos))