tot = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;33m',end ='')
        tot += 1
    else:
        print('\033[1;31m', end ='')
    print('{} '.format(c), end ='')
print('\033[mO Número {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('Por isso ele é primo !')
else:
    print('Por isso ele não é primo !')
