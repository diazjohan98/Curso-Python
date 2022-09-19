"""
plicación 03: Suma de n números anteriores
Enunciado: obtener la suma de los primeros N número natural positivo.

Análisis: Para la solución de este problema, se requiere que el usuario ingrese un número y el sistema realice el proceso para devolver la suma de los N primeros números.


c = 0
while c < 10:
    c += 1
    print('calor de c ', c)
"""

n = int(input('Ingrese un numero: '))

suma = 0
menores_n = 0

while menores_n < n:
    suma += menores_n
    menores_n+= 1

print('La suma es: ', suma)