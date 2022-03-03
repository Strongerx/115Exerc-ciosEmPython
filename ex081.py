cont = 0
list = []
while True:
    v = int(input('Digite um valor: '))
    cont += 1
    if v not in list:
        list.append(v)
    p = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if p in 'N':
        break
print(f'Você digitou {cont} elementos')
print(f'Os valores em ordem decrescente são {sorted(list, reverse=True)}')
if 5 in list:
    print('O valor 5 faz parte da lista !')
else:
    print('O valor 5 não faz parte da lista !')

