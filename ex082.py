list = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    if n not in list:
        list.append(n)
    if n % 2 == 0:
        pares.append(n)
    if n % 2 == 1:
        impares.append(n)
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r in 'N':
        break
print(f'A lista completa é {list}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
