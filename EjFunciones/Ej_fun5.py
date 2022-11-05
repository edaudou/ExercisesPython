#Crea una función “calcularMaxMin” que recibe una lista con valores 
# numéricos y devuelve el valor máximo y el mínimo. 
# Crea un programa que pida números por teclado y muestre el máximo y
#  el mínimo, utilizando la función anterior
def calcularMaxMin():
    l=[]
    n=1
    while n>0:
        n=int(input("Introduce el numero"))
        l.append(n)
    print(f"El minimo es {min(l)}")
    print(f"El maximo es {max(l)}")
calcularMaxMin()