#lectura
f=open("a.txt","r")
print(f.read())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

#escritura
f=open("b.txt","w")
f.write("Prueba 1\n")
print("Prueba 2\n",file=f)
f.writelines(["Prueba 3", "Prueba 5"])

#recorrido
with open("a.txt","r") as fichero:
    for linea in fichero:
        print(linea)
fichero.closed