from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
r = 0
while r != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    r = int(input('>>>> Qual é a sua opção? '))
    if r == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
    elif r == 2:
        print('A multiplicação de {} X {} é {}'.format(n1, n2, n1 * n2))
    elif r == 3:
        if n1 > n2:
            print('O maior valor é de {}'.format(n1))
        else:
            print('O maior valor é de {}'.format(n2))
    elif r == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif r == 5:
        print('Finalizando...')
    else:
        print('Opção invalida tente novamente!')
    sleep(2)
print('Fim do programa volte sempre !!')