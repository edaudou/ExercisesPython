for x,y in zip(range(1,4),["ana","juan","pepe"]):
    print(x,y)

paises=["China","India","USA","Indonesia"]
poblaciones=[1391,1365,327,264]
print(list(zip(paises,poblaciones)))

for pais, poblacion in zip(paises,poblaciones):
    print("{}: {} millones de habitantes.".format(pais,poblacion))
