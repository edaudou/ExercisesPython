#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math
c1=int(input("Dime el cateto 1:"))
c2=int(input("Dime el cateto 2:"))
hipotenusa=math.sqrt(c1*c1+c2*c2)
print("La hipotenusa es: "+str(hipotenusa))