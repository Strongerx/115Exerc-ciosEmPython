print('__'*60)
ps = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(ps))
if ps <=200:
    p1 = ps * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(p1))
else:
    p2 = ps * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(p2))
print('__'*60)