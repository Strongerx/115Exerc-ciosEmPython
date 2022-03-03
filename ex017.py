from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('\33[1;31mA hipotenusa vai medir: {:.2f}\33[m'.format(hi))