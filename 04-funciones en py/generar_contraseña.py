import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'f', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['$', '#', '%', '&', '/', '!', '¡']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasena = []

    for i in range(15):
        caracteres_random = random.choice(caracteres)
        contrasena.append(caracteres_random)

    contrasena = "". join(contrasena)
    return contrasena

def main():
    contrasena = generar_contrasena()
    print('tu nueva contraseña es: ',contrasena)

if __name__ == "__main__":
    main()