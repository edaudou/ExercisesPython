import time
tiempo=time.time()
print(time.localtime(tiempo))

print(time.localtime())
tiempo=time.localtime()
print(tiempo.tm_year)

print(time.asctime())

print(time.strftime('%d/%m/%Y %H:%M:%S'))