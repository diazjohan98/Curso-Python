from cgi import print_form
from persona import Persona

persona1 = Persona('Johan', 23)

persona1.mostrar_datos()

persona1.nombre = 'Diaz'
persona1.mostrar_datos()

print(persona1)