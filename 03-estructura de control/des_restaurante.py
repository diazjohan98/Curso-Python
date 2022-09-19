# entrada

consumo = float(input('Ingrese el consumo del cliente: '))

if consumo >= 0:
# Proceso

    if consumo <= 100:
        #descuento 10%
        dato_descuento = '10%'
        descuento = consumo * 0.10

    elif consumo > 100 and consumo < 200:
        #descuento 20%
        dato_descuento = '20%'
        descuento = consumo * 0.20
    elif consumo > 200:
        #descuento de 30%
        dato_descuento = '30%'
        descuento = consumo * 0.30
        

    monto_descuento = consumo - descuento
    igv = monto_descuento * 0.19
    total_pago = monto_descuento + igv

    print('=' * 30)
    print('-----Factura de Consumo-----')
    print('Descuento que se aplica:', dato_descuento)
    print('=' * 30)
    print('Consumo: ',consumo)
    print('Descuento: ', descuento)
    print('Monto con Descuento: ', monto_descuento)
    print('IGV: ', igv)
    print('=' * 30)
    print('Total a pagar: ', total_pago)
    print('=' * 30)

else:
    print('Error al ingresar el consumo')