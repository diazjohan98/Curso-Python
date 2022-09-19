from pickle import TRUE

"""
Estas son las aplicaciones y practicas que se realizaran en esta sección.
Aplicación 01: Crear un sistema que detecte si número es par positivos o 
par negativo y también si es impar positivo o negativos y si el numero 
ingresado es 0 que detecte si es neutro.
Enunciado: determinar si un número entero es par positivo, impar positivo, 
par negativo, impar negativo o neutro.

Análisis: para la solución de este problema, se requiere que el usuario 
ingrese un número entero y el sistema verifique si es par positivo, impar 
positivo, par negativo, impar negativo o neutro.

"""

n = int(input('Ingrese un número entero: '))

if n != 0:
    if n > 0:
        if n % 2 == 0:
            print(f'El numero {n} es PAR POSITIVO')
        else:
            print(f'El numero {n} es IMPAR POSITIVO')
    else:
        if n % 2 == 0:
            print(f'El numero {n} es PAR NEGATIVO')
        else:
            print(f'El numero {n} es IMPAR NEGATIVO')
else:
    print(f'El numero {n} es NEUTRO')

