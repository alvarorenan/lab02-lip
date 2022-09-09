n = int(input())
lista_impares = []
for x in range(n+1):
    if x % 2 != 0:
        lista_impares.append(x)
v1 = int(input())
v2 = int(input())
print(sum(lista_impares[v1:v2+1]))
