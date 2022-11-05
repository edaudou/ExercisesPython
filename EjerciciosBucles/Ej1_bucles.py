from math import factorial


n=int(input("Introduce un numero: "))
factorial=1
aux=n
while n>1:
    factorial=n*factorial
    n=n-1
print(aux,"!=",factorial)