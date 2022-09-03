from audioop import reverse


n = int(input())
lista_cidades = []
for x in range(n):
    lista_cidades.append(input())
lista_cidades.sort()
for x in lista_cidades:
    print(x)
