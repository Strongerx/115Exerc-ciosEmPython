def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end='')
    if cont == 0:
        maior = valor
    else:
        if valor > maior:
            maior = valor
    cont += 1
    print(f'\nForam informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


# Progama principal
maior(3 , 4 , 4 , 5 ,7 )
maior(2, 5, 3 ,2 , 6)