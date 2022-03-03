from random import randint
from time import sleep
print ('\33[1;32mSuas opçoes: ')
print ('[ 0 ] PEDRA ')
print ('[ 1 ] PAPEL' )
print ('[ 2 ] TESOURA\33[m')
jogador = int(input('\33[1;32mQual a sua jogada?\33[m '))
computador = randint(0,2)
itens = ('Pedra', 'Papel', 'Tesoura')
print ('\33[1;31mJO\33[m')
sleep(1)
print ('\33[1;31mKEN\33[m')
sleep(1)
print ('\33[1;31mPO !!!\33[m')
print ('__' * 15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print ('__' * 15)
if computador == 0:
    if jogador == 0:
        print ('\33[1;32mEMPATE\33[1;31m')
    elif jogador  == 1:
        print ('\33[1;34mJOGADOR VENCE\33[m')
    elif jogador == 2:
        print ('\33[1;31mCOMPUTADOR VENCE\33[m')
    else:
        print ('\33[1;31mJOGADA INVALIDA !!\33[m')
elif computador == 1:
    if jogador == 0:
        print('\33[1;31mCOMPUTADOR VENCE\33[m')
    elif jogador  == 1:
        print('\33[1;32mEMPATE\33[1;31m')
    elif jogador == 2:
        print('\33[1;34mJOGADOR VENCE\33[1;31m')
    else:
        print('\33[1;31mJOGADA INVALIDA !!\33[m')
elif computador == 2:
    if jogador == 0:
        print('\33[1;34mJOGADOR VENCE\33[1;31m')
    elif jogador  == 1:
        print('\33[1;31mCOMPUTADOR VENCE\33[m')
    elif jogador == 2:
        print('\33[1;32mEMPATE\33[1;31m')
    else:
        print('\33[1;31mJOGADA INVALIDA !!\33[1;31m')
