from ast import Break
import random

def jugar(vidas):
    numero_random = random.randint(1, 100)
    numero_elegido = None

    while numero_random != numero_elegido:
        numero_elegido = int(input('Ingrese un número entre 1 y 100: '))

        if numero_random < numero_elegido:
            print('ELige un numero mas pequeño')
            vidas -= 1
        elif numero_random > numero_elegido:
            print('Elige un numero mas grande')
            vidas -= 1

        if vidas == 0:
            print('GAME OVER')
            break

        print(f'Te quedan {vidas} vidas')
    
    if numero_elegido == numero_random:
        print("FELICIDADES GANASTE")

def main():
    while True:
        menu = """

        ADIVINA EL NUMERO ALEATORIO    
        
        1- Nivel Dificil
        2- Nivel Intermedio
        3- Nivel Facil
        4- Salir del juego
        Ingrese una opción: """

        opcion = input(menu)

        if opcion == '1':
            jugar(5) 
        elif opcion == '2':
            jugar(8)
        elif opcion == '3':
            jugar(10)
        elif opcion == '4':   
            print('CERRANDO JUEGO')
            break
        else:
            print('Opcion incorrecta !!!')
            print('Vuelve a ingresar la opcion correcta')

#Punto de inicio de la aplicacion
if __name__ == '__main__':
    main()
