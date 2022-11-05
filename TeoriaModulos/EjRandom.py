import random
print(random.randint(10,200))

print(random.choice(["hola","que","tal"]))

frutas=["fresas","platanos","peras","manzanos"]
random.shuffle(frutas)
print(frutas)

lista=[3,4,1,27,8,9]
numeros=random.sample(lista,3)
print(numeros)
