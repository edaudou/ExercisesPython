#recorrerlas
lista=[1,2,3,4,5,6]
for num in lista:
    print(num,end="")
print(lista)

#pertenencia
print(2 in lista)
print(8 not in lista)

#concatenación (no range ni conjuntos)
lista=lista+[7,8,9]
print(lista)

#repetición (no range ni conjuntos)
lista=lista*2
print(lista)

#indexación
print(lista[5])

#slice (no conjuntos)
print(lista[2:6])
print(lista[1:4:2])

#longitud
print(len(lista))

#max y min
print(max(lista))
print(min(lista))

#PARA LAS MUTABLES

#modificar un dato por posición
lista[3]=345
print(lista)

#modificar un subconjunto con slice
lista[5:8]=[400,500,600]
print(lista)

#eliminar un subconjunto con slice
del lista[5:]
print(lista)

#modificar con *=
lista*=2
print(lista)
