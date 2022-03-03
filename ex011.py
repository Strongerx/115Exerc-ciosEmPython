n1 = float(input('\33[1;34mDigite a altura da parede em metros:\33[m '))
n2 = float(input('\33[1;34mDigite a largura da parede em metros:\33[m '))
p = n1*n2
print ('A área da parede é de: \33[4;31m{:.2f}\33[m'.format(p))
print ('é necessario usar o total de \33[4;31m{:.2f}\33[m litros de tinta !!'.format(p/2))
