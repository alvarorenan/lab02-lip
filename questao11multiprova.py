n = int(input())
lista_numeros = []
for x in range(1,n+1):
    lista_numeros.append(x)
lista_numeros_copia = lista_numeros[:]
v1 = int(input())
v2 = int(input())
lista_numeros_copia.remove(v1)
lista_numeros_copia.remove(v2)
print(lista_numeros_copia)
print(lista_numeros)
