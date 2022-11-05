#Escribe un programa que lea una cadena y devuelva un diccionario
#con la cantidad de apariciones de cada carácter en la cadena.
d={}
str=input("Escribe una cadena: ")
for c in str:
    d[c]=str.count(c)
print(d)