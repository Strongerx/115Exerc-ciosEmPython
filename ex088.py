from random import randint
from time import sleep

ms = []
nj = 0

print('-'*40)
print(f'{" JOGOS DA MEGA SENA ":^40}')
print('-'*40)

nj = int(input('Qtos jogos voce quer que eu sorteie ? '))
print('='*10, f' SORTEANDO {nj} JOGOS ', '='*10)
print()

for cnt in range(nj):
    while len(ms) <= 5:
        num = randint(1, 60)
        while num not in ms:
         ms.append(num)
    ms.sort()
    print(f'Jogo {cnt+1}: {ms}')
    ms.clear()
    sleep(0.5)

print()
print(f'{" FIM DO PROGRAMA ":=^40}')
print(f'{" < BOA SORTE ! > ":=^40}')