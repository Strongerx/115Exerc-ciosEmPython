numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado, não vou adicionar !')
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r in 'N':
        break
print(f'Os valores digitados foram {sorted(numeros)}')