import random
numero = random.randint(0, 99)
print("Introduzca el numero de adivinar")
numero = pedir_numero()

print("Intente adivinar el numero")
while True:
    while True:
        entrada = input("Introduzca un numero entre 0 y 99: ")
        try:
            entrada = int(entrada)
        except:
            pass
        else:
            if 0 <= entrada <= 99:
                break 

    if entrada < numero:
        print("Demasiado pequeño")
    elif entrada > numero:
        print("Demasiado grande")
    else:
        print("Ha ganado")
        break
return entrada