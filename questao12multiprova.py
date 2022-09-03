n = int(input())
lista_numeros_pares = []
for x in range(n):
    if x % 2 == 0 and x != 0:
        lista_numeros_pares.append(x)
for x in lista_numeros_pares:
    print(x)