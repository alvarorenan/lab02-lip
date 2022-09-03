lista_nomes = []
for n in range(3):
    lista_nomes.append(input())
lista_quantidade_caracteres = []
for x in lista_nomes:
    lista_quantidade_caracteres.append(len(x))
print(lista_quantidade_caracteres)