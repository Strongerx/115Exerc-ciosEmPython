from random import randint
c = 0
computador = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número de entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
p = int(input('\033[1;31mQual o seu palpite?\033[m '))
while p != computador:
    if p >= computador:
        p = int(input('Menos... tente mais uma vez  '))
        c += 1
    else:
        p = int(input('Mais... tente mais uma vez  '))
        c += 1
print('\033[1;31mAcertou com {} tentativas. Parabéns !'.format(c + 1))