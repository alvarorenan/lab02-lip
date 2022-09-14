#MUITO DIFICIL

import math
n = int(input())
lista_pontos = []
for x in range(n):
    x = float(input())
    y = float(input())
    lista_pontos.append((x,y))
distancias = []
for x in range(len(lista_pontos)):
    for y in range(x+1, len(lista_pontos)):
        distancias.append(math.sqrt((lista_pontos[x][0]-lista_pontos[y][0])**2 + (lista_pontos[x][1]-lista_pontos[y][1])**2))
maior = max(distancias)
pontos_mais_distantes = []
for x,y in lista_pontos:
    for a,b in lista_pontos:
        if math.sqrt((x-a)**2 + (y-b)**2) == maior:
            pontos_mais_distantes.append((x,y))
print(f"Mais distantes: ({pontos_mais_distantes[0][0]:.2f}, {pontos_mais_distantes[0][1]:.2f}) ({pontos_mais_distantes[1][0]:.2f}, {pontos_mais_distantes[1][1]:.2f})")



# n = int(input())
# lista_pontos = []
# for x in range(n):
#     x = float(input()).__round__(2)
#     y = float(input()).__round__(2)
#     lista_pontos.append((x,y))
# distancias = []
# for x in range(len(lista_pontos)):
#     for y in range(x+1, len(lista_pontos)):
#         distancias.append(((lista_pontos[x][0] - lista_pontos[y][0])**2 + (lista_pontos[x][1] - lista_pontos[y][1])**2)**(1/2))
# maior = max(distancias)
# pontos_mais_distantes = []
# for x in lista_pontos:
#     for y in lista_pontos:
#         if ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5 == maior:
#             pontos_mais_distantes.append((x, y))

# print(f"Mais distantes: ({pontos_mais_distantes[0][0][0]:.2f}, {pontos_mais_distantes[0][0][1]:.2f}) ({pontos_mais_distantes[0][1][0]:.2f}, {pontos_mais_distantes[0][1][1]:.2f})")






