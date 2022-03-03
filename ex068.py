from random import  randint
print('==' * 20)
print('        VAMOS JOGAR PAR OU IMPAR ')
print('==' * 20)
cont = soma = 0
v = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    total = jogador + computador
    print(f'Você jogou {jogador} e computador jogou {computador}, total de {total}', end=' ')
    print('Deu Par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu !')
            v += 1
        else:
            print('Você perdeu !')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu !')
            v += 1
        else:
            print('Você perdeu !')
            break
    print('Vamos jogar novamente...')
print('Game over !!!')


