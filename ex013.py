a = float(input('Digite seu salário para saber o valor dele com 15% de aumento: \33[1;32mR$\33[m'))
d = a*15/100
vl = a+d
print('Seu salário com \33[1;31m15%\33[m de aumento é: \33[1;32mR${:.2f}\33[m'.format(vl))
