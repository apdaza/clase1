from random import randint

lista = []

for i in range(3):
    lista.append(randint(0, 100))

print lista
# booleano inicializado en falso
adivinado = False

"""
ciclo que permite 5 opciones
verifica si el numero está en la lista
"""
for i in range(5):
    a = input("ingrese su valor: ")
    if a in lista:
        print "ganaste"
        adivinado = True
        break
    else:
        print "sigue intentando"

if not adivinado:
    cad = ""
    for i in lista:
        cad += str(i) + ", "
    print "el numero aleatorio fue: " + cad[:-2]
