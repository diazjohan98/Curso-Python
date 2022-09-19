"""
Practica 01: Calcular cociente y residuo
Enunciado: hallar el cociente y residuo(resto)
de dos numeros enteros.
Analisis: para la solucion de este problema,
se requiere que el usuario ingrese dos
numeros enteros y el sistema realice el calculo
respectivo para hallar el cociente y residuo.
"""

print("HALLAR EL COCIENTE Y RESIDUO")

num1 =  input('Ingrese el primer numero:')
num2 =  input('Ingrese el segundo numero:')

#convertir a entero

num1 = int(num1)
num2 = int(num2)

#operacion
cociente = num1 // num2
residuo = num1 % num2

#salida
print('El cociente es: ', cociente)
print('El residuo es: ',residuo)