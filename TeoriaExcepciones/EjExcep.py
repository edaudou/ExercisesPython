while True:
    try:
      n=int(input("Escribe un número"))
      break
    except ValueError:
        print("Debes introducir un valor entero.")

cad=0
try:
    print(10/int(cad))
except ValueError:
    print("No se puede convertir a entero")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except:
    print("Otro error")
finally:
    print("El programa ha termiando.")

cad="a"
try:
    i=int(cad)
except ValueError as e:
    print(type(e))
    print(e.args)
    print(e)