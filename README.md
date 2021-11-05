# Juego-Adivine-el-n-mero

Mi direccion de GitHub para para este repositorio es la siguient: [GitHub](https://github.com/crltsnch/Juego-Adivine-el-n-mero.git)
https://github.com/crltsnch/Juego-Adivine-el-n-mero.git

Hemos resuelto un juego de adivinar valores entre 0 y 99.
El diagrama de flujo que tenemos de nuestro codigo es:

! [diagrama de flujo adivine el num ero] (/crltsnch/Juego-Adivine-el-n-mero/Untitled.png)
```
importar al azar
numero  =  int ( aleatorio . randint ( 0 , 99 ))
print ( "Adivine el numero" )
intento  =  int ( input ( "piensa un numero entre 0 y 99 incluidos:" ))
numero_intentos  =  1

print ( "piensa un numero entre 0 y 99 incluidos:" )
si  intento  ==  numero :
    print ( "Ha ganado" )

otra cosa :
    if  int ( intento ) <  numero :
        print ( "Demasiado pequeño" )
    elif  int ( intento ) >  numero :
        print ( "Demasiado grande" )
    while  int ( intento ) ! =  numero :
        intento  =  int ( input ( "piensa un numero entre 0 y 99 incluidos:" ))
        numero_intentos  + =  1
        if  intento  >  numero :
            print ( "Demasiado grande" )
        elif  intento  <  numero :
            print ( "Demasiado pequeño" )
        elif  intento  ==  numero :
            print ( "Ha ganado" )
print ( ""  +  str ( numero_intentos ))
```
