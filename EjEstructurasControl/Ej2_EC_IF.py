# Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y
#el exponente. Pueden ocurrir tres cosas:
#El exponente sea positivo, sólo tienes que imprimir la potencia. 
#El exponente sea 0, el resultado es 1.
#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base=int(input("Escribe la base: "))
exponente=int(input("Escribe el exponente: "))

if exponente==0:
    print(1)
elif exponente>0:
    #print(pow(base,exponente))
    print(base**exponente)
else: #exponente negativo
    print(1/(base**(exponente*(-1))))