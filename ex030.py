numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O seu número {} é PAR'.format(numero))
else:
    print('O seu número {} é IMPAR'.format(numero))
