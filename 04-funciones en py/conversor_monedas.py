
def convertir(valor_dolar, pais):
    cantidad_moneda = float(input(f'Ingrese cantidad de {pais}: '))

    dolares = cantidad_moneda / valor_dolar
    dolares = round(dolares, 2)
    print(f'Tienes ${dolares} Dolares')

def main():
    while True:
        menu = """ 
        1 - soles Peruanos a Dolares
        2 - Pesos colombiano a Dolare
        3 - Pesos Mexicanos a Dolars
        4 - Salir
        Ingrese una Opcion: """

        opcion = input(menu)

        if opcion == '1':
            convertir(3.86, 'Soles Peruanos')
        elif opcion == '2':
            convertir(4422.46, 'Pesos Colombianos')
        elif opcion == '3':
            convertir(19.93, 'Pesos Mexicanos')
        elif opcion == '4':
            print('Cerrando conversor de monedas')
            break
        else:
            print('Opcion incorrecta !!!')
            print('Vuelve a ingresar la opcion correcta')

#Punto de inicio de la aplicacion
if __name__ == '__main__':
    main()