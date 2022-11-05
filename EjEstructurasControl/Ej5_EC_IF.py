#Escribe un programa que pida un nombre de usuario y una contraseña y si
#se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”,
#sino se da un err

usuario=input("Introduce el usuario: ")
contra=input("Introduce la contraseña: ")
if usuario=="pepe" and contra=="asdasd":
    print("Has entrado en el sistema")
elif usuario!="pepe" and contra=="asdasd":
    print("El usuario es incorrecto")
elif usuario=="pepe" and contra!="asdasd":
    print("La contraseña es incorrecta")
else:
    print("El usuario y la contraseña son incorrectos")