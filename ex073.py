lista = ('Palmeiras', 'Santos', 'Vasco da gama', 'Gremio', 'Flamengo', 'Corinthians','internacional', 'Cruzeiro', 'São paulo', 'Atletico mineiro')
print('Lista de times do Brasileirão:',lista)
print('==' * 20)
print('Os 5 Primeiros são:',lista[0:5])
print('==' * 20)
print('Os 4 Ultimos são:',lista[-4:])
print('==' * 20)
print('Time em ordem alfabética:',sorted(lista))
print('==' * 20)
print(f'O Vasco da gama esta na {lista.index("Vasco da gama") + 1}ª posição')
print('==' * 20)


