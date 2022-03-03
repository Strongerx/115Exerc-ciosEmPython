dado = {}
partidas = []
dado['Nome'] = str(input('Nome do Jogador: '))
cont = int(input(f'Quantas partidas {dado["Nome"]} jogou? '))
for i in range(0, cont):
    partidas.append(int(input(f'Quantos gols na partida {i}? ')))
dado['gols'] = partidas[:]
dado['total'] = sum(partidas)
print('-=' * 30)
print(dado)
print('-=' * 30)
for k, v in dado.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
for d, v in enumerate(dado['gols']):
    print(f'     > Na partida {d}, fez {v} gols. ')
print(f'Foi um total de {dado["total"]} gols.')
