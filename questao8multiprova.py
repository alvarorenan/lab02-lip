n = int(input())
lista_pares = []
for x in range(n):
    if x % 2 == 0 and x != 0:
        lista_pares.append(x)
lista_pares_copia = lista_pares[:]
i1=int(input())
i2=int(input())
lista_pares_copia.pop(i1)
lista_pares_copia.pop(i2)
print(lista_pares)
print(lista_pares_copia)
