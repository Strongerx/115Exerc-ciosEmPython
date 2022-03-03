from random import  randint
from time import sleep
computador = randint(0, 5)
print('_'*60)
print('Vou pensar em um número entre 0 e 5. Tenta adivinhar... ')
print('_'*60)
numero = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)
if numero == computador:
    print('PARABENS! Você conseguiu me vencer pensei no numero',computador)
else:
    print('GANHEI! Eu pensei no número',computador,'e não no', numero)
