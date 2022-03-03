print('=='*20)
print('          10 TERMOS DE UMA PA')
print('=='*20)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(p), end='')
        p += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados !'.format(total))