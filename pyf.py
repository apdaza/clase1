from random import randint

lista = []

for i in range(10):
    if len(lista) == 3:
        break
    lista.append(randint(0,9)) 
    if lista[-1] in lista[:-1]:
        lista.pop()

print lista
