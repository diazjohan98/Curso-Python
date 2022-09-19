
def saludar(nombre):
    #global nombre
    return f'Hola, {nombre} desde la funcion saludar'
    
def sumar(a, b):
    return a + b

def restar(a=None, b=None):
    if a == None or b ==None:
        print('Error: debes de enviar dos numeros a la funcion')
    return a - b

saludo = saludar('Johan')
print(saludo)

suma = sumar(10, 20)
print('La suma es: ', suma)

# resta = restar(b = 20, a = 40)
resta = restar()
print('La resta es: ', resta)



# print(saludar()) puede ser una opcion 
#print('Hola desde fuera de la funcion', nombre)

