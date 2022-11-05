#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y
#la media de todos los números introducidos.

from statistics import median

suma=0
num=int(input("Introduce un numero: "))
numDeNum=0
while num!=0 :
     numDeNum=numDeNum+1
     suma=suma+num
     num=int(input("Dime un numero: "))
media=suma/numDeNum
print("Suma ",suma," Media ",media)