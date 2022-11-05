#read
import csv
fichero=open("a.csv")
contenido=csv.reader(fichero)
datos=list(contenido)
print(datos[0][0])
print(datos[1][1])
for row in contenido:
    print("Fila"+str(contenido.line_num)+ " "+str(row))
fichero.close()

#write
fichero=open("b.csv","w")
contenido=csv.writer(fichero)
contenido.writerow(['aaa','rrr'])
contenido.writerows(['aaa','rrr'],['a242a','rdgfar'],['a5454a','r5454rr'])