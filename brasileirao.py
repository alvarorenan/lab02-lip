lista_brasileirao = ['Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlético-MG', 
'São Paulo', 'Grêmio', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 
'Corinthians', 'Fluminense', 'Bahia', 'Vasco', 'Sport', 
'América-MG', 'Chapecoense', 'Vitória', 'Paraná', 'Atlético-GO']

lista_libertadores = lista_brasileirao[0:6]

lista_rebaixados = lista_brasileirao[-4:]

time_maior_nome = max(lista_brasileirao, key=len)

lista_metade = lista_brasileirao[0:10]
lista_metade_reversa = lista_brasileirao[10:20]
lista_metade_reversa.reverse();

print('Lista de times classificados para a Libertadores: {}'.format(lista_libertadores))
print('\nLista de times rebaixados: {}'.format(lista_rebaixados))
print('\nTime com maior nome: {}'.format(time_maior_nome))


for x in lista_metade:
    print(x, "X", lista_metade_reversa[lista_metade.index(x)])


