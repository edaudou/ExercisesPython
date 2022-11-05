#conversion
cad=str(7.8)
print(cad)

#slice
cadena="informática"
print(cadena[2:5])
print(cadena[2:7:2])
print(cadena[:5])
print(cadena[5:])
print(cadena[-1:-3])
print(cadena[::-1])

#inmutable
print(cadena.upper())
print(cadena)
cadena=cadena.upper()
print(cadena)

cad="hola, Como estás?"
#formato
print(cad.capitalize())
print(cad.lower())
print(cad.upper())
print(cad.swapcase())
print(cad.title())

#búsqueda
cad="bienvenido a mi aplicación"
print(cad.count("a"))
print(cad.count("a",16))
print(cad.count("a",10,16))

print(cad.find("mi"))
print(cad.find("hola"))

#sustitución
buscar="nombre apellido"
remplazar_por="Juan Perez"
print("Estimado Sr. nombre apellido:".replace(buscar,remplazar_por) )

cad="   hola   "
print(cad.strip())
print(cad.strip("0"))

cad="12:23:12"
print(cad.split(":"))

cad="hola\nadios\nhola"
print(cad.splitlines())
#validación
cad="bienvenido a mi aplicación"
print(cad.startswith("b"))
print(cad.startswith("v",4))
print(cad.endswith("ción"))
print(cad.endswith("ción",0,10))
print(cad.endswith("nido",0,10))
#trabajo con unicode

print(chr(97))
print(chr(1004))
print(ord("a"))
print(ord("Ϭ"))