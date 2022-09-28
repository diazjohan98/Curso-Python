from persona import Persona

persona1 = Persona('Johan', 23)
persona1.__nombre = 'Diaz'
#persona1.__metodo_privado() 
print(persona1.get_nombre())
print(persona1)