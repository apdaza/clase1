from random import randint



def generar_lista(tam):
    lista = []

    while len(lista) < tam:
        numero = randint(1,9)
        if numero not in lista:
            lista.append(numero)

    return lista

def suma(lista):
    acum = 0
    for i in lista:
        acum += i
    return acum

def fibo(n):
    if n in [1,2]:
        return 1
    return fibo(n-1) + fibo(n-2)

def suma_rec(lista):
    if lista == []:
        return 0
    return lista[0] + suma_rec(lista[1:])

def ordenar(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista



lista = generar_lista(5)
print lista
print suma(lista), suma_rec(lista)
print ordenar(lista)
print [fibo(x) for x in range(1,11)]
