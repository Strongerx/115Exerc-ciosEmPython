print('_'*50)
print('Analisador de Triângulos')
print('_'*50)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmento acima Não PODEM formar um triângulo!')

