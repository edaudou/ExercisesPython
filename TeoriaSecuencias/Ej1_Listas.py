#recorrido
lista=[1,2,3,4,5,6]
for num in lista:
    print(num,end="")
lista2=["a","b","c","d","e"]
print()
for num,letra in zip(lista,lista2):
    print(num,letra)
#permanencia
print(2 in lista)
print("a" not in lista2)

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
print(lista[5:])
print(lista[:5])
print(lista[::-1])

#funciones
#longitud
print(len(lista))
#max y min
print(max(lista))
print(min(lista))
#suma
print(sum(lista))
#ordenación
print(sorted(lista))
print(sorted(lista,reverse=True))
 

#listas multidimensionales
tabla=[[1,2,3],[4,5,6],[7,8,9]]
print(tabla[1][1])
for fila in tabla:
    for elem in fila:
        print(elem,end="")
    print()

#mutabilidad
lista1=[1,2,3]
lista1[2]=4
print(lista1)
del lista1[2]
print(lista1)


#COPIAR LISTAS
#así NO
lista1=[1,2,3]
lista2=lista1
lista1[1]=10
print(lista2)
#así SI
lista1=[1,2,3]
lista2=lista1[:]
lista1[1]=10
print(lista2)


#inserción
lista1.append(3)
print(lista1)
lista1.append(4)
print(lista1)

lista2=[5,6]
lista1.extend(lista2)
print(lista1)

lista1.insert(1,100)
print(lista1)

#eliminación
lista1.pop()
print(lista1)

#eliminación por posición
lista1.pop(1)
print(lista1)

#eliminación por valor solo el primero
lista1.remove(3)
print(lista1)

#ordenación
lista.reverse()
print(lista)

lista.sort()
print(lista)

lista.sort(reverse=True)

lista=["zhola","que","tal"]
lista.sort()
print(lista)

#busqueda
lista=[1,2,3,4,5,6]
print(lista.count(5))

print(lista.append(5))

print(lista.index(5))

#print(lista.index(5,1,4))