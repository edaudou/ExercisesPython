#Escribe un programa python que pida un número por teclado y que cree 
# un diccionario cuyas claves sean desde el número 1 hasta el número
# indicado, y los valores sean los cuadrados de las claves

d={}
n=int(input("Escribe un número: "))
for i in range(1,n+1):
     d[i]=i*i
print(d)