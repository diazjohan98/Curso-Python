"""
Practica 02: calcular precio de venta

Enunciado: dado el valor de venta de productos, hallar 
el IGV(18%) y el precio de venta.

Analisis: para la solucion de este problema,
se requiere que el usuario ingrese el valor de venta
del producto y el sistema realice el calculo 
respectivo para hallar el IGV y el precio de venta, para
esto use la siguiente expresion.

igv = vv * 0.18 

pv = vv + igv
"""
print('---REALIZAR UNA VENTA---')
vv = float(input('Valor del producto es: '))

igv = vv * 0.18

pv = vv + igv


print('='*25)
print('----FACTURA DE VENTA----')
print('='*25)
print('valor de venta: ', vv)
print('IGV: ', igv)
print('el valor total es: ', pv)
print('='*25)