lista_numeros = []
for x in range(3):
    lista_numeros.append(int(input()))
lista_numeros.remove(min(lista_numeros))
lista_numeros.remove(max(lista_numeros))
print(lista_numeros[0])