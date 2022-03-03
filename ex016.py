from math import trunc
num = float(input('\33[1;31mDigite um valor:\33[m '))
vl = trunc(num)

print ('O valor digitado foi de \33[1;35m{}\33[m e a sua porção inteira é de \33[1;35m{}\33[m '.format(num, vl))
