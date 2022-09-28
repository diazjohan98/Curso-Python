
from functools import partial


def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False

#Funcion Principal
def main():
    palabra = input('Ingrese una palabra: ')

    es_palindromo = palindromo(palabra)

    if es_palindromo:
        print('Es palindromo')
    else:
        print('No es palindromo')   

#punto de entrada de la aplicacion
if __name__ == '__main__':
    main()