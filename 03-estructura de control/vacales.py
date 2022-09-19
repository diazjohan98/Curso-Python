"""
Aplicación 02: Crear un sistema que detecte si un carácter es vocal o no
Enunciado: dado un carácter determinar si es una vocal.

Análisis: para la solución de este problema, se requiere que el usuario 
ingrese un carácter y el sistema verifique si es una vocal.

"""
vocal = input('Ingrese un caracter: ')

if vocal == 'a' or vocal == 'A':
    print(vocal, 'ES VOCAL')
elif vocal == 'e' or vocal == 'E':
    print(vocal, 'ES VOCAL')
elif vocal == 'i' or vocal == 'I':
    print(vocal, 'ES VOCAL')
elif vocal == 'o' or vocal == 'O':
    print(vocal, 'ES VOCAL')
elif vocal == 'u' or vocal == 'U':
    print(vocal, 'ES VOCAL')
else:
    print(vocal, 'NO ES VOCAL')