from time import *
from random import *
numeros = []
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n),
        print(f'{n} ', end='')
        sleep(0.3)

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista}, temos {soma}', end='')

sorteia(numeros)
somapar(numeros)