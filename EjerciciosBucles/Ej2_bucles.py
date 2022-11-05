#*Crea una aplicación que permita adivinar un número. La aplicación genera un número
#aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el
#número a adivinar es mayor o menor que el introducido,a demás de los intentos que te
#quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el
#número (además te dice en cuantos intentos lo has acertado), si se llega al limite de
#intentos te muestra el número que había generado.
import random

nA=random.randint(1,100)
nIntento=0
while nIntento<=10:
    nIntento=nIntento+1   
    n=int(input("Introduce un numero: "))
    if(n>nA):
        print("El numero es menor")
    if(n<nA):
        print("El numero es mayor")
    if(n==nA):
        print("Acertado en" ,nIntento)
        nIntento+1
        break
print("El número era ",nA)