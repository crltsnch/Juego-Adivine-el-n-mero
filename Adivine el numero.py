import random
numero = random.randint(0, 99)
numero = int ()
intento = input ("piensa un numero entre 0 y 99: ")

print("numero" + str(0) + str(99))

while int(intento) != numero:
    if intento > numero:
        print("Demasiado grande")
    if intento < numero:
        print("Demasiado pequeño")

print("¡Ha ganado!")