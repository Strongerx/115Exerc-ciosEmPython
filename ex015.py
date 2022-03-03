km = float(input('\33[1;34mQuantos Km rodados:\33[m '))
dias = int(input('\33[1;34mQuantos dias o carro foi alugado:\33[m '))
d = dias * 60
k = km * 0.15
v = d + k
print('O total a pagar é de \33[1;32mR${:.2f}\33[m'.format(v))

