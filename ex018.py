import math
a = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(a))
coss = math.cos(math.radians(a))
tang = math.tan(math.radians(a))
print ('O valor do seno é: \33[4;36m{:.2f}\33[m'.format(seno))
print ('O valor do cosseno é: \33[4;36m{:.2f}\33[m'.format(coss))
print ('O valor da tangente é: \33[4;36m{:.2f}\33[m'.format(tang))