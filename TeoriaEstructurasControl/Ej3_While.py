from itertools import count


cont=0
while cont<10:
    if cont % 2 !=0:
        continue
    print(cont)
    cont=cont+1