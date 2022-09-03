lista_numeros = []
for x in range(4):
    lista_numeros.append(int(input()))
for x in range(2):
    lista_numeros.remove(max(lista_numeros))
print(lista_numeros)