# Ejercicio 2
# Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado.
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra
# sus elementos por la pantalla.
i=0
lista=[]
while i<5:
    p=input("Escribe una palabra: ")
    lista.append(p)
    i=i+1
print(lista)
i=0
while i<5:
    n=lista[i]
    lista.reverse()
    i=i+1
print(lista)
