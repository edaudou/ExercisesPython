#Realizar un programa que inicialice una lista con 10 valores aleatorios
#  (del 1 al 10) y posteriormente muestre en pantalla 
# cada elemento de la lista junto con su cuadrado y su cubo.
import random
from tkinter import N
i=0
lista=[]
while i<10:
    lista[i]=random.randint(1, 10)
    i=i+1
i=0
while i<10:
    n=lista[i]
    cuadrado=n*n
    cubo=n**3
    print("Numero ",n," Cuadrado ",cuadrado," Cubo ",cubo)
    i=i+1
