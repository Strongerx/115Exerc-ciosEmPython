cont = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    n = int(input('Digite um número entre 0 e 10: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente ')
print(f'Você digitou o número {cont[n]}', end='')
