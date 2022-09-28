from http import client
from persona import Cliente, Empleado

# cliente1 = Cliente('Johan', 23)
# cliente2 = Cliente('Diaz', 23)

# cliente1.detalle_persona()
# print(cliente2)

empleado1 = Empleado('Johan', 23, 15000)
empleado2 = Empleado('Diaz', 23, 8000)

empleado1.detalle_persona()
empleado1.detalle_empleado()

print(empleado2)