print('=='*20)
print('          10 TERMOS DE UMA PA')
print('=='*20)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = t + (10 - 1) * r
for c in range(t, decimo, r):
    print('{}'.format(c), end ='-')
print('ACABOU !!')