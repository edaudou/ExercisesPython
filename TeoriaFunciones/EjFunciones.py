def operar(a,b):
    suma=a+b
    resta=a-b
    print(suma," ",resta)
operar(4,5)


PI=3.1415
def area(radio):
    return PI*radio**2
print(area(2))

def CalcularMaximo(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
numero1=int(input("Dime el numero 1"))
numero2=int(input("Dime el numero 2"))
num_max=CalcularMaximo(numero1,numero2)
print("El número máximo es:",num_max)

#paso por valor y referencia
#datos inmutable
def f(a):
    a=5
a=1
f(a)
print(a)

#tipos de datos mutable
def f(lista):
    lista.append(5)
l=[1,2]
f(l)
print(l)

def cuadrado(n):
    return n*n
a=cuadrado(2)
print(cuadrado(3)+1)

print(cuadrado(cuadrado(4)))
print(type(cuadrado(2)))
