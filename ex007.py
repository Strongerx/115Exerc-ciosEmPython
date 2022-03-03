from time import sleep

print('\33[1;34mCalculadora de médias\33[m')

n1 = float(input('\033[1;34mQual é a primeira nota?\033[m '))
n2 = float(input('\033[1;34mQual é a segunda nota?\033[m '))
print('\33[1;31mAnalisando...\33[m ')
sleep(2)
s = n1 + n2
vl = s/2
if vl > 5:
    print('Parabéns !! sua média foi de \033[4;32m{}\033[m'.format(vl))
else:
    print('Estude mais !! sua média foi de \033[4;31m{}\033[m'.format(vl))