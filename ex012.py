a = float(input('Digite o preço para saber o valor do produto em 5% de desconto: \33[1;32mR$\33[m'))
d = a*5/100
vl = a-d
print('O valor com 5% de desconto é: \33[1;32mR${:.2f}\33[m'.format(vl))
