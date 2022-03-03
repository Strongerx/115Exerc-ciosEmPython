'''from math import factorial
n = int(input('Qual o valor: '))
r = factorial(n)
print(r)'''
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end= '')
    f *= c
    c -= 1
print('{}'.format(f))