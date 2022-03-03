print('=='*20)
print('          10 TERMOS DE UMA PA')
print('=='*20)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1
while cont <= 10:
    print('{} > '.format(p), end='')
    p += r
    cont += 1
print('Acabou')