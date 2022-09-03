lista_brasileirao = ['Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlético-MG', 
'São Paulo', 'Grêmio', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 
'Corinthians', 'Fluminense', 'Bahia', 'Vasco', 'Sport', 
'América-MG', 'Chapecoense', 'Vitória', 'Paraná', 'Atlético-GO']

lista_libertadores = lista_brasileirao[0:6]

lista_rebaixados = lista_brasileirao[-4:]

time_maior_nome = max(lista_brasileirao, key=len)

lista_metade = lista_brasileirao[0:10]
lista_metade_reversa = lista_brasileirao[20:9:-1]

print(f"Lista de times que irão para a libertadores: {lista_libertadores}\n")
print(f"Lista de times que irão para a série B: {lista_rebaixados}\n")
print(f"Time com maior nome: {time_maior_nome}\n")

for x in lista_metade:
    print(x, "X", lista_metade_reversa[lista_metade.index(x)])


