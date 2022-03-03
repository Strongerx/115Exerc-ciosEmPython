from ex108 import *
p = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))} ')
print(f'Aumentando 10%, temos {moeda(aumentar(p))}')
print(f'Reduzindo 13%, temos {moeda(diminuir(p))}')