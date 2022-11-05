#Realizar un programa que comprueba si una cadena leída por 
# teclado comienza por una subcadena introducida por teclado.
cad=input("Escribe una cadena de caracteres")
subcad=input("Escribe una subcadena de caracteres")
long=len(subcad)
if cad[:long]==subcad:
    print("Si")
else:
    print("No")