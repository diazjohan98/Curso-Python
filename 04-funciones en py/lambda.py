
from tkinter import Scrollbar


sumar = lambda a,b:a+b
doblar = lambda n: n*2
par = lambda n: n% 2 == 0
impar = lambda n: n != 0
revertir = lambda cadena: cadena[: :-1]

print(sumar(10,30))
print(doblar(10))
print(par(4))
print(impar(6))
print(revertir('Hola'))
