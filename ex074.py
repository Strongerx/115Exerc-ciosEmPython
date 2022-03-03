from random import *
cont = 1
maior = menor = 0
sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )
print(f'Os valores sorteados foram: {sorteio}')
print(f'O maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')