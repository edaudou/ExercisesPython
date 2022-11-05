print(type(5))
print(type(5.7))
print(type([2,4]))
print(type(True))

#Tipos numéricos (int, float)
a=int(7.5)
print(a)
a=int("3434")
print(a)
b=float(1)
print(b)
b=float("1.345")
print(b)
print(7/2)
print(7//2)
print(divmod(7,2))
import math
print(math.pow(3,4))
print(abs(-7))
print(round(7.7564,2))

#Tipos booleanos
#True, Flase
a=True
print(a, type(a))
a="Pepe"
print(a, type(a))

#Cadenas de caracteres
cad1="Hola"
cad2='¿Qué tal?'
cad3='''Hola, que tal'''

#comparación
print("a">"A")
print("informatica">"informacion")
print(cad1>cad2)

#concatenacion
print("a"+"b")
print("a"+str(1))
print("a",1)

#repeticion
print("abc"*3)

#indexación
cadena="jose"
print(cadena[0])
print(cadena[3])

#longitud
print(len(cadena))