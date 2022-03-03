def ficha(jog ='<Desconhecido>', gols = 0):
    print(f'O Jogador {jog} fez {gols} gol(s) no campeonato.')


print('-=' * 15)
n = str(input('Nome do jogador: '))
g = str(input('Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols= g)
else:
    ficha(n, g)