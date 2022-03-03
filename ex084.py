dados = []
povo = []
peso = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    povo.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Você cadastrou {len(povo)} pessoas')
print(f'O maior peso foi de {max(peso):.2f}Kg. Peso de ', end='')
for p in povo:
    if p[1] == max(peso):
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {min(peso):.2f}Kg. Peso de ', end='')
for p in povo:
    if p[1] == min(peso):
        print(f'{p[0]} ', end='')